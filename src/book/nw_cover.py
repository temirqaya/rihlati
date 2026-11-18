"""Иллюстрация обложки мира намаза: Юсуф и Зейнеб на ковриках в ду‘а, фонарики."""
import re
import chars4 as C

def inner(svg): return re.sub(r'^<svg[^>]*>|</svg>$', '', svg)

def rug(cx, base, col, col2):
    # коврик в лёгкой перспективе, с михрабом и бахромой
    w1, w2, h = 70, 92, 46
    pts = f"{cx-w1/2},{base-h} {cx+w1/2},{base-h} {cx+w2/2},{base} {cx-w2/2},{base}"
    inn = f"{cx-w1/2+7},{base-h+5} {cx+w1/2-7},{base-h+5} {cx+w2/2-9},{base-5} {cx-w2/2+9},{base-5}"
    mih = f'M{cx-14} {base-8} V{base-26} Q{cx} {base-44} {cx+14} {base-26} V{base-8}Z'
    fr = ''.join(f'<path d="M{cx - w2/2 + 4 + i*7.3:.1f} {base} v5" stroke="{col2}" stroke-width="2" stroke-linecap="round"/>' for i in range(12))
    return (f'<polygon points="{pts}" fill="{col}" stroke="#7A5A3A" stroke-opacity=".35" stroke-width="1.5"/>'
            f'<polygon points="{inn}" fill="none" stroke="{col2}" stroke-width="2.2" stroke-dasharray="5 3"/>'
            f'<path d="{mih}" fill="none" stroke="{col2}" stroke-width="2"/>' + fr)

def lantern(x, top, ln, s=1.0):
    y = top + ln
    return (f'<path d="M{x} {top} V{y}" stroke="#B8914A" stroke-width="1.4"/>'
            f'<g transform="translate({x} {y}) scale({s})">'
            f'<circle cx="0" cy="22" r="26" fill="#F6D98A" opacity=".28"/>'
            f'<path d="M-6 0 h12 l-2 6 h-8z" fill="#B8914A"/>'
            f'<path d="M-12 8 Q0 0 12 8 L14 30 Q0 40 -14 30Z" fill="#F2C863" stroke="#9A7330" stroke-width="1.6"/>'
            f'<path d="M-7 12 V28 M0 9 V33 M7 12 V28" stroke="#9A7330" stroke-width="1.1" opacity=".7"/>'
            f'<path d="M-4 33 h8 l-4 7z" fill="#B8914A"/></g>')

def star(x, y, r, col='#E9C46A'):
    return f'<path d="M{x} {y-r} L{x+r*.3} {y-r*.3} L{x+r} {y} L{x+r*.3} {y+r*.3} L{x} {y+r} L{x-r*.3} {y+r*.3} L{x-r} {y} L{x-r*.3} {y-r*.3}Z" fill="{col}" opacity=".85"/>'

def cover(pal='ru'):
    a = inner(C.adam(150, left='dua', right='dua', mood='closed', pal=pal))
    m = inner(C.maryam(150, left='dua', right='dua', mood='closed', pal=pal))
    return ('<svg viewBox="10 20 300 270" xmlns="http://www.w3.org/2000/svg" class="nw-ill">'
            + lantern(48, 0, 34, 1.0) + lantern(272, 0, 54, .9) + lantern(160, 0, 14, .75)
            + star(96, 40, 5) + star(226, 30, 4) + star(132, 70, 3) + star(196, 64, 3.5)
            + rug(102, 292, '#2F7F73', '#E9C46A') + rug(218, 292, '#C76A86', '#F6E3CC')
            + f'<g transform="translate(36 96) scale(.66)">{a}</g>'
            + f'<g transform="translate(152 96) scale(.66)">{m}</g>'
            + '</svg>')

# ---- наклейки в духе «детского набора»: свои рисунки ----
def mosque(x, y, s=1.0):
    g = '#4E9A6B'; gd = '#2F6F4A'; w = '#F3E6CC'; wd = '#C9A979'; dr = '#6B4A32'
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<rect x="-50" y="18" width="100" height="50" rx="4" fill="{w}" stroke="{wd}" stroke-width="2"/>'
            f'<rect x="-54" y="14" width="108" height="8" rx="3" fill="{wd}"/>'
            f'<path d="M-32 18 Q-32 -30 0 -34 Q32 -30 32 18Z" fill="{g}" stroke="{gd}" stroke-width="2"/>'
            f'<path d="M-18 -8 Q-12 -24 2 -28" stroke="#fff" stroke-width="3" opacity=".35" fill="none" stroke-linecap="round"/>'
            f'<path d="M0 -34 V-44" stroke="{wd}" stroke-width="2"/><path d="M4 -52 a7 7 0 1 0 0 12 a5 5 0 1 1 0 -12z" fill="#E9C46A"/>'
            f'<path d="M-10 68 V48 Q0 34 10 48 V68Z" fill="{dr}"/>'
            + ''.join(f'<path d="M{dx-5} 50 V40 Q{dx} 32 {dx+5} 40 V50Z" fill="{dr}"/>' for dx in (-34, -20, 20, 34)) +
            f'<rect x="56" y="-28" width="14" height="96" rx="2" fill="{w}" stroke="{wd}" stroke-width="2"/>'
            f'<rect x="53" y="-6" width="20" height="6" rx="2" fill="{wd}"/><rect x="53" y="26" width="20" height="6" rx="2" fill="{wd}"/>'
            f'<path d="M55 -28 Q63 -50 71 -28Z" fill="{g}" stroke="{gd}" stroke-width="1.6"/>'
            f'<path d="M60 -14 v8 M66 -14 v8" stroke="{dr}" stroke-width="2.4" stroke-linecap="round"/>'
            f'<path d="M63 -46 v-6" stroke="{wd}" stroke-width="1.6"/></g>')

