"""Пробная страница в стиле «ночной сад»: фонари, лианы с цветами, лента-баннер, пергамент."""
import math, random
from lib import *

def lantern(x, y, s=1, chain=60):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M0 {-chain} V0" stroke="#C9A15B" stroke-width="2.5" stroke-dasharray="4 3"/>'
            f'<circle cx="0" cy="32" r="38" fill="#F7D774" opacity=".18"/><circle cx="0" cy="32" r="22" fill="#F7D774" opacity=".25"/>'
            f'<path d="M-10 0 h20 l6 10 h-32z" fill="#C9A15B" stroke="#8B6A2E" stroke-width="1.5"/>'
            f'<path d="M-16 10 Q-22 32 -12 54 H12 Q22 32 16 10Z" fill="#FFE7A3" stroke="#B8914A" stroke-width="2.5"/>'
            f'<path d="M-6 12 Q-10 32 -5 52 M6 12 Q10 32 5 52 M0 10 V54" stroke="#D8B26A" stroke-width="1.8" fill="none"/>'
            f'<ellipse cx="0" cy="34" rx="5" ry="9" fill="#fff" opacity=".9"/>'
            f'<path d="M-14 54 h28 l-6 10 h-16z" fill="#C9A15B" stroke="#8B6A2E" stroke-width="1.5"/><circle cx="0" cy="70" r="3.5" fill="#C9A15B"/></g>')

def vine(side, h=1123):
    random.seed(11 if side < 0 else 23)
    x0 = 18 if side < 0 else 776
    d = f"M{x0} 0 " + " ".join(f"Q{x0 + side*-26} {y+40} {x0} {y+80}" for y in range(0, h, 80))
    leaves = ""
    for y in range(20, h, 34):
        lx = x0 + side * -random.randint(4, 22)
        rot = random.randint(-60, 60) + (0 if side < 0 else 180)
        leaves += f'<ellipse cx="{lx}" cy="{y}" rx="13" ry="5.5" transform="rotate({rot} {lx} {y})" fill="{random.choice(["#4E7A4A", "#5E9E4E", "#3F6B3C"])}"/>'
    flowers = "".join(flower(x0 + side * -random.randint(8, 30), y, random.choice([1.2, 1.5, 1.8]), random.choice(["#E9A0B8", "#C9A0DC", "#F4C6D6", "#fff"]), GOLD)
                      for y in range(40, h, random.choice([70, 80, 90])))
    return f'<path d="{d}" stroke="#4E6B3E" stroke-width="5" fill="none"/>{leaves}{flowers}'

def ribbon(text, y, w=540, col="#4B3A8C", col2="#33276A"):
    x = (794 - w) / 2
    return (f'<g><path d="M{x-40} {y+12} L{x+10} {y+12} L{x+10} {y+62} L{x-40} {y+62} L{x-22} {y+37}Z" fill="{col2}"/>'
            f'<path d="M{x+w+40} {y+12} L{x+w-10} {y+12} L{x+w-10} {y+62} L{x+w+40} {y+62} L{x+w+22} {y+37}Z" fill="{col2}"/>'
            f'<path d="M{x} {y} Q{x+w/2} {y-16} {x+w} {y} L{x+w} {y+54} Q{x+w/2} {y+38} {x} {y+54}Z" fill="{col}" stroke="#D8B26A" stroke-width="2.5"/>'
            f'<path d="M{x+8} {y+7} Q{x+w/2} {y-8} {x+w-8} {y+7}" stroke="#D8B26A" stroke-width="1.2" stroke-dasharray="3 4" fill="none"/>'
            f'<text x="397" y="{y+33}" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="23" fill="#FFF6E0">{text}</text></g>')

def mosque(x, y, s, fill, op=1):
    return (f'<g transform="translate({x} {y}) scale({s})" fill="{fill}" opacity="{op}">'
            f'<rect x="-50" y="0" width="100" height="60"/><path d="M-30 0 Q-30 -40 0 -52 Q30 -40 30 0Z"/>'
            f'<rect x="-2" y="-66" width="4" height="16"/><rect x="-70" y="-50" width="12" height="110"/><path d="M-70 -50 L-64 -72 L-58 -50Z"/>'
            f'<rect x="58" y="-50" width="12" height="110"/><path d="M58 -50 L64 -72 L70 -50Z"/></g>')

