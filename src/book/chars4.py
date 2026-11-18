"""Зейнеб и Юсуф — новые персонажи, нарисованы с нуля.
Один рисунок на все языки, меняется только палитра (pal = PAL['ru'|'ct'|'tr']).
API как у chars/chars3: adam(w, left, right, mood, book, pal), maryam(...)."""
import itertools
_ids = itertools.count(5000)

SKIN, SKIN_L, SKIN_D = "#F6D9C3", "#FDEBDD", "#E4B898"
LINE = "#6B4A3C"
EYE = "#2F2420"
HAIR, HAIR_L = "#3B2A22", "#57402F"

PAL = {
    # Юсуф: tunic, tunic_d, trim, cap, cap_trim, pants  |  Зейнеб: scarf, scarf_d, scarf_trim, dress, dress_d, dress_trim, pin
    'ru': dict(tunic="#7FA2D6", tunic_d="#5F82BC", trim="#F4C96B", cap="#FFFDF7", cap_trim="#7FA2D6", pants="#EDE6DA",
               scarf="#F6C9D3", scarf_d="#E8A9B8", scarf_trim="#FFFFFF", dress="#A895D6", dress_d="#8775BE", dress_trim="#F4C96B", pin="#F4C96B"),
    'ct': dict(tunic="#4E7D69", tunic_d="#3B6353", trim="#D8B062", cap="#B5523A", cap_trim="#D8B062", pants="#EFE6D6",
               scarf="#F5ECDD", scarf_d="#E2D3BC", scarf_trim="#C9716A", dress="#C9716A", dress_d="#A9564F", dress_trim="#D8B062", pin="#7E9A6A"),
    'tr': dict(tunic="#2F6E9C", tunic_d="#225478", trim="#E9C46A", cap="#FFFDF7", cap_trim="#3E9A8E", pants="#ECE7DE",
               scarf="#8FD0C8", scarf_d="#6DB5AC", scarf_trim="#FFFFFF", dress="#E07F67", dress_d="#C4634D", dress_trim="#2F6E9C", pin="#E9C46A"),
}

def _defs(u, p):
    return (f'<defs>'
            f'<radialGradient id="sk{u}" cx=".42" cy=".38" r=".8"><stop offset="0" stop-color="{SKIN_L}"/><stop offset="1" stop-color="{SKIN}"/></radialGradient>'
            f'<radialGradient id="bl{u}"><stop offset="0" stop-color="#F08F8A" stop-opacity=".75"/><stop offset="1" stop-color="#F08F8A" stop-opacity="0"/></radialGradient>'
            f'<linearGradient id="tu{u}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{p["tunic"]}"/><stop offset="1" stop-color="{p["tunic_d"]}"/></linearGradient>'
            f'<linearGradient id="dr{u}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{p["dress"]}"/><stop offset="1" stop-color="{p["dress_d"]}"/></linearGradient>'
            f'<linearGradient id="sc{u}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{p["scarf"]}"/><stop offset="1" stop-color="{p["scarf_d"]}"/></linearGradient>'
            f'</defs>')

def _eye(x, cy, closed, lashes, left):
    if closed:
        return f'<path d="M{x-8} {cy} q8 7 16 0" stroke="{EYE}" stroke-width="2.8" fill="none" stroke-linecap="round"/>'
    out = (f'<ellipse cx="{x}" cy="{cy}" rx="8.5" ry="10.5" fill="{EYE}"/>'
           f'<ellipse cx="{x}" cy="{cy+4}" rx="6" ry="4.5" fill="#5A4034" opacity=".7"/>'
           f'<circle cx="{x+3}" cy="{cy-4}" r="3.4" fill="#fff"/><circle cx="{x-3}" cy="{cy+4}" r="1.6" fill="#fff" opacity=".9"/>')
    if lashes:
        s = -1 if left else 1
        out += f'<path d="M{x+s*6} {cy-8} q{s*3} -2 {s*5} -6" stroke="{EYE}" stroke-width="2.2" fill="none" stroke-linecap="round"/>'
    return out

