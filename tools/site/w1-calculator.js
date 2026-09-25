/* Калькулятор шага W1 «Оценки на салфетке».
 *
 * Исполняет пять пунктов метода из 00-workflow.md, ничего к ним не добавляя.
 * Если формулы здесь и в шаге разойдутся — прав шаг, а это ошибка калькулятора.
 *
 * Работает только на сайте: в репозитории GitHub скрипты не выполняет,
 * и блок остаётся пустым. Это сказано в самом шаге.
 */
(function () {
  "use strict";

  var SEC = 86400;

  // Ориентиры правдоподобия — те же, что перечислены в шаге W1
  var LIMITS = [
    { at: 5000,   text: "одна нода PostgreSQL уверенно держит тысячи простых транзакций в секунду — этого уже мало" },
    { at: 200000, text: "одна нода Redis — сотни тысяч операций в секунду; здесь и её не хватит" }
  ];

  var FIELDS = [
    { k: "dau",     l: "Пользователей в сутки",                v: 100000, hint: "DAU" },
    { k: "acts",    l: "Действий на пользователя в сутки",     v: 20 },
    { k: "fanout",  l: "Обращений внутри системы на действие", v: 1,
      hint: "во что разворачивается одно действие: справочники, проверки, записи" },
    { k: "peak",    l: "Коэффициент пика",                     v: 5,
      hint: "обычно 3–10, для событийных систем — до 100" },
    { k: "rec",     l: "Размер записи, КБ",                    v: 2 },
    { k: "months",  l: "Срок хранения, месяцев",               v: 12 },
    { k: "repl",    l: "Коэффициент репликации и индексов",    v: 2.5, hint: "обычно 2–3" },
    { k: "resp",    l: "Размер ответа, КБ",                    v: 20 }
  ];

  function num(n, d) {
    if (!isFinite(n)) return "—";
    d = d === undefined ? (n < 10 ? 1 : 0) : d;
    return n.toLocaleString("ru-RU", { maximumFractionDigits: d });
  }

  function bytes(kb) {
    var b = kb * 1024;
    var u = ["КБ", "МБ", "ГБ", "ТБ", "ПБ"];
    var i = 0, v = kb;
    while (v >= 1024 && i < u.length - 1) { v /= 1024; i++; }
    return num(v, v < 10 ? 1 : 0) + " " + u[i];
  }

  // Пункты 1–4 метода
  function compute(p) {
    var extPerDay  = p.dau * p.acts;
    var intPerDay  = extPerDay * p.fanout;
    var avgExt     = extPerDay / SEC;
    var avgInt     = intPerDay / SEC;
    var peakInt    = avgInt * p.peak;
    var volume     = extPerDay * p.rec * (p.months * 30) * p.repl;   // КБ
    var trafficKBs = avgExt * p.resp;                                 // КБ/с средний
    var trafficPeak= trafficKBs * p.peak;
    return {
      avgExt: avgExt, avgInt: avgInt, peakInt: peakInt,
      volume: volume, traffic: trafficKBs, trafficPeak: trafficPeak,
      monthTraffic: trafficKBs * SEC * 30
    };
  }

  function verdict(peakInt) {
    for (var i = LIMITS.length - 1; i >= 0; i--) {
      if (peakInt > LIMITS[i].at) return { hard: true, text: LIMITS[i].text };
    }
    return { hard: false, text: "в пределах одной ноды по нагрузке: ориентиры шага не нарушены" };
  }

  function el(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text !== undefined) e.textContent = text;
    return e;
  }

  function build(host) {
    host.classList.add("w1calc");

    var form = el("div", "w1calc__form");
    var inputs = {};
    FIELDS.forEach(function (f) {
      var wrap = el("label", "w1calc__field");
      wrap.appendChild(el("span", "w1calc__label", f.l));
      var inp = document.createElement("input");
      inp.type = "number";
      inp.min = "0";
      inp.step = "any";
      inp.value = f.v;
      inp.setAttribute("aria-label", f.l);
      inputs[f.k] = inp;
      wrap.appendChild(inp);
      if (f.hint) wrap.appendChild(el("span", "w1calc__hint", f.hint));
      form.appendChild(wrap);
    });
    host.appendChild(form);

    var out = el("div", "w1calc__out");
    host.appendChild(out);

    function read() {
      var p = {};
      FIELDS.forEach(function (f) {
        var v = parseFloat(inputs[f.k].value);
        p[f.k] = isFinite(v) && v >= 0 ? v : 0;
      });
      return p;
    }

    function render() {
      var p = read();
      var base = compute(p);
      // Проверка на порядок: что изменится, если ошиблись в десять раз
      var up   = compute(Object.assign({}, p, { dau: p.dau * 10 }));
      var down = compute(Object.assign({}, p, { dau: p.dau / 10 }));

      out.innerHTML = "";

      var rows = [
        ["Средний RPS, снаружи",     num(base.avgExt),  num(up.avgExt),  num(down.avgExt)],
        ["Средний RPS, внутри",      num(base.avgInt),  num(up.avgInt),  num(down.avgInt)],
        ["Пиковый RPS, внутри",      num(base.peakInt), num(up.peakInt), num(down.peakInt)],
        ["Объём за срок хранения",   bytes(base.volume), bytes(up.volume), bytes(down.volume)],
        ["Исходящий трафик, пик",    bytes(base.trafficPeak) + "/с", bytes(up.trafficPeak) + "/с", bytes(down.trafficPeak) + "/с"],
        ["Исходящий трафик в месяц", bytes(base.monthTraffic), bytes(up.monthTraffic), bytes(down.monthTraffic)]
      ];

      var tbl = el("table", "w1calc__table");
      var thead = el("thead");
      var htr = el("tr");
      ["Показатель", "Как есть", "×10", "÷10"].forEach(function (h) {
        htr.appendChild(el("th", null, h));
      });
      thead.appendChild(htr);
      tbl.appendChild(thead);
      var tb = el("tbody");
      rows.forEach(function (r) {
        var tr = el("tr");
        r.forEach(function (c, i) {
          var td = el("td", i === 0 ? null : "w1calc__num", c);
          tr.appendChild(td);
        });
        tb.appendChild(tr);
      });
      tbl.appendChild(tb);
      out.appendChild(tbl);

      // Вердикт и проверка на порядок — это и есть «готово, когда видно узкое место»
      var vb = verdict(base.peakInt), vu = verdict(up.peakInt), vd = verdict(down.peakInt);
      var note = el("div", "w1calc__note");
      note.appendChild(el("strong", null, vb.hard ? "Упирается: " : "Пока не упирается: "));
      note.appendChild(document.createTextNode(vb.text + "."));
      out.appendChild(note);

      var ord = el("div", "w1calc__note");
      if (vb.hard !== vu.hard || vb.hard !== vd.hard) {
        ord.appendChild(el("strong", null, "Ошибка на порядок меняет вывод. "));
        ord.appendChild(document.createTextNode(
          "Значит, число надо уточнять до того, как выбирать архитектуру: именно этого требует шаг."));
      } else {
        ord.appendChild(el("strong", null, "Ошибка на порядок вывода не меняет. "));
        ord.appendChild(document.createTextNode(
          "Значит, точность здесь не решает, и уточнять число незачем — решает что-то другое."));
      }
      out.appendChild(ord);

      if (p.fanout === 1) {
        var w = el("div", "w1calc__warn");
        w.appendChild(el("strong", null, "Разворачивание оставлено единицей. "));
        w.appendChild(document.createTextNode(
          "Шаг предупреждает: считаются входные события, а не то, во что событие разворачивается. " +
          "На прогоне U-02 0,17 подачи в секунду обернулись 933 обращениями — перевёрнуто в 5 500 раз."));
        out.appendChild(w);
      }
    }

    form.addEventListener("input", render);
    render();
  }

  function init() {
    var host = document.getElementById("w1-calc");
    if (host && !host.dataset.ready) {
      host.dataset.ready = "1";
      build(host);
    }
  }

  document.addEventListener("DOMContentLoaded", init);
  // Material переключает страницы без перезагрузки
  if (window.document$ && window.document$.subscribe) window.document$.subscribe(init);
})();
