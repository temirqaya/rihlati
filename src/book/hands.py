"""Схема «ручки букв»: открытая ладонь — буква соединяется с этой стороны, кулачок — нет."""
from lib import AR, INK

SKIN, SKD = "#F6DCC6", "#C99A7A"

def palm(flip=False, w=80):
    # ладонь пальцами наружу (влево); flip — пальцами вправо
    g = (f'<rect x="54" y="30" width="34" height="40" rx="12" fill="{SKIN}" stroke="{SKD}" stroke-width="2.5"/>'
         + "".join(f'<rect x="{x}" y="{y}" width="{l}" height="10" rx="5" fill="{SKIN}" stroke="{SKD}" stroke-width="2.5"/>' for x, y, l in [(14, 30, 46), (8, 41, 52), (12, 52, 48), (22, 63, 38)])
         + f'<path d="M66 30 Q60 12 46 10 Q42 16 52 28" fill="{SKIN}" stroke="{SKD}" stroke-width="2.5" stroke-linejoin="round"/>'
         + f'<rect x="84" y="36" width="12" height="28" rx="4" fill="#EAC9AF" stroke="{SKD}" stroke-width="2"/>')
    tr = ' transform="translate(100 0) scale(-1 1)"' if flip else ""
    return f'<svg viewBox="0 0 100 80" width="{w}" class="hand"><g{tr}>{g}</g></svg>'

def fist(flip=False, w=80):
    g = (f'<rect x="30" y="18" width="56" height="48" rx="18" fill="{SKIN}" stroke="{SKD}" stroke-width="2.5"/>'
         + "".join(f'<path d="M30 {y} q-10 0 -10 6 q0 6 10 6" fill="{SKIN}" stroke="{SKD}" stroke-width="2.5"/>' for y in (22, 34, 46))
         + f'<path d="M40 56 q14 -8 30 2" stroke="{SKD}" stroke-width="2.5" fill="none" stroke-linecap="round"/>'
         + f'<rect x="84" y="28" width="12" height="28" rx="4" fill="#EAC9AF" stroke="{SKD}" stroke-width="2"/>')
    tr = ' transform="translate(100 0) scale(-1 1)"' if flip else ""
    return f'<svg viewBox="0 0 100 80" width="{w}" class="hand"><g{tr}>{g}</g></svg>'

def scheme(letter, connects=True, w=70, color="#3E5180"):
    """4 строки: отдельно, в начале, в середине, в конце. Левая рука — связь со СЛЕДУЮЩЕЙ буквой, правая — с ПРЕДЫДУЩЕЙ."""
    rows = [("отдельно", letter, False, False), ("в начале", letter + "ـ", True, False),
            ("в середине", "ـ" + letter + "ـ", True, True), ("в конце", "ـ" + letter, False, True)]
    if not connects:
        rows = [rows[0], rows[3]]
    out = ""
    for lab, form, left_open, right_open in rows:
        lh = palm(False, w) if left_open else fist(False, w)
        rh = palm(True, w) if right_open else fist(True, w)
        out += f'<div class="hs-row"><div class="hs-h">{lh}</div><div class="hs-l" lang="ar" style="color:{color}">{form}</div><div class="hs-h">{rh}</div><small>{lab}</small></div>'
    return f'<div class="hscheme">{out}</div>'
