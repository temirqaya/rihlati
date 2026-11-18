"""Картинки шагов абдеста: Юсуф (adam) и Зейнеб (maryam) из chars4 у крана с водой.
Свои рисунки (не копия стоков): персонаж в полный рост, кран справа, струя и брызги."""
import re
import chars4 as C

_orig_arm = C._arm
def _arm(side, pose, sleeve, cuff, x0, y0, u):
    if not isinstance(pose, tuple):
        return _orig_arm(side, pose, sleeve, cuff, x0, y0, u)
    hx, hy = pose
    mx, my = (x0 + hx) / 2, (y0 + hy) / 2
    cx, cy = mx + side * 14, my + 18          # локоть чуть наружу и вниз
    d = f"M{x0} {y0} Q{cx:.0f} {cy:.0f} {hx} {hy}"
    ux, uy = hx - (hx - cx) * 0.18, hy - (hy - cy) * 0.18
    return (f'<path d="{d}" stroke="{C.LINE}" stroke-width="23" fill="none" stroke-linecap="round" opacity=".28"/>'
            f'<path d="{d}" stroke="{sleeve}" stroke-width="19.5" fill="none" stroke-linecap="round"/>'
            f'<circle cx="{ux:.1f}" cy="{uy:.1f}" r="10.5" fill="{cuff}"/>'
            f'<ellipse cx="{hx}" cy="{hy}" rx="10" ry="11" fill="{C.SKIN}" stroke="{C.SKIN_D}" stroke-width="1.6"/>')
C._arm = _arm

WATER, WATER_D = '#8FC9F0', '#4F9FD8'

def splash(x, y, s=1.0):
    pts = [(-14, -6), (-9, -14), (0, -17), (9, -14), (14, -6), (-18, 2), (18, 2)]
    return ''.join(f'<ellipse cx="{x + dx*s:.1f}" cy="{y + dy*s:.1f}" rx="{3*s:.1f}" ry="{4.2*s:.1f}" transform="rotate({dx*3} {x + dx*s:.1f} {y + dy*s:.1f})" fill="{WATER}" stroke="{WATER_D}" stroke-width="1"/>' for dx, dy in pts)

def drops(pts):
    return ''.join(f'<path d="M{x} {y-6} q4 6 0 9 q-4 -3 0 -9z" fill="{WATER}" stroke="{WATER_D}" stroke-width=".9"/>' for x, y in pts)

def tap(y_end, stream=True):
    t = ('<rect x="262" y="0" width="12" height="300" fill="#D9DEE6"/>'
         '<path d="M262 132 H226 q-10 0 -10 10 v8" stroke="#B9C2CF" stroke-width="11" fill="none" stroke-linecap="round"/>'
         '<rect x="236" y="118" width="18" height="8" rx="3" fill="#B9C2CF"/><rect x="242" y="110" width="6" height="10" fill="#B9C2CF"/>')
    if stream:
        t += (f'<path d="M213 154 C211 {(154+y_end)/2:.0f} 219 {(154+y_end)/2:.0f} 215 {y_end}" stroke="{WATER_D}" stroke-width="11" fill="none" stroke-linecap="round" opacity=".35"/>'
              f'<path d="M213 154 C211 {(154+y_end)/2:.0f} 219 {(154+y_end)/2:.0f} 215 {y_end}" stroke="{WATER}" stroke-width="8" fill="none" stroke-linecap="round"/>'
              f'<path d="M212 160 V{y_end-6}" stroke="#fff" stroke-width="2" opacity=".7" stroke-linecap="round"/>')
    return t

def inner(svg):
    return re.sub(r'^<svg[^>]*>|</svg>$', '', svg)

def scene(who, la, ra, mood='smile', y_end=196, extra='', bg='#EAF4F1', stream=True):
    ch = (C.adam if who == 'a' else C.maryam)(200, left=la, right=ra, mood=mood)
    return (f'<svg viewBox="0 0 300 300" xmlns="http://www.w3.org/2000/svg" class="wu">'
            f'<rect x="0" y="0" width="300" height="300" rx="28" fill="{bg}"/>' + tap(y_end, stream) +
            f'<g transform="translate(0 4)">{inner(ch)}</g>' + extra + '</svg>')

