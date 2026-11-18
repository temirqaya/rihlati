# Эталонные персонажи «Моё путешествие к чтению Священного Корана» — версия 2.
# Палитра: шоколад #5C342E, крем #F4EBE2, индиго #3E5180 + золото, пыльная роза.
# Зейнеб и Юсуф рисуются одним и тем же кодом на всех страницах (одинаковые лица,
# пропорции, одежда). Меняются только поза рук и выражение лица.
import itertools

_ids = itertools.count()

LINE = "#6B4238"        # мягкий контур
SKIN, SKIN_D = "#F6DCC6", "#E8BFA2"
IRIS = "#5C342E"

def _defs(u, extra=""):
    return (f'<defs>'
            f'<radialGradient id="sk{u}" cx=".45" cy=".4" r=".7"><stop offset="0" stop-color="#FBE8D8"/><stop offset="1" stop-color="{SKIN}"/></radialGradient>'
            f'<radialGradient id="bl{u}"><stop offset="0" stop-color="#E9928A" stop-opacity=".75"/><stop offset="1" stop-color="#E9928A" stop-opacity="0"/></radialGradient>'
            f'{extra}</defs>')

def _eye(x, y, lashes, mood_closed=False):
    if mood_closed:
        return f'<path d="M{x-8} {y+1} q8 -8 16 0" stroke="{IRIS}" stroke-width="3" fill="none" stroke-linecap="round"/>'
    s = (f'<ellipse cx="{x}" cy="{y}" rx="8.5" ry="10.5" fill="#fff"/>'
         f'<ellipse cx="{x}" cy="{y+1.5}" rx="7" ry="8.8" fill="{IRIS}"/>'
         f'<ellipse cx="{x}" cy="{y+3}" rx="4.2" ry="5.2" fill="#2E1A16"/>'
         f'<ellipse cx="{x+2.6}" cy="{y-2.6}" rx="2.8" ry="3.2" fill="#fff"/>'
         f'<circle cx="{x-2.6}" cy="{y+5.2}" r="1.3" fill="#fff" opacity=".85"/>'
         f'<path d="M{x-9} {y-6} q9 -8 18 0" stroke="{IRIS}" stroke-width="2.6" fill="none" stroke-linecap="round"/>')
    if lashes:
        side = 1 if x > 100 else -1
        s += (f'<path d="M{x+side*8} {y-5} l{side*5} -4 M{x+side*9} {y-1} l{side*5.5} -1.5" '
              f'stroke="{IRIS}" stroke-width="2.2" stroke-linecap="round"/>')
    return s

def _face(u, cx, cy, mood, lashes):
    left = _eye(cx-19, cy, lashes, mood_closed=(mood == "wink"))
    right = _eye(cx+19, cy, lashes)
    brows = (f'<path d="M{cx-27} {cy-17} q8 -5 15 -1" stroke="{IRIS}" stroke-width="2.4" fill="none" stroke-linecap="round" opacity=".75"/>'
             f'<path d="M{cx+12} {cy-18} q7 -4 15 1" stroke="{IRIS}" stroke-width="2.4" fill="none" stroke-linecap="round" opacity=".75"/>')
    nose = f'<path d="M{cx-2.5} {cy+12} q2.5 2.5 5 0" stroke="{SKIN_D}" stroke-width="2.4" fill="none" stroke-linecap="round"/>'
    if mood == "sad":
        brows = (f'<path d="M{cx-27} {cy-13} q8 -6 15 -9" stroke="{IRIS}" stroke-width="2.4" fill="none" stroke-linecap="round" opacity=".75"/>'
                 f'<path d="M{cx+12} {cy-22} q7 3 15 9" stroke="{IRIS}" stroke-width="2.4" fill="none" stroke-linecap="round" opacity=".75"/>')
        mouth = (f'<path d="M{cx-8} {cy+25} q8 -7 16 0" stroke="#9C3F3A" stroke-width="3" fill="none" stroke-linecap="round"/>'
                 f'<path d="M{cx+24} {cy+8} q-3 6 0 9 q3 -3 0 -9z" fill="#8FC3EC"/>')
    elif mood == "open":
        mouth = (f'<path d="M{cx-9} {cy+19} q9 2 18 0 q-2 12 -9 12 q-7 0 -9 -12z" fill="#9C3F3A"/>'
                 f'<path d="M{cx-5} {cy+27} q5 -4 10 0 q-5 4 -10 0z" fill="#E98A86"/>')
    else:
        mouth = f'<path d="M{cx-9} {cy+20} q9 9 18 0" stroke="#9C3F3A" stroke-width="3" fill="none" stroke-linecap="round"/>'
    blush = (f'<ellipse cx="{cx-31}" cy="{cy+14}" rx="10" ry="6.5" fill="url(#bl{u})"/>'
             f'<ellipse cx="{cx+31}" cy="{cy+14}" rx="10" ry="6.5" fill="url(#bl{u})"/>')
    return brows + left + right + blush + nose + mouth

