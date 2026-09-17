#!/usr/bin/env python3
# Проверка целостности памятки. Запуск из корня репозитория: python3 tools/check.py
# -*- coding: utf-8 -*-
"""Проверка целостности документа: якоря, диапазоны ID по блокам, соответствие подписи ссылки её цели."""
import re, os, glob, sys

ROOT = os.environ.get('GUIDE_ROOT') or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
files = {os.path.relpath(p, ROOT).replace('\\', '/'): open(p, encoding='utf-8').read()
         for p in glob.glob(ROOT + '/**/*.md', recursive=True)}

# 1. диапазоны ID по блокам из реестра
reg = files['01-roadmap.md']
BLOCK_FILE = {"B01": "01-network-and-api", "B02": "02-traffic-and-edge", "B03": "03-storage-and-data",
              "B04": "04-caching", "B05": "05-async-and-messaging", "B06": "06-distributed-systems",
              "B07": "07-architecture-styles", "B08": "08-reliability", "B09": "09-security",
              "B10": "10-delivery-and-ops", "B11": "11-performance-and-cost", "B12": "12-case-studies"}
ranges = {}
for m in re.finditer(r'^### (B\d\d) · .+?\n\n`topics/([\w-]+)\.md`(.*?)(?=^### |\Z)', reg, flags=re.M | re.S):
    blk, fn, body = m.group(1), m.group(2), m.group(3)
    ids = re.findall(r'^\| (T-\d{3}) \|', body, flags=re.M)
    if ids:
        ranges['topics/%s.md' % fn] = (ids[0], ids[-1], blk)

# 2. карта якорь -> ID карточки (по написанным файлам)
anchor_owner = {}
for f, c in files.items():
    for m in re.finditer(r'<a id="([^"]+)"></a>\s*\n\s*\n## (T-\d{3})', c):
        anchor_owner[(f, m.group(1))] = m.group(2)
anchors = {f: set(re.findall(r'<a id="([^"]+)"></a>', c)) for f, c in files.items()}

bad_anchor, bad_range, bad_label = [], [], []
for f, c in files.items():
    d = os.path.dirname(f)
    for m in re.finditer(r'\[([^\]]*)\]\((?!https?:)([^)]+)\)', c):
        label, tgt = m.group(1), m.group(2)
        path, _, anc = tgt.partition('#')
        rel = os.path.normpath(os.path.join(d, path)).replace('\\', '/') if path else f
        lm = re.match(r'(T-\d{3})', label.strip())
        # ссылка, уходящая за пределы дерева документа
        if path and (rel.startswith('..') or rel.startswith('/')):
            bad_anchor.append((f, tgt + '  ← выходит за пределы документа'))
            continue
        # ссылка на несуществующий пока файл: проверяем только диапазон ID
        if path and rel not in files:
            if lm and rel in ranges:
                lo, hi, blk = ranges[rel]
                if not (lo <= lm.group(1) <= hi):
                    bad_range.append((f, label[:28], tgt, '%s ожидает %s..%s' % (blk, lo, hi)))
            continue
        if anc and rel in anchors and anc not in anchors[rel]:
            bad_anchor.append((f, tgt))
            continue
        if lm and rel in ranges:
            lo, hi, blk = ranges[rel]
            if not (lo <= lm.group(1) <= hi):
                bad_range.append((f, label[:28], tgt, '%s ожидает %s..%s' % (blk, lo, hi)))
                continue
        if lm and (rel, anc) in anchor_owner and anchor_owner[(rel, anc)] != lm.group(1):
            bad_label.append((f, label[:28], tgt, 'цель — ' + anchor_owner[(rel, anc)]))

# 3. ID карточек против реестра, монотонность
reg_ids = dict(re.findall(r'^\| (T-\d{3}) \| [✅○] \| (.+?) \| ', reg, flags=re.M))
cards = []
for f in sorted(files):
    if f.startswith('topics/'):
        ids = re.findall(r'^## (T-\d{3})', files[f], flags=re.M)
        if ids != sorted(ids):
            print('НЕ ПО ПОРЯДКУ:', f)
        cards += ids

print('карточек:', len(cards), '| вне реестра:', [i for i in cards if i not in reg_ids],
      '| дубликаты:', len(cards) - len(set(cards)))
print('битых якорей:', len(bad_anchor))
for b in bad_anchor[:10]: print('   ', b)
print('ID вне диапазона блока:', len(bad_range))
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

print('шапок с полями подряд не списком:', len(bad_head))
for b in bad_head[:10]: print('   ', b)

sys.exit(1 if (bad_anchor or bad_range or bad_label or bad_ver or bad_adr or bad_head) else 0)
