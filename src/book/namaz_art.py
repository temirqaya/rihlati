"""Позы намаза: Юсуф и Зейнеб (стиль chars4). Свои рисунки, не копия стоков.
Стоя — вид спереди; руку, саджда, сидение — вид сбоку (лицом вправо)."""
import re
import chars4 as C
import wudu_art  # кортежные руки (hx, hy)

P = C.PAL['ru']
L = C.LINE
def inner(svg): return re.sub(r'^<svg[^>]*>|</svg>$', '', svg)

BG = '#FFF4D9'
def frame(body, front=False):
    rug = ('<path d="M24 262 H276 L268 276 H32Z" fill="#8DBB6A" stroke="#5E8E44" stroke-width="1.5"/>'
           '<path d="M40 268 H260" stroke="#E9C46A" stroke-width="2" stroke-dasharray="6 4"/>'
           + ''.join(f'<path d="M{x} 276 v6" stroke="#5E8E44" stroke-width="2" stroke-linecap="round"/>' for x in range(36, 268, 9)))
    if front:
        rug = ('<path d="M70 230 H230 L262 284 H38Z" fill="#8DBB6A" stroke="#5E8E44" stroke-width="1.5"/>'
               '<path d="M82 238 H218 L244 276 H56Z" fill="none" stroke="#E9C46A" stroke-width="2" stroke-dasharray="6 4"/>'
               '<path d="M134 274 V252 Q150 236 166 252 V274" fill="none" stroke="#E9C46A" stroke-width="2"/>'
               + ''.join(f'<path d="M{x} 284 v6" stroke="#5E8E44" stroke-width="2" stroke-linecap="round"/>' for x in range(42, 262, 9)))
    return (f'<svg viewBox="0 0 300 300" xmlns="http://www.w3.org/2000/svg" class="pz">'
            f'<rect width="300" height="300" rx="28" fill="{BG}"/>{rug}{body}</svg>')

# ---------------- вид спереди (стоя)
def front(who, la, ra, face_dx=0):
    old = C._face
    if face_dx:
        C._face = lambda u, cx, cy, mood, lashes=False: old(u, cx + face_dx, cy, mood, lashes)
    try:
        ch = (C.adam if who == 'a' else C.maryam)(200, left=la, right=ra, mood='closed')
    finally:
        C._face = old
    return f'<g transform="translate(66 6) scale(.9)">{inner(ch)}</g>'

def takbir(who):
    if who == 'a': return frame(front('a', (46, 104), (154, 104)), True)
    return frame(front('m', (58, 168), (142, 168)), True)

def qiyam(who):
    if who == 'a': return frame(front('a', (96, 214), (106, 208)), True)
    return frame(front('m', (96, 206), (106, 200)), True)

def itidal(who):
    return frame(front(who, 'down', 'down'), True)