def welcome_page():
    random.seed(4)
    stars = "".join(star(random.randint(60, 734), random.randint(20, 520), random.choice([2.5, 3, 4, 6]), random.choice(["#FFF6E0", "#F7D774", "#fff"])) for _ in range(60))
    bg = f'''<svg class="fz-bg" viewBox="0 0 794 1123" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
<defs><linearGradient id="nsky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1F2A55"/><stop offset=".45" stop-color="#3E5180"/><stop offset=".75" stop-color="#6E5A8E"/><stop offset="1" stop-color="#5C342E"/></linearGradient>
<radialGradient id="glow" cx=".5" cy=".75" r=".5"><stop offset="0" stop-color="#F7D774" stop-opacity=".35"/><stop offset="1" stop-color="#F7D774" stop-opacity="0"/></radialGradient></defs>
<rect width="794" height="1123" fill="url(#nsky)"/><rect width="794" height="1123" fill="url(#glow)"/>{stars}
{crescent(60, 470, 22, "#F7D774", "#34457A")}
{mosque(110, 640, 1.2, "#2A3768", .9)}{mosque(690, 630, 1.1, "#2A3768", .9)}{mosque(400, 700, 1.8, "#33427A", .7)}
{"".join(f'<circle cx="{random.randint(80, 714)}" cy="{random.randint(640, 760)}" r="{random.choice([1.5, 2, 2.5])}" fill="#F7D774" opacity=".8"/>' for _ in range(70))}
<path d="M280 1123 Q330 900 397 760 Q464 900 514 1123Z" fill="#7A6A9A" opacity=".55"/>
<path d="M300 1123 Q340 920 397 770 Q454 920 494 1123" stroke="#D8B26A" stroke-width="2" stroke-dasharray="3 10" fill="none"/>
{vine(-1)}{vine(1)}
{lantern(62, 200, .9, 200)}{lantern(734, 230, .9, 230)}
</svg>'''
    items = [("أ ب ت", "Познакомимся<br>с арабскими буквами"), ("👄", "Научимся правильно<br>произносить звуки"),
             ("◌َ ◌ِ ◌ُ", "Узнаем волшебные<br>знаки — харакаты"), ("📖", "Изучим простые<br>правила таджвида"), ("⭐", "Будем читать, играть<br>и собирать звёздочки!")]
    circ = "".join(f'<div class="fz-it"><div class="fz-c"><span{" lang=ar" if "◌" in a or "أ" in a else ""}>{a}</span></div><p>{t}</p></div>' for a, t in items)
    return f'''<section class="page fz">{bg}
<svg class="fz-top" viewBox="0 0 794 140">{ribbon("Добро пожаловать в наше путешествие!", 50, w=600)}</svg>
<div class="fz-parch">
<div class="fz-h">Ассаляму алейкум, дорогой друг!</div>
<p>Мы очень рады, что ты отправляешься в удивительное путешествие в мир арабских букв и правильного чтения Корана!</p>
<p>Мы — Зейнеб и Юсуф — будем твоими друзьями и помощниками.</p>
<p>Вместе мы научимся читать буквы, слова и аяты из Корана красиво и правильно, с любовью к Аллаху ❤</p>
</div>
<div class="fz-kids"><div>{adam(230, right="wave", mood="open")}</div><div>{maryam(230, left="wave", mood="open")}</div></div>
<div class="fz-names">
<div class="fz-n g"><span>📗</span><div><b>Это Юсуф!</b><p>Я люблю читать Коран, задавать вопросы и узнавать новое!</p></div></div>
<div class="fz-n p"><span>⭐</span><div><b>Это Зейнеб!</b><p>Я люблю звёзды, красивое чтение и помогать друзьям!</p></div></div></div>
<div class="fz-wait"><div class="fz-wh">Что нас ждёт?</div><div class="fz-its">{circ}</div></div>
<div class="fz-bot">⭐ <span>Готов? Тогда давай скажем вместе:<br><b>«Бисмиллях» — и начнём наше путешествие!</b></span> ⭐</div>
</section>'''

