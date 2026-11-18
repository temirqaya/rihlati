"""Минималистичная обложка (для книги ученика и книги учителя)."""
from lib import *

def cover(book, subtitle="Рабочая книга для детей", badge=None, kids=True):
    arch = ('<svg class="cm-arch" viewBox="0 0 300 380" xmlns="http://www.w3.org/2000/svg">'
            '<path d="M20 370 L20 150 Q20 90 110 60 Q140 48 150 14 Q160 48 190 60 Q280 90 280 150 L280 370" fill="none" stroke="#C9A15B" stroke-width="2.5"/>'
            '<path d="M36 370 L36 156 Q36 104 118 76 Q142 66 150 40 Q158 66 182 76 Q264 104 264 156 L264 370" fill="none" stroke="#C9A15B" stroke-width="1" opacity=".6"/>'
            f'{crescent(150, 2, 0)}</svg>')
    moon = f'<svg class="cm-moon" viewBox="0 0 60 60"><circle cx="28" cy="30" r="20" fill="#D8B26A"/><circle cx="37" cy="25" r="17" fill="#FBF6F0"/>{star(46, 44, 5, "#D8B26A")}</svg>'
    k = f'<div class="cm-kids">{adam(150, right="wave")}{maryam(150, left="wave")}</div>' if kids else ""
    b = f'<div class="cm-badge">{badge}</div>' if badge else ""
    book.add(f'''<section class="page cover-min">
<div class="cm-frame"></div>
<div class="cm-in">
{moon}
<div class="cm-ar" lang="ar" dir="rtl">رِحْلَتِي مَعَ الْقُرْآنِ</div>
<div class="cm-line"></div>
<div class="cm-ru">Моё путешествие<br>к чтению Священного Корана</div>
<div class="cm-sub">{subtitle}</div>{b}
<div class="cm-stage">{arch}{k}</div>
</div></section>''', raw=True)

CSS = """
.cover-min{background:#FBF6F0}
.cm-frame{position:absolute;inset:10mm;border:1.5px solid #D8B26A;border-radius:6mm}
.cm-in{position:absolute;inset:24mm 20mm 10mm;display:flex;flex-direction:column;align-items:center;text-align:center}
.cm-moon{width:16mm;height:16mm;margin-bottom:6mm}
.cm-ar{font-family:"Amiri";font-weight:700;font-size:64px;line-height:1.5;color:#3E5180}
.cm-line{width:30mm;height:1.5px;background:#D8B26A;margin:4mm 0 6mm}
.cm-ru{font-weight:800;font-size:27px;line-height:1.25;color:#5C342E;letter-spacing:.01em}
.cm-sub{margin-top:5mm;font-size:12.5px;font-weight:700;letter-spacing:.28em;text-transform:uppercase;color:#B8914A}
.cm-badge{margin-top:4mm;font-family:"Amiri";font-weight:700;font-size:26px;color:#3E5180}
.cm-stage{position:relative;width:110mm;height:120mm;margin-top:auto;margin-bottom:6mm}
.cm-arch{position:absolute;inset:0;width:100%;height:100%}
.cm-kids{position:absolute;left:0;right:0;bottom:0;display:flex;justify-content:center;gap:2mm}
"""