def _arm(side, pose, sleeve, sleeve_d, cuff, x0, y0, u):
    s = side
    if pose == "wave":
        d, hx, hy = f"M{x0} {y0} q{s*24} -2 {s*30} -42", x0 + s*31, y0 - 50
    elif pose == "point":
        d, hx, hy = f"M{x0} {y0} q{s*22} 4 {s*40} -8", x0 + s*46, y0 - 10
    elif pose == "hold":
        d, hx, hy = f"M{x0} {y0} q{s*10} 24 {-s*8} 36", x0 - s*12, y0 + 40
    else:
        d, hx, hy = f"M{x0} {y0} q{s*15} 20 {s*12} 44", x0 + s*12, y0 + 50
    return (f'<path d="{d}" stroke="{LINE}" stroke-width="23" fill="none" stroke-linecap="round" opacity=".55"/>'
            f'<path d="{d}" stroke="{sleeve}" stroke-width="19" fill="none" stroke-linecap="round"/>'
            f'<path d="{d}" stroke="{sleeve_d}" stroke-width="6" fill="none" stroke-linecap="round" opacity=".35" transform="translate({-s*3} 2)"/>'
            f'<circle cx="{hx - (hx-x0)*0.08:.1f}" cy="{hy - (hy-y0)*0.08:.1f}" r="10.5" fill="{cuff}"/>'
            f'<circle cx="{hx}" cy="{hy}" r="9.5" fill="url(#sk{u})" stroke="{SKIN_D}" stroke-width="1.8"/>')

def _book(cx, cy, u):
    return (f'<g transform="translate({cx} {cy})">'
            f'<path d="M-36 -16 Q-18 -23 0 -14 Q18 -23 36 -16 L36 19 Q18 12 0 21 Q-18 12 -36 19Z" fill="#3E5180" stroke="#2C3A60" stroke-width="2.5" stroke-linejoin="round"/>'
            f'<path d="M-32 -13 Q-16 -18 -2 -11 L-2 17 Q-16 10 -32 15Z M32 -13 Q16 -18 2 -11 L2 17 Q16 10 32 15Z" fill="#F4EBE2"/>'
            f'<path d="M-26 -6 L-8 -3 M-26 1 L-8 4 M-26 8 L-12 10 M8 -3 L26 -6 M8 4 L26 1 M12 10 L26 8" stroke="#C9A15B" stroke-width="1.8" stroke-linecap="round"/>'
            f'<circle cx="-27" cy="17" r="9" fill="url(#sk{u})" stroke="{SKIN_D}" stroke-width="1.5"/><circle cx="27" cy="17" r="9" fill="url(#sk{u})" stroke="{SKIN_D}" stroke-width="1.5"/></g>')