CSS = '''
.fz{background:#1F2A55}
.fz-bg{position:absolute;inset:0;width:100%;height:100%}
.fz-top{position:absolute;top:2mm;left:0;width:100%;z-index:3}
.fz-star{position:absolute;top:30mm;right:12mm;width:18mm;height:18mm;z-index:3}
.fz-star svg{width:100%;height:100%}.fz-star b{position:absolute;inset:0;display:grid;place-items:center;color:#FFF6E0;font-weight:900;font-size:22px;padding-top:1mm}
.fz-parch{position:absolute;top:36mm;left:30mm;right:30mm;background:linear-gradient(180deg,#FFF8EA,#F4EBE2);border-radius:26px 26px 40px 40px;
  border:3px solid #D8B26A;box-shadow:0 0 0 6px rgba(255,248,234,.35),0 6px 18px rgba(0,0,0,.35);padding:6mm 9mm 9mm;text-align:center;color:#4A2C27;z-index:2}
.fz-h{font-weight:900;font-size:22px;color:#3F6B3C;margin-bottom:2mm}
.fz-parch p{font-size:15.5px;font-weight:700;line-height:1.5;margin:1mm 0}
.fz-kids{position:absolute;top:118mm;left:14mm;right:14mm;display:flex;justify-content:space-between;z-index:2}
.fz-kids .char{filter:drop-shadow(0 6px 10px rgba(0,0,0,.35))}
.fz-names{position:absolute;top:186mm;left:16mm;right:16mm;display:grid;grid-template-columns:1fr 1fr;gap:10mm;z-index:3}
.fz-n{display:flex;gap:3mm;align-items:center;border-radius:40px;padding:3mm 6mm;border:2.5px dashed #fff;box-shadow:0 4px 10px rgba(0,0,0,.3)}
.fz-n.g{background:#E5EEDC;outline:3px solid #A8C49A}.fz-n.p{background:#F8E1E6;outline:3px solid #E9A0B8}
.fz-n span{font-size:34px}.fz-n b{font-size:19px;font-weight:900;color:#3F6B3C}.fz-n.p b{color:#A8473B}
.fz-n p{font-size:12.5px;font-weight:700;color:#4A2C27}
.fz-wait{position:absolute;top:214mm;left:16mm;right:16mm;background:#FFF3D6;border:3px solid #D8B26A;border-radius:24px;padding:3mm 4mm;z-index:3;box-shadow:0 4px 12px rgba(0,0,0,.3)}
.fz-wh{text-align:center;font-weight:900;font-size:21px;color:#3F6B3C}
.fz-its{display:grid;grid-template-columns:repeat(5,1fr);gap:2mm;margin-top:2mm}
.fz-it{text-align:center}
.fz-c{width:24mm;height:24mm;margin:0 auto;border-radius:50%;background:radial-gradient(circle at 40% 35%,#fff,#F3E3C6);border:3px solid #D8B26A;display:grid;place-items:center;box-shadow:0 0 0 3px #fff inset}
.fz-c span{font-size:30px;line-height:1}.fz-c span[lang]{font-family:"Amiri";font-weight:700;font-size:24px;color:#3E5180;line-height:1.6}
.fz-it p{font-size:11px;font-weight:800;line-height:1.25;margin-top:1.5mm;color:#4A2C27}
.fz-bot{position:absolute;bottom:9mm;left:22mm;right:22mm;background:#4B3A8C;border:2.5px solid #D8B26A;border-radius:40px;color:#FFF6E0;text-align:center;
  padding:2.5mm 6mm;font-size:14px;z-index:3;display:flex;align-items:center;justify-content:space-between;font-size:26px}
.fz-bot span{font-size:14px;line-height:1.4}.fz-bot b{font-size:17px}
'''

if __name__ == "__main__":
    css = (ROOT / "style.css").read_text(encoding="utf-8") + (ROOT / "style2.css").read_text(encoding="utf-8") + (ROOT / "style3.css").read_text(encoding="utf-8") + CSS
    (ROOT / "fancy_test.html").write_text(f'<!doctype html><html lang="ru"><head><meta charset="utf-8"><style>{css}</style></head><body>{welcome_page()}</body></html>', encoding="utf-8")

