#!/usr/bin/env python3
# Проверка целостности памятки. Запуск из корня репозитория: python3 tools/check.py
# -*- coding: utf-8 -*-
"""Проверка целостности документа: якоря, коды карточек по темам, соответствие подписи ссылки её цели."""
import re, os, glob, sys, io

ROOT = os.environ.get('GUIDE_ROOT') or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
files = {os.path.relpath(p, ROOT).replace('\\', '/'): open(p, encoding='utf-8').read()
         for p in glob.glob(ROOT + '/**/*.md', recursive=True)}

# 1. код карточки определяется файлом, в котором она лежит (вместо прежних сквозных диапазонов)
PREFIX = {"01-network-and-api": "NET", "02-traffic-and-edge": "EDGE", "03-storage-and-data": "DATA",
          "04-caching": "CACHE", "05-async-and-messaging": "MSG", "06-distributed-systems": "DIST",
          "07-architecture-styles": "ARCH", "08-reliability": "REL", "09-security": "SEC",
          "10-delivery-and-ops": "OPS", "11-performance-and-cost": "PERF", "12-case-studies": "CASE"}
CODE = r'(?:' + '|'.join(sorted(PREFIX.values(), key=len, reverse=True)) + r')-\d{2}'
ranges = {'topics/%s.md' % fn: pre for fn, pre in PREFIX.items()}

# 2. карта якорь -> код карточки (по написанным файлам)
anchor_owner = {}
for f, c in files.items():
    for m in re.finditer(r'<a id="([^"]+)"></a>\s*\n\s*\n## (' + CODE + r')', c):
        anchor_owner[(f, m.group(1))] = m.group(2)
anchors = {f: set(re.findall(r'<a id="([^"]+)"></a>', c)) for f, c in files.items()}

# 2a. якорь, определённый в файле дважды: ссылка ведёт на первое вхождение, второе — невидимая копия
dup_anchor = []
for f, c in files.items():
    seen = {}
    for a in re.findall(r'<a id="([^"]+)"></a>', c):
        seen[a] = seen.get(a, 0) + 1
    for a, n in sorted(seen.items()):
        if n > 1:
            dup_anchor.append((f, '%s — определён %d раза' % (a, n)))

bad_anchor, bad_range, bad_label = [], [], []
for f, c in files.items():
    d = os.path.dirname(f)
    for m in re.finditer(r'\[([^\]]*)\]\((?!https?:)([^)]+)\)', c):
        label, tgt = m.group(1), m.group(2)
        path, _, anc = tgt.partition('#')
        rel = os.path.normpath(os.path.join(d, path)).replace('\\', '/') if path else f
        lm = re.match(r'(' + CODE + r')', label.strip())
        # ссылка, уходящая за пределы дерева документа
        if path and (rel.startswith('..') or rel.startswith('/')):
            bad_anchor.append((f, tgt + '  ← выходит за пределы документа'))
            continue
        # ссылка на несуществующий пока файл: проверяем только диапазон ID
        if path and rel not in files:
            if lm and rel in ranges:
                pre = ranges[rel]
                if not lm.group(1).startswith(pre + '-'):
                    bad_range.append((f, label[:28], tgt, 'файл ожидает код %s-NN' % pre))
            continue
        if anc and rel in anchors and anc not in anchors[rel]:
            bad_anchor.append((f, tgt))
            continue
        if lm and rel in ranges:
            pre = ranges[rel]
            if not lm.group(1).startswith(pre + '-'):
                bad_range.append((f, label[:28], tgt, 'файл ожидает код %s-NN' % pre))
                continue
        if lm and (rel, anc) in anchor_owner and anchor_owner[(rel, anc)] != lm.group(1):
            bad_label.append((f, label[:28], tgt, 'цель — ' + anchor_owner[(rel, anc)]))

# 3. ID карточек против реестра, монотонность
reg = files['01-roadmap.md']
reg_ids = dict(re.findall(r'^\| (' + CODE + r') \| [✅○] \| (.+?) \| ', reg, flags=re.M))
cards = []
for f in sorted(files):
    if f.startswith('topics/'):
        ids = re.findall(r'^## (' + CODE + r')', files[f], flags=re.M)
        if ids != sorted(ids):
            print('НЕ ПО ПОРЯДКУ:', f)
        cards += ids

print('карточек:', len(cards), '| вне реестра:', [i for i in cards if i not in reg_ids],
      '| дубликаты:', len(cards) - len(set(cards)))
print('битых якорей:', len(bad_anchor))
for b in bad_anchor[:10]: print('   ', b)
print('код карточки не совпадает с темой файла:', len(bad_range))
for b in bad_range[:10]: print('   ', b)
print('подпись не совпадает с целью:', len(bad_label))
for b in bad_label[:10]: print('   ', b)