def adam(w=150, left="down", right="wave", mood="smile", book=False):
    u = next(_ids)
    defs = _defs(u, f'<linearGradient id="rb{u}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFBF5"/><stop offset="1" stop-color="#EFE3D3"/></linearGradient>'
                    f'<linearGradient id="kf{u}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#F1E7DA"/></linearGradient>')
    left_arm = _arm(-1, "hold" if book else left, "#FBF4EA", "#C9B39C", "#3E5180", 66, 172, u)
    right_arm = _arm(1, "hold" if book else right, "#FBF4EA", "#C9B39C", "#3E5180", 134, 172, u)
    g = (
        f'<ellipse cx="100" cy="290" rx="52" ry="6" fill="#5C342E" opacity=".12"/>'
        f'<path d="M72 276 q-12 0 -12 9 q0 5 14 5 h12 q4 0 4 -6 z" fill="#5C342E"/>'
        f'<path d="M128 276 q12 0 12 9 q0 5 -14 5 h-12 q-4 0 -4 -6 z" fill="#5C342E"/>'
        + left_arm + right_arm +
        # тауб
        f'<path d="M68 162 Q100 150 132 162 L148 276 Q100 288 52 276 Z" fill="url(#rb{u})" stroke="{LINE}" stroke-width="2.2" stroke-linejoin="round"/>'
        f'<path d="M80 200 Q78 240 72 270 M120 200 Q122 240 128 270" stroke="#E2D2BF" stroke-width="2.5" fill="none" stroke-linecap="round"/>'
        # жилетка-садри шоколадного цвета
        f'<path d="M70 166 Q84 158 92 160 L96 232 Q80 236 62 232 Z" fill="#5C342E"/>'
        f'<path d="M130 166 Q116 158 108 160 L104 232 Q120 236 138 232 Z" fill="#5C342E"/>'
        f'<path d="M66 224 Q80 228 95 225 M134 224 Q120 228 105 225" stroke="#C9A15B" stroke-width="2" fill="none" stroke-dasharray="1 4" stroke-linecap="round"/>'
        # ворот и пуговицы
        f'<path d="M100 162 L100 214" stroke="#3E5180" stroke-width="3" stroke-linecap="round"/>'
        f'<circle cx="100" cy="180" r="2.8" fill="#C9A15B"/><circle cx="100" cy="194" r="2.8" fill="#C9A15B"/><circle cx="100" cy="208" r="2.8" fill="#C9A15B"/>'
        f'<path d="M87 160 Q100 170 113 160" stroke="#3E5180" stroke-width="5" fill="none" stroke-linecap="round"/>'
        f'<path d="M56 266 Q100 279 144 266" stroke="#3E5180" stroke-width="4" fill="none" stroke-linecap="round"/>'
        # шея, уши, голова
        f'<path d="M90 140 h20 v22 q-10 6 -20 0z" fill="{SKIN_D}"/>'
        f'<ellipse cx="42" cy="104" rx="10" ry="13" fill="url(#sk{u})" stroke="{SKIN_D}" stroke-width="2"/>'
        f'<ellipse cx="158" cy="104" rx="10" ry="13" fill="url(#sk{u})" stroke="{SKIN_D}" stroke-width="2"/>'
        f'<ellipse cx="100" cy="100" rx="58" ry="55" fill="url(#sk{u})" stroke="{SKIN_D}" stroke-width="2"/>'
        # волосы: чёлка прядями
        f'<path d="M44 92 Q46 58 100 54 Q154 58 156 92 Q148 80 138 84 Q130 72 118 80 Q108 70 96 80 Q86 70 76 82 Q64 74 58 86 Q50 82 44 92Z" fill="#5C342E"/>'
        f'<path d="M64 74 Q72 66 84 66 M110 64 Q124 64 134 72" stroke="#7A4A3E" stroke-width="2.5" fill="none" stroke-linecap="round"/>'
        f'<path d="M46 90 q-4 14 2 22 M154 90 q4 14 -2 22" stroke="#5C342E" stroke-width="7" fill="none" stroke-linecap="round"/>'
        # куфи с вышивкой
        f'<path d="M48 72 Q50 26 100 24 Q150 26 152 72 Q100 58 48 72Z" fill="url(#kf{u})" stroke="{LINE}" stroke-width="2.2" stroke-linejoin="round"/>'
        f'<path d="M51 66 Q100 52 149 66" stroke="#3E5180" stroke-width="5" fill="none"/>'
        f'<path d="M56 63 l6 -5 l6 5 l6 -5 l6 5 l6 -5 l6 5 l6 -5 l6 5 l6 -5 l6 5 l6 -5 l6 5 l6 -5 l6 5" stroke="#F4EBE2" stroke-width="1.6" fill="none" transform="translate(0 -1)"/>'
        f'<path d="M64 44 Q100 32 136 44" stroke="#C9A15B" stroke-width="2.4" fill="none" stroke-dasharray="1.5 7" stroke-linecap="round"/>'
        f'<circle cx="100" cy="27" r="3.5" fill="#C9A15B"/>'
        + _face(u, 100, 104, mood, lashes=False)
    )
    if book:
        g += _book(100, 226, u)
    return f'<svg class="char" viewBox="0 0 200 300" width="{w}" xmlns="http://www.w3.org/2000/svg">{defs}{g}</svg>'