def quran(x, y, s=1.0):
    wd = '#8A5A34'; wl = '#B07A48'
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-34 30 L28 -6 M34 30 L-28 -6" stroke="{wd}" stroke-width="9" stroke-linecap="round"/>'
            f'<path d="M-34 30 L28 -6 M34 30 L-28 -6" stroke="{wl}" stroke-width="5" stroke-linecap="round"/>'
            f'<path d="M-2 -10 L-40 -2 L-38 10 L0 2Z" fill="#2F7F73"/><path d="M2 -10 L40 -2 L38 10 L0 2Z" fill="#2F7F73"/>'
            f'<path d="M0 -12 Q-18 -22 -38 -6 L-36 4 Q-18 -10 0 0Z" fill="#FBF6EA" stroke="#C9A979" stroke-width="1.4"/>'
            f'<path d="M0 -12 Q18 -22 38 -6 L36 4 Q18 -10 0 0Z" fill="#FBF6EA" stroke="#C9A979" stroke-width="1.4"/>'
            + ''.join(f'<path d="M{-30+i*0} {-6-i*3} Q-18 {-14-i*3} -6 {-8-i*3}" stroke="#9FB8B0" stroke-width="1.2" fill="none"/>'
                      f'<path d="M6 {-8-i*3} Q18 {-14-i*3} 30 {-6-i*3}" stroke="#9FB8B0" stroke-width="1.2" fill="none"/>' for i in range(3)) +
            '</g>')

def tasbih(x, y, s=1.0):
    import math
    b = ''.join(f'<circle cx="{18*math.cos(t/16*2*math.pi):.1f}" cy="{14*math.sin(t/16*2*math.pi):.1f}" r="3.6" fill="#8A4F2E" stroke="#5E3219" stroke-width=".8"/>' for t in range(16))
    return (f'<g transform="translate({x} {y}) scale({s})">{b}'
            f'<path d="M0 14 v10" stroke="#5E3219" stroke-width="2"/><circle cx="0" cy="27" r="3.4" fill="#8A4F2E"/>'
            f'<path d="M-3 30 l3 10 l3 -10z" fill="#C76A86"/></g>')

def kufi(x, y, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-20 6 Q-20 -14 0 -15 Q20 -14 20 6Z" fill="#F2C863" stroke="#B8914A" stroke-width="1.6"/>'
            f'<rect x="-21" y="2" width="42" height="8" rx="3" fill="#2F7F73"/>'
            f'<path d="M-14 -4 l4 -6 l4 6 l4 -6 l4 6 l4 -6 l4 6" stroke="#C76A86" stroke-width="1.6" fill="none"/></g>')

def slippers(x, y, s=1.0):
    one = lambda dx, r: (f'<g transform="translate({dx} 0) rotate({r})"><ellipse cx="0" cy="0" rx="9" ry="16" fill="#A996D8" stroke="#6E5BA6" stroke-width="1.5"/>'
                         f'<path d="M-9 -2 Q0 -14 9 -2 Q0 -6 -9 -2Z" fill="#F2C863"/></g>')
    return f'<g transform="translate({x} {y}) scale({s})">{one(-10, -12)}{one(10, 12)}</g>'

def cover2(pal='ru'):
    a = inner(C.adam(150, left='dua', right='dua', mood='closed', pal=pal))
    m = inner(C.maryam(150, left='dua', right='dua', mood='closed', pal=pal))
    return ('<svg viewBox="0 0 320 300" xmlns="http://www.w3.org/2000/svg" class="nw-ill">'
            + lantern(34, 0, 22, .85) + lantern(78, 0, 46, .7)
            + star(120, 34, 5) + star(150, 62, 3) + star(18, 92, 3)
            + mosque(232, 66, .82)
            + rug(112, 284, '#2F7F73', '#E9C46A') + rug(212, 284, '#C76A86', '#F6E3CC')
            + f'<g transform="translate(54 108) scale(.6)">{a}</g>'
            + f'<g transform="translate(156 108) scale(.6)">{m}</g>'
            + quran(36, 246, .78) + tasbih(292, 214, .9) + kufi(28, 160, .9) + slippers(292, 272, .8)
            + '</svg>')

def items():
    """Иллюстрация для карты мира: только предметы, без детей."""
    return ('<svg viewBox="0 0 320 210" xmlns="http://www.w3.org/2000/svg" class="nw-ill">'
            + lantern(40, 0, 18, .8) + lantern(86, 0, 40, .65) + lantern(282, 0, 26, .72)
            + star(126, 30, 5) + star(236, 22, 4) + star(20, 96, 3) + star(300, 110, 3.5)
            + mosque(176, 92, .9)
            + rug(160, 202, '#2F7F73', '#E9C46A')
            + quran(62, 176, .95) + tasbih(286, 136, .95) + kufi(46, 120, 1.0) + slippers(250, 190, .85)
            + '</svg>')