# 4. версии в decisions/
bad_ver = []
dec = {f: c for f, c in files.items() if f.startswith('decisions/')}
master = None
if 'decisions/00-template.md' in dec:
    m = re.search(r'^(?:- )?\*\*Версия:\*\* (\d+\.\d+)', dec['decisions/00-template.md'], flags=re.M)
    master = m.group(1) if m else None
    if not master:
        bad_ver.append(('decisions/00-template.md', 'нет версии у мастер-шаблона'))

for f, c in sorted(dec.items()):
    m = re.search(r'^(?:- )?\*\*Версия:\*\* (\d+\.\d+)', c, flags=re.M)
    if not m:
        bad_ver.append((f, 'нет строки версии'))
        continue
    ver = m.group(1)
    # соответствие мастер-шаблону
    mm = re.search(r'по мастер-шаблону \[?v(\d+\.\d+)', c)
    if f != 'decisions/00-template.md' and f != 'decisions/02-versioning.md':
        if not mm:
            bad_ver.append((f, 'не объявлена совместимость с мастер-шаблоном'))
        elif master and mm.group(1).split('.')[0] != master.split('.')[0]:
            bad_ver.append((f, 'MAJOR расходится с мастером: v%s против v%s' % (mm.group(1), master)))
    # история версий
    h = re.search(r'## История версий\s*\n\s*\n\| Версия \| Дата \| Изменение \|\s*\n\|[-| ]+\|\s*\n\| ([\d.]+) \|', c)
    if not h:
        bad_ver.append((f, 'нет истории версий или у неё другая форма'))
    elif h.group(1) != ver:
        bad_ver.append((f, 'верхняя строка истории (%s) != заявленной версии (%s)' % (h.group(1), ver)))

print('файлов решений:', len(dec), '| мастер-шаблон: v%s' % master)
print('проблем с версиями:', len(bad_ver))
for b in bad_ver[:10]: print('   ', b)

# 5. ADR в examples/: статус, метод, существование версии метода
bad_adr = []
# какие версии объявлены в истории каждого документа решений
declared = {}
for f, c in files.items():
    if f.startswith('decisions/'):
        name = os.path.basename(f).replace('.md', '')
        hist = re.search(r'## История версий(.*)$', c, flags=re.S)
        declared[name] = set(re.findall(r'^\| (\d+\.\d+) \|', hist.group(1), flags=re.M)) if hist else set()
adr_tpl_vers = declared.get('01-adr-template', set())

adrs = {f: c for f, c in files.items() if re.search(r'/ADR-\d{4}', '/' + f)}
for f, c in sorted(adrs.items()):
    if not re.search(r'^Статус:\s+(предложен|принят|отменён|заменён ADR-\d{4})', c, flags=re.M):
        bad_adr.append((f, 'нет строки статуса или статус не из словаря'))
    m = re.search(r'^Метод:\s+(D-\d\d)[^ ]* v(\d+\.\d+)(.*)$', c, flags=re.M)
    if not m:
        bad_adr.append((f, 'нет строки метода вида "D-NN vX.Y ..."'))
        continue
    doc, ver, rest = m.group(1), m.group(2), m.group(3)
    hit = [k for k in declared if k.startswith(doc + '-')]
    if not hit:
        bad_adr.append((f, 'метод ссылается на несуществующий документ ' + doc))
    elif ver not in declared[hit[0]]:
        bad_adr.append((f, '%s v%s нет в истории версий %s (есть: %s)' % (doc, ver, hit[0], ','.join(sorted(declared[hit[0]])) or '—')))
    ta = re.search(r'шаблон ADR v(\d+\.\d+)', rest)
    if not ta:
        bad_adr.append((f, 'в методе не указана версия шаблона ADR'))
    elif ta.group(1) not in adr_tpl_vers:
        bad_adr.append((f, 'шаблон ADR v%s нет в его истории версий' % ta.group(1)))

print('ADR в примерах:', len(adrs), '| проблем:', len(bad_adr))
for b in bad_adr[:10]: print('   ', b)

# 6. шапки: несколько полей подряд обязаны быть списком, иначе markdown слепит их в абзац
HEAD = re.compile(r'^(- )?\*\*[^*]+:\*\* ')
bad_head = []
for f, c in sorted(dec.items()):
    lines = c.split('\n')[:20]
    run = []
    for ln in lines:
        m = HEAD.match(ln)
        if m:
            run.append(bool(m.group(1)))
        else:
            if len(run) > 1 and not all(run):
                bad_head.append((f, 'шапка из %d полей не списком — склеится в абзац' % len(run)))
            run = []
    if len(run) > 1 and not all(run):
        bad_head.append((f, 'шапка из %d полей не списком — склеится в абзац' % len(run)))