# ---------------- вид сбоку
def head_side(who, mood='closed'):
    """Голова в профиль, центр (0,0), лицо вправо."""
    sk, skd = C.SKIN, C.SKIN_D
    eye = ('<path d="M22 2 q8 7 16 0" stroke="#2F2420" stroke-width="2.8" fill="none" stroke-linecap="round"/>' if mood == 'closed'
           else '<ellipse cx="30" cy="2" rx="7" ry="9.5" fill="#2F2420"/><circle cx="32" cy="-2" r="2.8" fill="#fff"/>')
    face = (eye + '<ellipse cx="34" cy="20" rx="9" ry="6" fill="#F08F8A" opacity=".35"/>'
            '<path d="M38 30 q6 4 11 -1" stroke="#A24642" stroke-width="2.6" fill="none" stroke-linecap="round"/>'
            '<path d="M18 -16 q8 -4 16 0" stroke="#3B2A22" stroke-width="2.4" fill="none" stroke-linecap="round" opacity=".55"/>')
    if who == 'a':
        return (f'<ellipse cx="0" cy="0" rx="55" ry="53" fill="{sk}" stroke="{skd}" stroke-width="1.8"/>'
                f'<path d="M54 8 q8 4 2 10" fill="{sk}" stroke="{skd}" stroke-width="1.8"/>'
                f'<path d="M-55 4 Q-58 -40 -10 -48 Q30 -52 44 -26 Q30 -34 16 -26 Q4 -36 -8 -24 Q-18 -10 -30 -2 Q-36 14 -44 30 Q-56 22 -55 4Z" fill="{C.HAIR}"/>'
                f'<ellipse cx="-12" cy="6" rx="10" ry="13" fill="{sk}" stroke="{skd}" stroke-width="1.8"/>'
                f'<path d="M-50 -24 Q-44 -66 2 -66 Q44 -64 48 -30 Q0 -40 -50 -24Z" fill="{P["cap"]}" stroke="{L}" stroke-width="2" stroke-linejoin="round"/>'
                f'<path d="M-48 -27 Q0 -42 47 -33" stroke="{P["cap_trim"]}" stroke-width="4" fill="none"/>'
                + ''.join(f'<path d="M{x} {-52 + abs(x)*.06:.1f} l4 -5 4 5 -4 5z" fill="{P["cap_trim"]}"/>' for x in (-30, -14, 2, 18))
                + face)
    return (f'<path d="M6 -64 Q-58 -66 -64 -4 Q-66 44 -40 66 Q-6 80 30 60 Q58 46 56 6 Q54 -56 6 -64Z" fill="{P["scarf"]}" stroke="{L}" stroke-width="2" stroke-opacity=".6"/>'
            f'<ellipse cx="14" cy="6" rx="42" ry="44" fill="{sk}" stroke="{skd}" stroke-width="1.6"/>'
            f'<path d="M-22 40 Q-30 -40 14 -42 Q44 -42 54 -10 Q50 -54 8 -56 Q-44 -54 -30 30Z" fill="{P["scarf"]}" stroke="{L}" stroke-width="1.6" stroke-opacity=".6"/>'
            f'<path d="M-22 30 Q-26 -36 12 -48 Q40 -50 50 -24" stroke="{P["scarf_trim"]}" stroke-width="2.2" fill="none" stroke-dasharray="2 5" stroke-linecap="round"/>'
            f'<path d="M-40 52 Q-10 72 28 58" stroke="{P["scarf_d"]}" stroke-width="2.5" fill="none" stroke-linecap="round"/>'
            + face)

