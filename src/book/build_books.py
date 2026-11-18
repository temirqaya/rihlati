#!/usr/bin/env python3
"""Сборка двух книг: ученика (book_student.html) и учителя (book_teacher.html)."""
from lib import Book, ROOT, star, GOLD
import sections_a as A, sections_b as B, intro as I, teacher as T, closing as C, fancy as F, cover_min as CM, extras as E

def render(book, name, title):
    toc = "".join(f'<div class="toc-r"><span lang="ar" dir="rtl">{ar}</span><b>{ru}</b><i></i><em>{n}</em></div>' for (ru, ar), n in book.toc)
    pages = [p.replace("{TOC}", toc) for p in book.pages]
    css = (ROOT / "style.css").read_text(encoding="utf-8") + (ROOT / "style2.css").read_text(encoding="utf-8") + (ROOT / "style3.css").read_text(encoding="utf-8") + F.CSS + CM.CSS + E.CSS + (ROOT / "style4.css").read_text(encoding="utf-8")
    (ROOT / name).write_text(f'<!doctype html><html lang="ru"><head><meta charset="utf-8"><title>{title}</title><style>{css}</style></head><body>{"".join(pages)}</body></html>', encoding="utf-8")
    print(name, len(pages))

s = Book()
A.cover(s); s.add(F.welcome_soft(), raw=True); s.pages[-1] = s.pages[-1].replace("{PNUM}", s.pnum_html(len(s.pages))); A.meet(s); I.hadith_page(s); A.toc_page(s); I.alphabet_page(s); I.sun_moon_page(s); A.map_page(s)
E.install_openers(s)
A.section1(s); A.section2(s); A.section3(s)
B.section4(s); B.section5(s); B.section6(s); B.section7(s); B.section8(s)
B.section9(s); B.section10(s)
E.stickers(s, B.SEC10)
C.build(s)
E.back_cover(s, "Добрая рабочая книга для самых маленьких: 28 букв, огласовки, первые правила таджвида и первые суры — вместе с Зейнеб и Юсуфом, шаг за шагом, с играми и любовью.")
render(s, "book_student.html", "Моё путешествие к чтению Священного Корана — книга ученика")

t = Book()
import cover_min as CM, extras as E
CM.cover(t, "Книга учителя", badge="دَلِيلُ الْمُعَلِّمِ")

t.add('<h1 class="title">Содержание</h1><div class="toc">{TOC}</div>', section=T.TSEC)
T.build(t, s.meta)
E.back_cover(t, "Книга учителя к рабочей книге «Моё путешествие к чтению Священного Корана»: план уроков, подсказки, ответы и материалы для занятий.")
render(t, "book_teacher.html", "Моё путешествие к чтению Священного Корана — книга учителя")