def _face(u, cx, cy, mood, lashes=False):
    brows = (f'<path d="M{cx-28} {cy-17} q8 -5 15 -1" stroke="{HAIR}" stroke-width="2.4" fill="none" stroke-linecap="round" opacity=".55"/>'
             f'<path d="M{cx+13} {cy-18} q7 -4 15 1" stroke="{HAIR}" stroke-width="2.4" fill="none" stroke-linecap="round" opacity=".55"/>')
    if mood == "open":
        mouth = (f'<path d="M{cx-8} {cy+18} q8 2.5 16 0 q-2 11 -8 11 q-6 0 -8 -11z" fill="#B24E4A"/>'
                 f'<path d="M{cx-4} {cy+25} q4 -3 8 0 q-1 3 -4 3 q-3 0 -4 -3z" fill="#E9837E"/>')
    else:
        mouth = f'<path d="M{cx-7} {cy+19} q7 7 14 0" stroke="#A24642" stroke-width="2.8" fill="none" stroke-linecap="round"/>'
    blush = (f'<ellipse cx="{cx-31}" cy="{cy+13}" rx="10" ry="6.5" fill="#F08F8A" opacity=".35"/>'
             f'<ellipse cx="{cx+31}" cy="{cy+13}" rx="10" ry="6.5" fill="#F08F8A" opacity=".35"/>')
    nose = f'<path d="M{cx-2.5} {cy+10} q2.5 2.5 5 0" stroke="{SKIN_D}" stroke-width="2.4" fill="none" stroke-linecap="round"/>'
    e = _eye(cx - 19, cy, mood in ("closed", "wink"), lashes, True) + _eye(cx + 19, cy, mood == "closed", lashes, False)
    return brows + e + blush + nose + mouth