def limb(d, col, w=19.5):
    return (f'<path d="{d}" stroke="{L}" stroke-width="{w+3.5}" fill="none" stroke-linecap="round" stroke-linejoin="round" opacity=".28"/>'
            f'<path d="{d}" stroke="{col}" stroke-width="{w}" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
def hand(x, y, r=0):
    return f'<ellipse cx="{x}" cy="{y}" rx="11" ry="8" transform="rotate({r} {x} {y})" fill="{C.SKIN}" stroke="{C.SKIN_D}" stroke-width="1.6"/>'
def foot(x, y, r=0, col='#5A3E33'):
    return f'<ellipse cx="{x}" cy="{y}" rx="16" ry="7" transform="rotate({r} {x} {y})" fill="{col}"/>'

def cloth(who):
    return (P['tunic'], P['trim'], P['pants']) if who == 'a' else (P['dress'], P['dress_trim'], P['dress'])

def ruku(who):
    c, t, pt = cloth(who)
    legs = limb('M104 196 L104 252', pt, 26) + foot(118, 256, 0, '#5A3E33' if who == 'a' else '#7A4A3E')
    if who == 'a':
        torso = (f'<path d="M80 150 Q82 132 104 132 L186 136 Q204 146 196 166 L130 172 L132 214 Q104 222 78 212Z" fill="{c}" stroke="{L}" stroke-width="2" stroke-linejoin="round"/>'
                 f'<path d="M80 206 Q104 216 130 208" stroke="{t}" stroke-width="4" fill="none"/>')
    else:
        torso = (f'<path d="M80 150 Q82 132 104 132 L186 136 Q204 146 196 166 L132 172 L136 252 Q104 262 74 252Z" fill="{c}" stroke="{L}" stroke-width="2" stroke-linejoin="round"/>'
                 f'<path d="M76 244 Q104 256 134 246" stroke="{t}" stroke-width="5" fill="none" stroke-linecap="round"/>')
    arm = limb('M178 150 Q160 186 128 204', c) + f'<circle cx="136" cy="199" r="10" fill="{t}"/>' + hand(122, 208, -30)
    head = f'<g transform="translate(236 168) rotate(62) scale(.82)">{head_side(who)}</g>'
    return frame(legs + torso + head + arm)

def sajda(who):
    c, t, pt = cloth(who)
    sh = '#5A3E33' if who == 'a' else '#7A4A3E'
    legs = (limb('M70 252 L118 252', pt, 24) + limb('M118 252 L104 206', pt, 26) + foot(58, 250, -70, sh))
    torso = (f'<path d="M84 210 Q88 186 112 186 L184 214 Q196 226 186 240 L156 246 Q120 246 96 236Z" fill="{c}" stroke="{L}" stroke-width="2" stroke-linejoin="round"/>')
    arm = limb('M176 220 Q186 238 196 252', c) + f'<circle cx="192" cy="245" r="10" fill="{t}"/>' + hand(204, 256, 0)
    head = f'<g transform="translate(226 220) rotate(96) scale(.78)">{head_side(who)}</g>'
    return frame(legs + torso + head + arm)

def sit(who, finger=False):
    c, t, pt = cloth(who)
    sh = '#5A3E33' if who == 'a' else '#7A4A3E'
    legs = foot(92, 256, 0, sh) + limb('M100 250 L176 250', pt, 28)
    if who == 'a':
        torso = (f'<path d="M98 252 Q86 232 100 200 L104 158 Q130 146 152 160 L154 206 Q190 226 184 254Z" fill="{c}" stroke="{L}" stroke-width="2" stroke-linejoin="round"/>'
                 f'<path d="M96 246 Q140 262 182 250" stroke="{t}" stroke-width="4" fill="none"/>')
    else:
        torso = (f'<path d="M92 260 Q80 232 98 200 L104 160 Q130 148 152 162 L156 206 Q196 226 192 262Z" fill="{c}" stroke="{L}" stroke-width="2" stroke-linejoin="round"/>'
                 f'<path d="M92 256 Q140 270 190 258" stroke="{t}" stroke-width="5" fill="none" stroke-linecap="round"/>')
    arm = limb('M136 170 Q150 208 170 226', c) + f'<circle cx="164" cy="220" r="10" fill="{t}"/>' + hand(178, 232, 10)
    if finger:
        arm += '<path d="M186 230 l17 -3" stroke="#E4B898" stroke-width="8" stroke-linecap="round"/><path d="M186 230 l17 -3" stroke="#F6D9C3" stroke-width="5" stroke-linecap="round"/>'
    head = f'<g transform="translate(140 {104 if who == "a" else 108}) rotate(10) scale(.9)">{head_side(who)}</g>'
    return frame(legs + torso + head + arm)

def salam(who, side=1):
    """Вид спереди, сидя. side=-1: поворот к своему правому плечу (для зрителя — влево)."""
    ch = front(who, (84, 232), (116, 232), face_dx=side * 22)
    k = P['pants'] if who == 'a' else P['dress']
    knees = (f'<path d="M84 238 Q60 238 56 262 Q60 280 100 280 L200 280 Q240 280 244 262 Q240 238 216 238Z" fill="{k}" stroke="{L}" stroke-width="2"/>')
    clip = f'<clipPath id="cl{who}{side}"><rect x="0" y="0" width="300" height="248"/></clipPath>'
    arr = (f'<path d="M{150 + side*70} 70 q{side*18} 8 {side*16} 30" stroke="#C9A15B" stroke-width="4" fill="none" stroke-linecap="round"/>'
           f'<path d="M{150 + side*86} 96 l{side*2} 12 l{side*-10} -6z" fill="#C9A15B"/>')
    return frame(f'<defs>{clip}</defs>' + knees + f'<g clip-path="url(#cl{who}{side})" transform="translate(0 30)">{ch}</g>' + arr, True)

ORDER = [('takbir', takbir), ('qiyam', qiyam), ('ruku', ruku), ('itidal', itidal), ('sajda', sajda),
         ('sit', sit), ('tash', lambda w: sit(w, True)), ('salamR', lambda w: salam(w, -1)), ('salamL', lambda w: salam(w, 1))]
def all_poses(who): return {k: f(who) for k, f in ORDER}
