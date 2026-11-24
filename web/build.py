import json
from pathlib import Path
from content import LESSONS

HERE = Path(__file__).resolve().parent
template = (HERE / 'template.html').read_text(encoding='utf-8')
for i, item in enumerate(LESSONS):
    assert item['sections'] and item['refs']
    for q in item['questions']:
        assert 0 <= q['answer'] < len(q['options'])
data = json.dumps(LESSONS, ensure_ascii=False).replace('</', '<\\/')
html = template.replace('/*__STYLE__*/', (HERE / 'style.css').read_text(encoding='utf-8'))
html = html.replace('/*__DATA__*/', 'const LESSONS = ' + data + ';')
html = html.replace('/*__APP__*/', (HERE / 'app.js').read_text(encoding='utf-8'))
assert '/*__' not in html
(HERE.parent / 'index.html').write_text(html, encoding='utf-8')
print(f'Built {len(LESSONS)} lessons / {sum(len(x["questions"]) for x in LESSONS)} quizzes / {len(html.encode("utf-8")):,} bytes')