def maryam(w=150, left="wave", right="down", mood="smile", book=False):
    u = next(_ids)
    defs = _defs(u, f'<linearGradient id="hj{u}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7486BA"/><stop offset="1" stop-color="#53669B"/></linearGradient>'
                    f'<linearGradient id="dr{u}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#E7B8A8"/><stop offset="1" stop-color="#D59A88"/></linearGradient>')
    left_arm = _arm(-1, "hold" if book else left, "#DEA897", "#A86E5E", "#F4EBE2", 64, 188, u)
    right_arm = _arm(1, "hold" if book else right, "#DEA897", "#A86E5E", "#F4EBE2", 136, 188, u)
    g = (
        f'<ellipse cx="100" cy="290" rx="54" ry="6" fill="#5C342E" opacity=".12"/>'
        f'<path d="M74 278 q-12 0 -12 8 q0 5 14 5 h12 q4 0 4 -6 z" fill="#5C342E"/>'
        f'<path d="M126 278 q12 0 12 8 q0 5 -14 5 h-12 q-4 0 -4 -6 z" fill="#5C342E"/>'
        # платье
        f'<path d="M72 166 Q100 156 128 166 L152 278 Q100 290 48 278 Z" fill="url(#dr{u})" stroke="{LINE}" stroke-width="2.2" stroke-linejoin="round"/>'
        f'<path d="M84 210 Q80 246 74 274 M116 210 Q120 246 126 274" stroke="#C78775" stroke-width="2.4" fill="none" stroke-linecap="round" opacity=".7"/>'
        f'<path d="M52 262 Q100 276 148 262" stroke="#F4EBE2" stroke-width="7" fill="none" stroke-linecap="round"/>'
        f'<path d="M58 263 Q100 276 142 263" stroke="#C9A15B" stroke-width="2" fill="none" stroke-dasharray="1 5" stroke-linecap="round"/>'
        f'<g fill="#F4EBE2">' + "".join(f'<g transform="translate({x} {y})"><circle r="4.5"/><circle r="1.8" fill="#C9A15B"/></g>' for x, y in [(76, 238), (100, 243), (124, 238)]) + '</g>'
        # хиджаб: внешний слой
        f'<path d="M100 26 Q164 28 166 108 Q168 166 138 190 Q100 206 62 190 Q32 166 34 108 Q36 28 100 26Z" fill="url(#hj{u})" stroke="#3E5180" stroke-width="2.4" stroke-linejoin="round"/>'
        f'<path d="M48 150 Q60 178 82 190 M152 150 Q140 178 118 190" stroke="#3E5180" stroke-width="2.4" fill="none" stroke-linecap="round" opacity=".55"/>'
        f'<path d="M60 168 Q100 196 140 168" stroke="#8E9DCA" stroke-width="3" fill="none" stroke-linecap="round" opacity=".7"/>'
        # кремовая подшапочка и лицо
        f'<ellipse cx="100" cy="104" rx="52" ry="54" fill="#F4EBE2"/>'
        f'<ellipse cx="100" cy="110" rx="46" ry="47" fill="url(#sk{u})" stroke="{SKIN_D}" stroke-width="1.8"/>'
        f'<path d="M52 104 Q54 56 100 54 Q146 56 148 104 Q144 66 100 64 Q56 66 52 104Z" fill="#F4EBE2"/>'
        f'<path d="M56 98 Q60 62 100 60 Q140 62 144 98" stroke="#E2D2BF" stroke-width="2" fill="none"/>'
        # блик на хиджабе и брошь
        f'<path d="M58 54 Q76 38 98 36" stroke="#A3B0D8" stroke-width="5" fill="none" stroke-linecap="round" opacity=".7"/>'
        f'<g transform="translate(142 156)"><circle r="8" fill="#F4EBE2" stroke="#C9A15B" stroke-width="2"/><circle r="3.4" fill="#C9A15B"/></g>'
        + left_arm + right_arm
        + _face(u, 100, 110, mood, lashes=True)
    )
    if book:
        g += _book(100, 228, u)
    return f'<svg class="char" viewBox="0 0 200 300" width="{w}" xmlns="http://www.w3.org/2000/svg">{defs}{g}</svg>'
