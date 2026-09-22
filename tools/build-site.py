#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Готовит build/docs для MkDocs, не трогая раскладку репозитория.

Репозиторий остаётся источником: ни один его файл не меняется и не переезжает.
Здесь делаются только те правки, без которых сайт не совпадает с GitHub:
  * README.md становится index.md (главная страница), ссылки на него переписываются;
  * tools/check.py кладётся рядом, чтобы ссылки на проверку работали;
  * у разделов появляется страница-оглавление вместо ссылки на папку,
    которая на GitHub показывает список файлов, а на сайте не значит ничего.

Mermaid отдельной настройки не требует: Material сам находит блоки .mermaid
и рисует их в цветах текущей темы.
"""
import io, os, re, shutil, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, 'build', 'docs')
SKIP = ('.git', 'build', '_to_delete', 'site')

SECTIONS = {
    'topics':    ('Карточки', 'Двенадцать блоков, 155 карточек: механика, а не решения.'),
    'decisions': ('Решения', 'Документы решений: вопросы, оси, дисквалификаторы, форма записи.'),
    'examples':  ('Прогоны', 'Кейсы, проведённые через цепочку целиком, с ADR и находками.'),
    'research':  ('Исследование', 'Опрос поля, реестр проблем, мини-исследования и предсказания.'),
}

def title_of(path):
    with io.open(path, encoding='utf-8') as f:
        for line in f:
            if line.startswith('# '):
                return line[2:].strip()
    return os.path.basename(path)

def main():
    shutil.rmtree(os.path.join(ROOT, 'build'), ignore_errors=True)
    os.makedirs(DOCS)

    # --- markdown ---
    copied = []
    for base, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP]
        for fn in sorted(files):
            if not fn.endswith('.md'):
                continue
            src = os.path.join(base, fn)
            rel = os.path.relpath(src, ROOT).replace(os.sep, '/')
            dst_rel = 'index.md' if rel == 'README.md' else rel
            dst = os.path.join(DOCS, dst_rel)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            text = io.open(src, encoding='utf-8').read()
            # ссылки на README ведут на главную
            text = re.sub(r'(\]\((?:\.\./)*)README\.md', r'\1index.md', text)
            # ссылка на папку раздела ведёт на его страницу-оглавление
            text = re.sub(r'(\]\((?:\.\./)*)(topics|decisions|examples|research)/\)',
                          r'\1\2/index.md)', text)
            io.open(dst, 'w', encoding='utf-8').write(text)
            copied.append(dst_rel)

    # --- проверка: на неё ссылаются четыре документа ---
    os.makedirs(os.path.join(DOCS, 'tools'), exist_ok=True)
    shutil.copy(os.path.join(ROOT, 'tools', 'check.py'),
                os.path.join(DOCS, 'tools', 'check.py'))

    # --- страницы-оглавления разделов ---
    for name, (heading, lead) in SECTIONS.items():
        lines = ['# %s' % heading, '', lead, '']
        if name == 'examples':
            for run in sorted(os.listdir(os.path.join(ROOT, name))):
                ctx = os.path.join(ROOT, name, run, '00-context.md')
                if os.path.isfile(ctx):
                    lines.append('- [%s](%s/00-context.md)' % (title_of(ctx), run))
        else:
            for fn in sorted(os.listdir(os.path.join(ROOT, name))):
                if fn.endswith('.md'):
                    lines.append('- [%s](%s)' % (title_of(os.path.join(ROOT, name, fn)), fn))
        lines += ['', '> Страница собрана из файлов раздела при сборке сайта. '
                      'В репозитории её нет: там то же самое показывает список файлов папки.']
        io.open(os.path.join(DOCS, name, 'index.md'), 'w', encoding='utf-8').write('\n'.join(lines) + '\n')

    print('скопировано страниц: %d' % len(copied))
    sys.exit(subprocess.call(['mkdocs', 'build', '--strict'] + sys.argv[1:], cwd=ROOT))

if __name__ == '__main__':
    main()