# 9. факты, объявленные прозой в README, против того, что на диске
bad_declared = []
rd = files.get('README.md', '')
if rd:
    m = re.search(r'мастер-шаблон v(\d+\.\d+)', rd)
    if not m:
        bad_declared.append(('README.md', 'не объявлена версия мастер-шаблона'))
    elif master and m.group(1) != master:
        bad_declared.append(('README.md', 'объявлен мастер-шаблон v%s, на диске v%s' % (m.group(1), master)))
    dnums = sorted(int(re.search(r'D-(\d+)', k).group(1))
                   for k in files if re.match(r'decisions/D-\d+', k))
    m = re.search(r'D-01-…\s*…\s*D-(\d+)-…', rd)
    if m and dnums and int(m.group(1)) != dnums[-1]:
        bad_declared.append(('README.md', 'список файлов обрывается на D-%s, на диске до D-%02d'
                             % (m.group(1), dnums[-1])))

# 10. взаимность указателей между шапками документов решений
bad_mutual, _hdr = [], {}
for f, c in files.items():
    m = re.match(r'decisions/(D-\d+)', f)
    if not m:
        continue
    head = []
    for ln in c.split('\n'):
        if ln.startswith('- **'):
            head.append(ln)
        elif head and not ln.startswith('- '):
            break
    txt = '\n'.join(l for l in head
                    if l.startswith('- **Не решает:**') or l.startswith('- **Не путать с:**'))
    _hdr[m.group(1)] = set(re.findall(r'D-\d+', txt)) - {m.group(1)}
for a in sorted(_hdr):
    for b in sorted(_hdr[a]):
        if b in _hdr and a not in _hdr[b]:
            bad_mutual.append(('decisions/%s' % a, 'шапка называет %s, обратной ссылки нет' % b))

print('односторонних указателей между шапками:', len(bad_mutual))
for b in bad_mutual[:10]: print('   ', b)
print('дубликатов якорей:', len(dup_anchor))
for b in dup_anchor[:10]: print('   ', b)
print('объявленное в README не совпадает с диском:', len(bad_declared))
for b in bad_declared[:10]: print('   ', b)
# --- стадия: шапка документа против строки шага в рабочем процессе ---
STAGES = ('гринфилд', 'работающая', 'под изменением')
bad_stage = []
_doc_stage = {}
for f in sorted(glob.glob(os.path.join(ROOT, 'decisions', 'D-*.md'))):
    code = re.match(r'(D-\d+)', os.path.basename(f)).group(1)
    c = io.open(f, encoding='utf-8').read()
    m = re.search(r'^- \*\*Стадия:\*\* (.*)$', c, re.M)
    if not m:
        bad_stage.append(('decisions/%s' % os.path.basename(f), 'нет поля «Стадия» в шапке'))
        continue
    val = m.group(1).split(' — ')[0].strip()
    st = [x.strip() for x in val.split(' · ')]
    unknown = [x for x in st if x not in STAGES]
    if unknown:
        bad_stage.append(('decisions/%s' % os.path.basename(f), 'неизвестная стадия: %s' % ', '.join(unknown)))
        continue
    _doc_stage[code] = st

_wf = io.open(os.path.join(ROOT, '00-workflow.md'), encoding='utf-8').read()
_step_stage = {}
for m in re.finditer(r'^\*\*Документы шага:\*\* (.*)$', _wf, re.M):
    body = m.group(1)
    if body.startswith('нет'):
        continue
    for dm in re.finditer(r'\[(D-\d+)\]\([^)]*\)\s*`([^`]+)`', body):
        code, val = dm.group(1), dm.group(2)
        if code in _step_stage:
            bad_stage.append(('00-workflow.md', '%s назван в двух шагах' % code))
        _step_stage[code] = [x.strip() for x in val.split(' · ')]

for code in sorted(set(_doc_stage) | set(_step_stage)):
    a, b = _doc_stage.get(code), _step_stage.get(code)
    if b is None:
        bad_stage.append(('00-workflow.md', '%s не назван ни в одной строке «Документы шага»' % code))
    elif a is None:
        bad_stage.append(('00-workflow.md', '%s назван в шаге, но документа с таким кодом нет' % code))
    elif a != b:
        bad_stage.append(('%s' % code, 'шапка: «%s», шаг: «%s»' % (' · '.join(a), ' · '.join(b))))

# тот же словарь — в местных пометках [стадия: ...]
for f in sorted(glob.glob(os.path.join(ROOT, 'decisions', 'D-*.md'))):  # мастер-шаблон описывает форму пометки и содержит образцы
    rel = 'decisions/' + os.path.basename(f)
    for mk in re.finditer(r'\[стадия: ([^\]]+)\]', io.open(f, encoding='utf-8').read()):
        for x in mk.group(1).split(' · '):
            if x.strip() not in STAGES:
                bad_stage.append((rel, 'пометка называет неизвестную стадию: %s' % x.strip()))

print('стадия в шапке не совпадает со строкой шага:', len(bad_stage))
for b in bad_stage[:10]: print('   ', b)
print('шапок с полями подряд не списком:', len(bad_head))
for b in bad_head[:10]: print('   ', b)

sys.exit(1 if (bad_anchor or dup_anchor or bad_range or bad_label or bad_ver or bad_adr or bad_head or bad_declared or bad_mutual or bad_stage) else 0)
