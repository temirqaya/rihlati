"""Перевод мира намаза: вытаскиваем русские фрагменты из готовой структуры NW
и заменяем по словарю nw_<lang>.json (ключ — русский фрагмент)."""
import re, json, os
CYR = re.compile('[А-Яа-яЁё]')
INLINE = r'(?:b|/b|br/?|br /)'
SPLIT = re.compile(r'(<(?!' + INLINE + r'>)[^>]+>)')

def units_of(s):
    """Русские фрагменты строки. Для HTML — текст между блочными тегами (с <b> внутри)."""
    out = []
    if '<' in s:
        for part in SPLIT.split(s):
            if part.startswith('<') and not re.match(r'<' + INLINE + '>', part):
                # атрибуты тоже могут содержать текст (aria-label, title)
                continue
            if CYR.search(part): out.append(part.strip())
    elif CYR.search(s):
        out.append(s.strip())
    return out

def walk(o, f):
    if isinstance(o, dict): return {k: (walk(v, f) if k not in ('id', 'world', 'color', 'icon') else v) for k, v in o.items()}
    if isinstance(o, list): return [walk(v, f) for v in o]
    if isinstance(o, str): return f(o)
    return o

def collect(nw):
    seen = []
    def f(s):
        for u in units_of(s):
            if u not in seen: seen.append(u)
        return s
    walk(nw, f); return seen

def apply(nw, T, missing):
    def tr1(u):
        if u in T and T[u]: return T[u]
        missing.add(u); return u
    def f(s):
        if '<' in s:
            parts = SPLIT.split(s)
            return ''.join(p if (p.startswith('<') and not re.match(r'<' + INLINE + '>', p)) or not CYR.search(p)
                           else p.replace(p.strip(), tr1(p.strip())) for p in parts)
        return s.replace(s.strip(), tr1(s.strip())) if CYR.search(s) else s
    return walk(nw, f)

def load(lang):
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'nw_{lang}.json')
    return json.load(open(p)) if os.path.exists(p) else {}