def welcome_soft():
    items = [("أ ب ت", "Познакомимся<br>с арабскими буквами"), ("👄", "Научимся правильно<br>произносить звуки"),
             ("◌َ ◌ِ ◌ُ", "Узнаем волшебные<br>знаки — харакаты"), ("📖", "Изучим простые<br>правила таджвида"), ("⭐", "Будем читать, играть<br>и собирать звёздочки!")]
    circ = "".join(f'<div class="ws-it"><div class="ws-c" style="background:{["#E4EDDC", "#F8E1E6", "#E8E2F5", "#DDEAF5", "#F8EDD3"][i]}"><span{" lang=ar" if "◌" in a or "أ" in a else ""}>{a}</span></div><p>{t}</p></div>' for i, (a, t) in enumerate(items))
    return f'''<section class="page ws">{sky_svg()}
<div class="ws-in">
<div class="ws-k">Добро пожаловать в наше путешествие!</div>
<div class="ws-line"></div>
<div class="ws-h">Ассаляму алейкум, дорогой друг!</div>
<p class="ws-p">Мы очень рады, что ты отправляешься в удивительное путешествие в мир арабских букв и правильного чтения Корана!</p>
<div class="ws-kids">
<div class="ws-kid"><div class="ws-say a">Ассаляму алейкум! Меня зовут <b>Юсуф</b>. Я очень люблю буквы, задаю много вопросов и никогда не сдаюсь. Пойдём учиться вместе?</div>{adam(175, right="wave", mood="open")}</div>
<div class="ws-kid"><div class="ws-say m">Ва алейкум ассалям! А меня зовут <b>Зейнеб</b>. Я люблю звёздочки и красивое чтение. Если станет трудно — я всегда помогу!</div>{maryam(175, left="wave", mood="open")}</div></div>
<p class="ws-p2">Вместе мы научимся читать буквы, слова и аяты из Корана красиво и правильно, с любовью к Аллаху ❤</p>
<div class="ws-wh">Что нас ждёт?</div>
<div class="ws-its">{circ}</div>
<div class="ws-bot">Готов? Тогда давай скажем вместе: <b>«Бисмиллях»</b> — и начнём наше путешествие!</div>
</div>{{PNUM}}</section>'''

CSS += """
.ws-in{position:absolute;inset:20mm 22mm 20mm;display:flex;flex-direction:column;align-items:center;text-align:center}
.ws-k{font-weight:700;font-size:12.5px;letter-spacing:.25em;text-transform:uppercase;color:#B8914A}
.ws-line{width:28mm;height:1.5px;background:#D8B26A;margin:4mm 0 6mm}
.ws-h{font-weight:800;font-size:24px;color:#3E5180}
.ws-p{font-size:14.5px;line-height:1.7;color:#5C342E;margin-top:3mm;max-width:150mm}
.ws-kids{display:grid;grid-template-columns:1fr 1fr;gap:8mm;margin-top:5mm;width:100%}
.ws-say{position:relative;border-radius:20px;padding:3mm 5mm;font-size:13px;line-height:1.5;color:#4A2C27;margin-bottom:4mm;min-height:27mm;display:block}
.ws-say::after{content:"";position:absolute;bottom:-7px;left:50%;width:14px;height:14px;transform:translateX(-50%) rotate(45deg);background:inherit;border:inherit;border-top:0;border-left:0}
.ws-say.a{background:#E4EDDC;border:1.5px solid #A8C49A}.ws-say.m{background:#F8E1E6;border:1.5px solid #E9A0B8}
.ws-say b{color:#3E5180;font-size:inherit;margin:0}
.ws-p2{font-size:14px;line-height:1.6;color:#5C342E;margin-top:5mm;max-width:150mm;font-weight:600}
.ws-kid{display:flex;flex-direction:column;align-items:center;gap:1mm}
.ws-kid b{font-size:18px;color:#3E5180;margin-top:2mm}
.ws-kid span{font-size:12.5px;color:#7A5A52;max-width:62mm;line-height:1.5}
.ws-wh{font-weight:800;font-size:18px;color:#5C342E;margin-top:8mm}
.ws-its{display:grid;grid-template-columns:repeat(5,1fr);gap:3mm;margin-top:4mm;width:100%}
.ws-c{width:20mm;height:20mm;margin:0 auto;border-radius:50%;border:1.5px solid #D8B26A;display:grid;place-items:center;background:#fff}
.ws-c span{font-size:24px;line-height:1}.ws-c span[lang]{font-family:"Amiri";font-weight:700;font-size:20px;color:#3E5180;line-height:1.6}
.ws-it p{font-size:10.5px;line-height:1.35;margin-top:2mm;color:#7A5A52;font-weight:600}
.ws-bot{margin-top:auto;font-size:13.5px;color:#5C342E;border-top:1.5px solid #E8DCD0;padding-top:4mm;width:100%}
.ws-bot b{color:#3E5180}
"""
