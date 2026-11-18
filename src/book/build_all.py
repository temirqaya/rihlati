#!/usr/bin/env python3
"""Полная сборка книги «رِحْلَتِي مَعَ الْقُرْآنِ» → book_full.html (затем Chrome → PDF)."""
from lib import Book, ROOT
import sections_a as A, sections_b as B, intro as I

book = Book()
A.cover(book); A.meet(book); I.hadith_page(book); A.toc_page(book); I.alphabet_page(book); I.sun_moon_page(book); A.map_page(book)
A.section1(book); A.section2(book); A.section3(book)
B.section4(book); B.section5(book); B.section6(book); B.section7(book); B.section8(book)
B.section9(book); B.section10(book); B.review_sheet(book); B.cards(book)

toc = "".join(f'<div class="toc-r"><span lang="ar" dir="rtl">{ar}</span><b>{ru}</b><i></i><em>{n}</em></div>' for (ru, ar), n in book.toc)
pages = [p.replace("{TOC}", toc) for p in book.pages]
css = (ROOT / "style.css").read_text(encoding="utf-8") + (ROOT / "style2.css").read_text(encoding="utf-8")
html = f'''<!doctype html><html lang="ru"><head><meta charset="utf-8"><title>Моё путешествие к чтению Священного Корана</title>
<style>{css}</style></head><body>{"".join(pages)}</body></html>'''
(ROOT / "book_full.html").write_text(html, encoding="utf-8")
print("pages:", len(pages))
