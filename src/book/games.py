"""Разные игры для страниц букв: у каждой буквы — своя игра."""
import random, math
from lib import star, flower, AR

INK = "#4A2C27"
F = 'font-family="Amiri" font-weight="700" text-anchor="middle"'

def _pool(letter, group, all_letters, k):
    pool = [x for x in group if x != letter] + random.sample([l for l in all_letters if l != letter and l not in group], 3)
    return random.choices(pool, k=k)

def _mix(letter, n_target, n_total, group, all_letters):
    cells = [letter] * n_target + _pool(letter, group, all_letters, n_total - n_target)
    random.shuffle(cells)
    return cells

def svg(body, h=230):
    return f'<svg viewBox="0 0 600 {h}" class="game" xmlns="http://www.w3.org/2000/svg">{body}</svg>'

# 1. шарики
def balloons(letter, g, al):
    cells = _mix(letter, 5, 12, g, al)
    cols = ["#E8505B", "#F2B544", "#6F86C2", "#6DBE6A", "#C9A0DC", "#F29A4A"]
    b = ""
    for i, c in enumerate(cells):
        x = 50 + (i % 6) * 100 + (25 if i >= 6 else 0); y = 60 + (i // 6) * 110
        col = cols[i % 6]
        b += (f'<path d="M{x} {y+42} Q{x-8} {y+70} {x+4} {y+96}" stroke="#9C8478" stroke-width="1.5" fill="none"/>'
              f'<ellipse cx="{x}" cy="{y}" rx="32" ry="38" fill="#fff" stroke="{col}" stroke-width="3.5"/>'
              f'<path d="M{x-4} {y+38} L{x+4} {y+38} L{x} {y+45}Z" fill="{col}"/>'
              f'<path d="M{x-18} {y-16} q6 -10 14 -12" stroke="{col}" stroke-width="3" fill="none" opacity=".5" stroke-linecap="round"/>'
              f'<text x="{x}" y="{y+14}" {F} font-size="46" fill="{INK}">{c}</text>')
    return ("Праздник шариков! Раскрась все шарики с буквой", svg(b, 260))

# 2. рыбалка
def fishing(letter, g, al):
    cells = _mix(letter, 3, 8, g, al)
    b = '<rect x="6" y="6" width="588" height="250" rx="40" fill="#E4EEF8" stroke="#8E9DC6" stroke-width="2.5"/>'
    b += "".join(f'<path d="M{20+i*64} 26 q16 -10 32 0" stroke="#fff" stroke-width="3" fill="none"/>' for i in range(9))
    for i, c in enumerate(cells):
        x = 90 + (i % 4) * 140 + (30 if i >= 4 else 0); y = 85 + (i // 4) * 110
        b += (f'<path d="M{x-58} {y} Q{x-10} {y-46} {x+40} {y} Q{x-10} {y+46} {x-58} {y}Z" fill="#fff" stroke="#F29A4A" stroke-width="3.5"/>'
              f'<path d="M{x+38} {y} L{x+64} {y-22} L{x+64} {y+22}Z" fill="#F29A4A"/><circle cx="{x-40}" cy="{y-8}" r="4" fill="{INK}"/>'
              f'<text x="{x-4}" y="{y+17}" {F} font-size="48" fill="{INK}">{c}</text>')
    return ("Рыбалка! Обведи кружком рыбок с буквой", svg(b, 262))

# 3. звёздное небо
def stars(letter, g, al):
    cells = _mix(letter, 5, 12, g, al)
    b = '<rect x="10" y="10" width="580" height="240" rx="30" fill="#3E5180"/>'
    random.seed(len(cells) + ord(letter))
    b += "".join(f'<circle cx="{random.randint(20, 580)}" cy="{random.randint(20, 240)}" r="1.5" fill="#fff" opacity=".7"/>' for _ in range(40))
    for i, c in enumerate(cells):
        x = 60 + (i % 6) * 96; y = 75 + (i // 6) * 110 + (20 if i % 2 else 0)
        b += star(x, y, 44, "#FFF6E0", stroke="#D8B26A") + f'<text x="{x}" y="{y+15}" {F} font-size="36" fill="{INK}">{c}</text>'
    return ("Звёздное небо! Раскрась жёлтым звёзды с буквой", svg(b, 260))

# 4. цветочная полянка
def meadow(letter, g, al):
    cells = _mix(letter, 4, 10, g, al)
    b = '<path d="M10 200 Q300 170 590 200 L590 250 L10 250Z" fill="#DCE8D2"/>'
    pet = ["#E9A0B8", "#C9A0DC", "#F2B544", "#8FC3EC"]
    for i, c in enumerate(cells):
        x = 60 + i * 54 + (0 if i < 10 else 0); y = 80 + (i % 2) * 60
        x = 55 + (i % 5) * 120 + (i // 5) * 55; y = 70 + (i // 5) * 100
        b += f'<path d="M{x} {y+30} Q{x+4} {y+60} {x} {y+90}" stroke="#5E9E4E" stroke-width="4" fill="none"/>'
        b += "".join(f'<ellipse cx="{x + 30*math.cos(a/57.3):.0f}" cy="{y + 30*math.sin(a/57.3):.0f}" rx="17" ry="17" fill="{pet[i % 4]}" opacity=".85"/>' for a in range(0, 360, 60))
        b += f'<circle cx="{x}" cy="{y}" r="26" fill="#FFF8EA" stroke="#D8B26A" stroke-width="2.5"/><text x="{x}" y="{y+13}" {F} font-size="34" fill="{INK}">{c}</text>'
    return ("Цветочная полянка! Помоги пчёлке найти цветы с буквой — раскрась их", svg(b, 255))

# 5. яблоня
def apple_tree(letter, g, al):
    cells = _mix(letter, 4, 10, g, al)
    b = ('<rect x="280" y="170" width="40" height="80" rx="8" fill="#9C6B3E"/>'
         '<ellipse cx="300" cy="115" rx="270" ry="105" fill="#A8C49A"/><ellipse cx="200" cy="100" rx="120" ry="70" fill="#B9D2AA"/><ellipse cx="420" cy="110" rx="120" ry="70" fill="#B9D2AA"/>')
    pos = [(110, 90), (200, 50), (300, 40), (400, 50), (490, 90), (150, 155), (250, 120), (350, 120), (450, 155), (300, 185)]
    for (x, y), c in zip(pos, cells):
        b += (f'<circle cx="{x}" cy="{y}" r="30" fill="#fff" stroke="#E8505B" stroke-width="3"/><path d="M{x} {y-30} q3 -10 10 -12" stroke="#7A4A30" stroke-width="3" fill="none"/>'
              f'<text x="{x}" y="{y+13}" {F} font-size="34" fill="{INK}">{c}</text>')
    return ("Яблоня! Раскрась красным яблоки с буквой, остальные — зелёным", svg(b, 255))

# 6. сколько букв?
def count_game(letter, g, al):
    rows = []
    for r in range(3):
        n = [3, 2, 4][r]
        rows.append(_mix(letter, n, 7, g, al))
    b = ""
    for r, row in enumerate(rows):
        y = 50 + r * 75
        b += f'<rect x="10" y="{y-38}" width="580" height="64" rx="18" fill="#F7F0E8"/>'
        for i, c in enumerate(row):
            x = 560 - i * 66
            b += f'<text x="{x - 40}" y="{y+12}" {F} font-size="40" fill="{INK}">{c}</text>'
        b += f'<rect x="22" y="{y-28}" width="48" height="44" rx="10" fill="#fff" stroke="#9C8478" stroke-width="2" stroke-dasharray="5 4"/>'
    return ("Посчитай! Сколько раз в каждом ряду спряталась буква? Впиши число в окошко слева", svg(b, 240))

# 7. соедини одинаковые
def connect_same(letter, g, al):
    others = list(dict.fromkeys([x for x in g if x != letter] + random.sample([l for l in al if l != letter and l not in g], 4)))[:3]
    left = [letter] + others
    right = left[:]
    random.shuffle(right)
    while right == left:
        random.shuffle(right)
    b = ""
    for i, (a, c) in enumerate(zip(left, right)):
        y = 35 + i * 55
        b += (f'<rect x="420" y="{y-24}" width="80" height="48" rx="14" fill="#F6E1D8"/><text x="460" y="{y+13}" {F} font-size="34" fill="{INK}">{a}</text><circle cx="410" cy="{y}" r="6" fill="{INK}"/>'
              f'<rect x="100" y="{y-24}" width="80" height="48" rx="14" fill="#E4E9F4"/><text x="140" y="{y+13}" {F} font-size="34" fill="{INK}">{c}</text><circle cx="190" cy="{y}" r="6" fill="{INK}"/>')
    return ("Найди пару! Соедини линией одинаковые буквы", svg(b, 240))

# 8. дорожка к домику
def path_home(letter, g, al):
    random.seed(ord(letter) * 3)
    path = {(0, 0), (1, 0), (1, 1), (1, 2), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (2, 5), (2, 6)}
    b = '<path d="M590 30 L560 6 L530 30Z" fill="#A8473B"/><rect x="535" y="30" width="50" height="34" fill="#F4EBE2" stroke="#5C342E" stroke-width="2"/>'
    others = [x for x in g if x != letter] or random.sample([l for l in al if l != letter], 3)
    for r in range(3):
        for c in range(7):
            x = 500 - c * 74; y = 90 + r * 62
            ch = letter if (r, c) in path else random.choice(others + random.sample([l for l in al if l != letter], 2))
            b += f'<rect x="{x-30}" y="{y-28}" width="60" height="54" rx="14" fill="#F7F0E8" stroke="#DCCDBF" stroke-width="2"/><text x="{x}" y="{y+13}" {F} font-size="32" fill="{INK}">{ch}</text>'
    b += f'<text x="560" y="96" font-family="Nunito" font-weight="900" font-size="14" text-anchor="middle" fill="#3E5180">старт</text>'
    b += f'<path d="M30 290 h40" stroke="#C9A15B" stroke-width="3"/><g transform="translate(40 255)"><path d="M-22 0 L0 -18 L22 0Z" fill="#3E5180"/><rect x="-16" y="0" width="32" height="24" fill="#FBF6F0" stroke="#3E5180" stroke-width="2"/></g>'
    return ("Дорожка домой! Шагай только по буквам — от старта к домику внизу", svg(b, 290))

# 9. охота (как раньше)
def hunt(letter, g, al):
    cells = _mix(letter, 7, 20, g, al)
    grid = "".join(f'<div class="hc"><span lang="ar" dir="rtl">{c}</span></div>' for c in cells)
    return ("Охота за буквами! Найди и раскрась все буквы", f'<div class="hunt" dir="rtl">{grid}</div>')

GAMES = [hunt, balloons, fishing, stars, meadow, apple_tree, count_game, connect_same, path_home]

def game_for(idx, letter, group, all_letters):
    random.seed(idx * 31 + 7)
    fn = GAMES[(idx - 1) % len(GAMES)]
    head, body = fn(letter, group, all_letters)
    return f'{head} {AR(letter, "inl")}', body, fn.__name__
