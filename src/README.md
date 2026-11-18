# Рихляти — исходники

Сайт в корне репозитория (`index.html`, `qt/`, `tr/`) **собирается автоматически** из этих файлов.
Готовые `index.html` руками не правим — правим исходники и пересобираем.

## Что где
| Файл | Отвечает за |
|---|---|
| `book/online/book_template.html` | обложка, карта, уроки букв (раздел 1), игры из книги, таблица букв, «Об этом приложении», стили |
| `book/online/har.js` | огласовки, танвин, мадд (разделы 2, 4, 5) |
| `book/online/sk.js` | сукун и шадда (раздел 3) |
| `book/online/p.js` | движок разделов 6–11 |
| `book/online/pdata.py` | тексты разделов 6–11 (слова, махраджи, таджвид, суры, диплом, игры) |
| `book/online/mouth.py` | рисунок головы (махраджи) |
| `book/chars4.py` | персонажи Зейнеб и Юсуф |
| `book/online/ct.py`, `ct2.py`, `new_tr.py` | крымскотатарский перевод |
| `book/online/tr_vals.py`, `tr2.py`, `new_tr.py` | турецкий перевод |
| `book/online/voice.json` | голос автора: слоги (фатха/касра/дамма, сукун, шадда, танвин, мадд), первые слова |
| `book/online/voice_names_ru.json`, `voice_names.json` | названия букв (рус / крымскотат.+тур.) |
| `book/online/songs.json` | песенка махраджей, озвучка сур |
| `book/quran_hafs.json` | текст Корана (Хафс) |
| `book/fonts/` | шрифты Amiri Quran и Nunito (лицензия OFL) |

## Сборка
Папка `book/` должна лежать по пути `/home/claude/book`, сайт — в `/home/claude/ruhlar-`.
```
cd /home/claude/book/online
python3 pdata.py && python3 pdata.py ct && python3 pdata.py tr
python3 build_book.py
python3 make_all.py
```
После сборки поднять версию кэша в `sw.js` (`rihlati-vNN`).