def _arm(side, pose, sleeve, cuff, x0, y0, u):
    s = side
    if pose == "wave":
        d, hx, hy = f"M{x0} {y0} q{s*26} -4 {s*30} -44", x0 + s*31, y0 - 52
    elif pose == "point":
        d, hx, hy = f"M{x0} {y0} q{s*22} 6 {s*42} -8", x0 + s*48, y0 - 10
    elif pose == "dua":
        d, hx, hy = f"M{x0} {y0} q{s*10} 30 {-s*12} 22", x0 - s*14, y0 + 16
    elif pose == "hold":
        d, hx, hy = f"M{x0} {y0} q{s*10} 24 {-s*8} 36", x0 - s*12, y0 + 40
    else:
        d, hx, hy = f"M{x0} {y0} q{s*14} 22 {s*10} 46", x0 + s*10, y0 + 52
    if pose == "dua":
        hand = f'<ellipse cx="{hx}" cy="{hy}" rx="9.5" ry="12.5" transform="rotate({-s*20} {hx} {hy})" fill="{SKIN}" stroke="{SKIN_D}" stroke-width="1.6"/>'
    else:
        hand = f'<circle cx="{hx}" cy="{hy}" r="9.5" fill="{SKIN}" stroke="{SKIN_D}" stroke-width="1.6"/>'
    cx, cy = hx - (hx - x0) * 0.12, hy - (hy - y0) * 0.12
    return (f'<path d="{d}" stroke="{LINE}" stroke-width="23" fill="none" stroke-linecap="round" opacity=".28"/>'
            f'<path d="{d}" stroke="{sleeve}" stroke-width="19.5" fill="none" stroke-linecap="round"/>'
            f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="10.5" fill="{cuff}"/>' + hand)

def _book(cx, cy, col):
    return (f'<g transform="translate({cx} {cy})"><path d="M-30 -4 Q-15 -12 0 -4 Q15 -12 30 -4 V24 Q15 16 0 24 Q-15 16 -30 24Z" fill="#FFFDF7" stroke="{LINE}" stroke-width="1.8" stroke-linejoin="round"/>'
            f'<path d="M0 -4 V24" stroke="{LINE}" stroke-width="1.4"/><path d="M-32 -2 V27 Q-16 19 0 27 Q16 19 32 27 V-2" fill="none" stroke="{col}" stroke-width="4" stroke-linejoin="round"/>'
            + "".join(f'<path d="M{a} {b} h{w}" stroke="#C9B9A6" stroke-width="1.6" stroke-linecap="round"/>' for a, b, w in [(-24, 3, 18), (-24, 9, 16), (-24, 15, 18), (6, 3, 18), (8, 9, 16), (6, 15, 18)])
            + '</g>')

def _stars_band(x1, x2, y, col):
    return "".join(f'<path d="M{x} {y-4} l1.6 3.2 3.4 .5 -2.5 2.4 .6 3.4 -3.1 -1.6 -3.1 1.6 .6 -3.4 -2.5 -2.4 3.4 -.5z" fill="{col}"/>' for x in range(int(x1), int(x2), 13))

def adam(w=150, left="down", right="wave", mood="smile", book=False, pal='ru'):
    p = PAL[pal] if isinstance(pal, str) else pal
    u = next(_ids)
    if book: left, right = "hold", "hold"
    la = _arm(-1, left, p["tunic"], p["trim"], 68, 176, u)
    ra = _arm(1, right, p["tunic"], p["trim"], 132, 176, u)
    body = (f'<ellipse cx="100" cy="291" rx="52" ry="6" fill="#4A3028" opacity=".12"/>'
            # ноги и обувь
            f'<path d="M80 248 L79 280 H97 L99 256 L101 256 L103 280 H121 L120 248Z" fill="{p["pants"]}" stroke="{LINE}" stroke-width="1.8" stroke-linejoin="round"/>'
            f'<path d="M77 278 q-13 0 -13 8 q0 5 15 5 h13 q5 0 5 -6z M123 278 q13 0 13 8 q0 5 -15 5 h-13 q-5 0 -5 -6z" fill="#5A3E33"/>'
            # длинная рубаха
            f'<path d="M70 166 Q100 154 130 166 L142 256 Q100 266 58 256Z" fill="{p['tunic']}" stroke="{LINE}" stroke-width="2" stroke-linejoin="round"/>'
            f'<path d="M100 166 V214" stroke="{p["trim"]}" stroke-width="3"/>'
            + "".join(f'<circle cx="100" cy="{y}" r="2.3" fill="#FFFDF7"/>' for y in (178, 191, 204))
            + f'<path d="M86 163 Q100 175 114 163" stroke="{p["trim"]}" stroke-width="4" fill="none" stroke-linecap="round"/>'
            + f'<path d="M60 250 Q100 260 140 250" stroke="{p["trim"]}" stroke-width="4" fill="none"/>' + _stars_band(66, 136, 244, p["trim"]))
    head = (f'<path d="M92 142 h16 v22 q-8 5 -16 0z" fill="{SKIN_D}"/>'
            f'<ellipse cx="41" cy="106" rx="9.5" ry="12.5" fill="{SKIN}" stroke="{SKIN_D}" stroke-width="1.8"/>'
            f'<ellipse cx="159" cy="106" rx="9.5" ry="12.5" fill="{SKIN}" stroke="{SKIN_D}" stroke-width="1.8"/>'
            f'<ellipse cx="100" cy="103" rx="59" ry="56" fill="{SKIN}" stroke="{SKIN_D}" stroke-width="1.8"/>'
            # волосы: чёлка
            f'<path d="M43 98 Q42 58 100 54 Q158 58 157 98 Q150 80 136 84 Q132 72 118 80 Q110 68 100 78 Q90 68 80 80 Q68 72 62 86 Q50 82 43 98Z" fill="{HAIR}"/>'
            f'<path d="M70 70 Q88 62 104 64" stroke="{HAIR_L}" stroke-width="3" fill="none" stroke-linecap="round" opacity=".8"/>'
            f'<path d="M45 92 q-4 14 1 24 M155 92 q4 14 -1 24" stroke="{HAIR}" stroke-width="7" fill="none" stroke-linecap="round"/>'
            # шапочка-тюбетейка
            f'<path d="M50 72 Q52 30 100 28 Q148 30 150 72 Q100 60 50 72Z" fill="{p["cap"]}" stroke="{LINE}" stroke-width="2" stroke-linejoin="round"/>'
            f'<path d="M52 68 Q100 56 148 68" stroke="{p["cap_trim"]}" stroke-width="4" fill="none"/>'
            + "".join(f'<path d="M{x} {49 - abs(x-100)*0.07:.1f} l4 -5 4 5 -4 5z" fill="{p["cap_trim"]}"/>' for x in range(62, 136, 14))
            + f'<path d="M100 28 V58 M74 33 Q86 44 88 60 M126 33 Q114 44 112 60" stroke="{p["cap_trim"]}" stroke-width="1.6" fill="none" opacity=".55"/>'
            + _face(u, 100, 108, mood))
    extra = _book(100, 206, p["trim"]) if book else ""
    g = body + head + extra + la + ra
    return f'<svg class="char" viewBox="0 0 200 300" width="{w}" xmlns="http://www.w3.org/2000/svg">{g}</svg>'

def maryam(w=150, left="wave", right="down", mood="smile", book=False, pal='ru'):
    p = PAL[pal] if isinstance(pal, str) else pal
    u = next(_ids)
    if book: left, right = "hold", "hold"
    la = _arm(-1, left, p["dress"], p["dress_trim"], 66, 192, u)
    ra = _arm(1, right, p["dress"], p["dress_trim"], 134, 192, u)
    flowers = "".join(f'<g transform="translate({x} {y})">' + "".join(f'<circle cx="{4*dx}" cy="{4*dy}" r="3" fill="#FFFDF7"/>' for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]) +
                      f'<circle r="2.2" fill="{p["dress_trim"]}"/></g>' for x, y in [(78, 226), (122, 226), (100, 242), (70, 252), (130, 252)])
    body = (f'<ellipse cx="100" cy="291" rx="54" ry="6" fill="#4A3028" opacity=".12"/>'
            f'<path d="M76 280 q-13 0 -13 7 q0 5 15 5 h13 q5 0 5 -6z M124 280 q13 0 13 7 q0 5 -15 5 h-13 q-5 0 -5 -6z" fill="#7A4A3E"/>'
            # платье
            f'<path d="M72 172 Q100 162 128 172 L154 280 Q100 292 46 280Z" fill="{p['dress']}" stroke="{LINE}" stroke-width="2" stroke-linejoin="round"/>'
            f'<path d="M88 182 Q100 196 112 182" stroke="{p["dress_trim"]}" stroke-width="3" fill="none" stroke-linecap="round"/>'
            + flowers +
            f'<path d="M50 268 Q100 282 150 268" stroke="{p["dress_trim"]}" stroke-width="5" fill="none" stroke-linecap="round"/>'
            + _stars_band(58, 144, 278, "#FFFDF7"))
    scarf_back = (f'<path d="M100 30 Q166 32 168 112 Q170 170 140 196 Q100 212 60 196 Q30 170 32 112 Q34 32 100 30Z" fill="{p['scarf']}" stroke="{LINE}" stroke-width="2" stroke-linejoin="round" stroke-opacity=".6"/>'
                  f'<path d="M48 156 Q60 184 84 196 M152 156 Q140 184 116 196" stroke="{p["scarf_d"]}" stroke-width="2.5" fill="none" stroke-linecap="round"/>'
                  f'<path d="M60 186 Q100 204 140 186" stroke="{p["scarf_trim"]}" stroke-width="3" fill="none" stroke-dasharray="1 6" stroke-linecap="round"/>')
    face = (f'<ellipse cx="100" cy="112" rx="47" ry="48" fill="{SKIN}" stroke="{SKIN_D}" stroke-width="1.6"/>'
            # передний край платка
            f'<path d="M50 108 Q50 52 100 50 Q150 52 150 108 Q146 74 100 72 Q54 74 50 108Z" fill="{p['scarf']}" stroke="{LINE}" stroke-width="1.6" stroke-opacity=".6"/>'
            f'<path d="M56 96 Q60 66 100 64 Q140 66 144 96" stroke="{p["scarf_trim"]}" stroke-width="2.2" fill="none" stroke-dasharray="2 5" stroke-linecap="round"/>'
            # брошка-цветок
            f'<g transform="translate(140 80)">' + "".join(f'<circle cx="{5*dx}" cy="{5*dy}" r="4.2" fill="{p["pin"]}"/>' for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]) +
            f'<circle r="3.4" fill="#FFFDF7"/></g>'
            + _face(u, 100, 116, mood, lashes=True))
    extra = _book(100, 222, p["dress_trim"]) if book else ""
    g = body + scarf_back + face + extra + la + ra
    return f'<svg class="char" viewBox="0 0 200 300" width="{w}" xmlns="http://www.w3.org/2000/svg">{g}</svg>'