# координаты плеч: Юсуф 68/132,176; Зейнеб 66/134,192
def steps(who):
    mo = 0 if who == 'a' else 10            # у Зейнеб лицо и плечи ниже
    return {
        'hands':  scene(who, (186, 198), (208, 192), 'smile', 190, splash(204, 198, 1.3)),
        'mouth':  scene(who, 'down', (112, 140 + mo), 'smile', 286, drops([(122, 132 + mo), (126, 146 + mo), (104, 150 + mo)]) + splash(215, 288, 1.1)),
        'nose':   scene(who, 'down', (108, 124 + mo), 'smile', 286, drops([(118, 116 + mo), (96, 118 + mo)]) + splash(215, 288, 1.1)),
        'face':   scene(who, (74, 118 + mo), (126, 118 + mo), 'closed', 286, drops([(64, 104 + mo), (136, 104 + mo), (100, 92 + mo), (84, 140 + mo), (118, 140 + mo)]) + splash(215, 288, 1.1)),
        'arms':   scene(who, (170, 210), (214, 196), 'smile', 192, splash(196, 204, 1.2) + drops([(178, 214), (160, 200)])),
        'head':   scene(who, 'down', (96, 76 + mo), 'smile', 190, drops([(84, 66 + mo), (116, 60 + mo)]), stream=False),
        'ears':   scene(who, (44, 108 + mo), (156, 108 + mo), 'smile', 190, drops([(34, 100 + mo), (166, 100 + mo)]), stream=False),
        'neck':   scene(who, (86, 158 + mo), (114, 158 + mo), 'smile', 190, drops([(100, 150 + mo)]), stream=False),
    }

HEART = '<path d="M0 6 C-10 -2 -12 -12 -5 -14 C-1 -15 0 -11 0 -9 C0 -11 1 -15 5 -14 C12 -12 10 -2 0 6Z" fill="#E9A0B8" stroke="#B43F55" stroke-width="1.6"/>'
def finger(x, y):
    return f'<path d="M{x} {y-6} v-16" stroke="{C.SKIN_D}" stroke-width="8" stroke-linecap="round"/><path d="M{x} {y-6} v-16" stroke="{C.SKIN}" stroke-width="5.5" stroke-linecap="round"/>'

def feet_scene(who):
    sk, skd = C.SKIN, C.SKIN_D
    leg, cuf = ('#7FA0D6', '#F2C863') if who == 'a' else ('#A996D8', '#F6C9D6')
    def foot(x):
        return (f'<rect x="{x-17}" y="96" width="34" height="112" rx="14" fill="{leg}" stroke="{C.LINE}" stroke-width="1.6" stroke-opacity=".5"/>'
                f'<rect x="{x-19}" y="186" width="38" height="14" rx="6" fill="{cuf}"/>'
                f'<path d="M{x-14} 200 Q{x-20} 238 {x-4} 242 L{x+48} 242 Q{x+64} 240 {x+62} 228 Q{x+60} 216 {x+34} 214 Q{x+18} 210 {x+14} 200 Z" fill="{sk}" stroke="{skd}" stroke-width="2"/>'
                + ''.join(f'<ellipse cx="{x + 40 + i*6}" cy="{219 + i*2.2:.1f}" rx="3.6" ry="4.2" fill="{sk}" stroke="{skd}" stroke-width="1.3"/>' for i in range(4)))
    return (f'<svg viewBox="0 0 300 300" xmlns="http://www.w3.org/2000/svg" class="wu"><rect width="300" height="300" rx="28" fill="#EAF4F1"/>'
            + tap(222) + '<rect x="30" y="242" width="240" height="14" rx="7" fill="#D6E6EC"/>'
            + foot(84) + foot(164) + splash(214, 224, 1.4) + drops([(150, 252), (200, 250), (238, 248), (120, 250)])
            + '</svg>')

def more(who):
    mo = 0 if who == 'a' else 10
    return {
        'niyya':   scene(who, (90, 196 + mo), (110, 196 + mo), 'smile', 190, f'<g transform="translate(150 70) scale(1.6)">{HEART}</g>' + drops([]), stream=False),
        'shahada': scene(who, 'down', (150, 128 + mo), 'smile', 190, finger(150, 128 + mo), stream=False),
        'feet':    feet_scene(who),
    }
