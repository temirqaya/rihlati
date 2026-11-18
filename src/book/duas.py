#!/usr/bin/env python3
"""Карточки дуа для детей — с Зейнеб и Юсуфом, в стиле книги."""
import lib
from lib import *
import cover_min as CM, extras as E, fancy as F, metod as M

OUT = "#5C342E"
SW = f'stroke="{OUT}" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"'
def ic(body):
    return f'<svg viewBox="0 0 100 100" class="dic">{body}</svg>'

ICONS = {
 "food": ic(f'<ellipse cx="50" cy="62" rx="40" ry="16" fill="#fff" {SW}/><ellipse cx="50" cy="58" rx="28" ry="9" fill="#F3E3C6"/>'
            f'<path d="M30 52 Q36 34 50 36 Q64 34 70 52Z" fill="#E0A55B" {SW}/><path d="M86 20 V56 M80 20 V34 Q80 40 86 40 Q92 40 92 34 V20" {SW} fill="none"/><path d="M14 20 Q22 30 14 40 V56" {SW} fill="none"/>'),
 "after": ic(f'<ellipse cx="50" cy="64" rx="40" ry="14" fill="#fff" {SW}/><ellipse cx="50" cy="61" rx="27" ry="7" fill="#F7F0E8"/><path d="M38 30 q4 -10 12 0 q8 -10 12 0 q0 10 -12 18 q-12 -8 -12 -18z" fill="#E9A0B8" {SW}/>'),
 "adhan": ic(f'<rect x="40" y="30" width="20" height="62" fill="#FBF6F0" {SW}/><path d="M36 30 H64 L60 22 H40Z" fill="#D8B26A" {SW}/><path d="M42 22 Q42 8 50 4 Q58 8 58 22Z" fill="#6F86C2" {SW}/>'
             f'<rect x="46" y="40" width="8" height="12" rx="4" fill="#6F86C2"/><path d="M70 30 q8 8 0 16 M78 24 q14 14 0 28" stroke="#C9A15B" stroke-width="3" fill="none" stroke-linecap="round"/><path d="M30 30 q-8 8 0 16 M22 24 q-14 14 0 28" stroke="#C9A15B" stroke-width="3" fill="none" stroke-linecap="round"/>'),
 "quran": ic(f'<path d="M14 84 L50 60 L86 84" fill="none" {SW}/><path d="M50 26 Q32 16 12 22 V66 Q32 60 50 70 Q68 60 88 66 V22 Q68 16 50 26Z" fill="#5E7F4E" {SW}/>'
             f'<path d="M50 28 Q34 20 18 26 V62 Q34 58 50 66Z M50 28 Q66 20 82 26 V62 Q66 58 50 66Z" fill="#FBF6F0"/><path d="M24 36 H42 M24 44 H42 M58 36 H76 M58 44 H76" stroke="#C9A15B" stroke-width="2.5"/>'),
 "sleep": ic(f'<path d="M62 12 A36 36 0 1 0 88 66 A28 28 0 1 1 62 12Z" fill="#F7D774" {SW}/><path d="M44 50 q4 4 8 0" stroke="{OUT}" stroke-width="2.5" fill="none"/><path d="M30 46 q4 4 8 0" stroke="{OUT}" stroke-width="2.5" fill="none"/>'
             f'<text x="70" y="34" font-family="Nunito" font-weight="900" font-size="14" fill="#6F86C2">z</text><text x="78" y="22" font-family="Nunito" font-weight="900" font-size="18" fill="#6F86C2">Z</text>'),
 "wake": ic(f'<path d="M6 76 H94" {SW}/>' + "".join(f'<rect x="47" y="14" width="6" height="14" rx="3" fill="#F2B544" transform="rotate({a} 50 72)"/>' for a in (-70, -35, 0, 35, 70)) + f'<path d="M22 76 A28 28 0 0 1 78 76Z" fill="#F7D774" {SW}/>'),
 "out": ic(f'<rect x="26" y="14" width="40" height="78" rx="3" fill="#A56C47" {SW}/><path d="M66 14 L84 22 V96 L66 92" fill="#8B5A3C" {SW}/><circle cx="74" cy="56" r="3" fill="#D8B26A"/><path d="M6 92 H94" {SW}/>'),
 "home": ic(f'<path d="M12 46 L50 14 L88 46Z" fill="#A8473B" {SW}/><rect x="20" y="44" width="60" height="46" fill="#F4EBE2" {SW}/><path d="M42 90 V64 Q50 56 58 64 V90Z" fill="#5C342E"/><path d="M32 70 q-2 -6 4 -6 q4 0 4 6 q-4 5 -4 5 q0 0 -4 -5z" fill="#E9A0B8"/>'),
 "study": ic(f'<rect x="14" y="60" width="64" height="12" rx="2" fill="#6F86C2" {SW}/><rect x="20" y="48" width="58" height="12" rx="2" fill="#E5BFAE" {SW}/><rect x="16" y="36" width="56" height="12" rx="2" fill="#A8C49A" {SW}/>'
             f'<path d="M82 14 L92 24 L60 56 L48 58 L50 46Z" fill="#F2B544" {SW}/>'),
 "parents": ic(f'<path d="M50 88 Q10 60 14 34 Q18 14 36 16 Q46 18 50 30 Q54 18 64 16 Q82 14 86 34 Q90 60 50 88Z" fill="#E9A0B8" {SW}/><path d="M30 34 q4 -8 12 -6" stroke="#fff" stroke-width="4" fill="none" stroke-linecap="round"/>'),
 "sneeze": ic(f'<circle cx="38" cy="54" r="26" fill="#F6DCC6" stroke="#C99A7A" stroke-width="2.5"/><path d="M28 50 q4 -4 8 0 M42 50 q4 -4 8 0" stroke="{OUT}" stroke-width="2.5" fill="none"/><ellipse cx="38" cy="66" rx="5" ry="4" fill="#9C3F3A"/>'
              f'<path d="M66 30 Q74 22 82 30 Q92 30 90 40 Q96 50 86 54 H66 Q56 52 58 42 Q56 30 66 30Z" fill="#E4EAF6" stroke="#8E9DC6" stroke-width="2"/><text x="76" y="46" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="11" fill="#6F86C2">апчхи!</text>'),
 "wc": ic(f'<path d="M40 10 V30 Q40 38 50 38 H70" fill="none" {SW}/><rect x="66" y="30" width="18" height="16" rx="4" fill="#8E9DC6" {SW}/><path d="M75 50 q-6 10 0 14 q6 -4 0 -14z" fill="#8FC3EC" {SW}/><path d="M60 80 q-6 10 0 14 q6 -4 0 -14z" fill="#8FC3EC" {SW}/><path d="M6 96 H94" {SW}/>'),
}

from icons import ICONS as WI
ICONS.update({
 "mosque": ic(f'<rect x="18" y="52" width="64" height="40" fill="#FBF6F0" {SW}/><path d="M28 52 Q28 24 50 18 Q72 24 72 52Z" fill="#5E7F4E" {SW}/><path d="M50 18 V8" {SW}/><circle cx="50" cy="7" r="3" fill="#D8B26A"/>'
              f'<rect x="6" y="34" width="10" height="58" fill="#FBF6F0" {SW}/><path d="M6 34 L11 22 L16 34Z" fill="#D8B26A"/><rect x="84" y="34" width="10" height="58" fill="#FBF6F0" {SW}/><path d="M84 34 L89 22 L94 34Z" fill="#D8B26A"/>'
              f'<path d="M42 92 V72 Q50 64 58 72 V92Z" fill="#5C342E"/>'),
 "mosque_out": ic(f'<rect x="18" y="52" width="64" height="40" fill="#FBF6F0" {SW}/><path d="M28 52 Q28 24 50 18 Q72 24 72 52Z" fill="#3C7FB0" {SW}/><path d="M42 92 V72 Q50 64 58 72 V92Z" fill="#F7D774" {SW}/>{star(80, 18, 9, "#D8B26A")}'),
 "clothes": WI["ثَوْبٌ"].replace('class="ico"', 'class="dic"'),
 "mirror": ic(f'<ellipse cx="50" cy="42" rx="30" ry="36" fill="#E4EAF6" {SW}/><path d="M34 30 q6 -12 18 -14" stroke="#fff" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M50 78 V94 M36 94 H64" {SW}/>{star(70, 56, 6, "#D8B26A")}'),
 "rain": ic(f'<path d="M24 52 Q8 52 10 38 Q12 26 26 28 Q30 10 50 10 Q70 10 74 28 Q92 26 92 42 Q92 52 78 52Z" fill="#DCE6F5" {SW}/>' + "".join(f'<path d="M{x} {y} q-5 9 0 12 q5 -3 0 -12z" fill="#6F9FD8"/>' for x, y in [(30, 62), (50, 70), (70, 62), (40, 80), (62, 82)])),
 "car": ic(f'<path d="M10 66 V52 Q12 44 22 42 L32 26 Q36 22 44 22 H62 Q70 22 74 28 L84 42 Q92 44 92 52 V66Z" fill="#E8505B" {SW}/><path d="M36 30 H48 V42 H28Z M54 30 H66 L74 42 H54Z" fill="#E4EAF6" {SW}/>'
           f'<circle cx="28" cy="68" r="10" fill="#4A2C27"/><circle cx="74" cy="68" r="10" fill="#4A2C27"/><circle cx="28" cy="68" r="4" fill="#ddd"/><circle cx="74" cy="68" r="4" fill="#ddd"/>'),
 "hard": ic(f'<path d="M6 88 L36 34 L52 58 L64 42 L94 88Z" fill="#A8C49A" {SW}/><path d="M36 34 L44 48 L36 46 L28 50Z" fill="#fff"/><path d="M50 88 Q52 70 50 62" stroke="#5C342E" stroke-width="2" stroke-dasharray="3 4" fill="none"/>{star(78, 18, 8, "#D8B26A")}'),
 "yunus": WI["حُوتٌ"].replace('class="ico"', 'class="dic"'),
 "nice": WI["وَرْدَةٌ"].replace('class="ico"', 'class="dic"'),
 "thanks": ic(f'<rect x="16" y="40" width="68" height="50" rx="4" fill="#E9A0B8" {SW}/><rect x="10" y="30" width="80" height="14" rx="4" fill="#F2B544" {SW}/><path d="M50 30 V90" stroke="#fff" stroke-width="7"/>'
              f'<path d="M50 30 Q36 8 28 20 Q24 30 50 30 Q76 30 72 20 Q64 8 50 30Z" fill="#F2B544" {SW}/>'),
 "salam": WI["يَدٌ"].replace('class="ico"', 'class="dic"'),
 "istighfar": ic(f'<path d="M30 92 Q20 70 22 46 Q24 36 30 38 Q34 40 34 50 V64 M70 92 Q80 70 78 46 Q76 36 70 38 Q66 40 66 50 V64" fill="#F6DCC6" stroke="#C99A7A" stroke-width="2.5" stroke-linecap="round"/>'
                 f'<path d="M30 40 Q30 24 38 22 Q44 22 44 34 V62 M70 40 Q70 24 62 22 Q56 22 56 34 V62" fill="#F6DCC6" stroke="#C99A7A" stroke-width="2.5"/>{star(50, 16, 9, "#D8B26A")}{star(32, 8, 4, "#D8B26A")}{star(68, 8, 4, "#D8B26A")}'),
})

# (ключ, заголовок, арабский текст, чтение, смысл, кто говорит, цвет)
DUAS = [
 ("food", "Перед едой", "بِسْمِ اللَّهِ", "Бисмиллях", "С именем Аллаха.", "Если забыл в начале, скажи: «Бисмилляхи аввалаху ва ахираху» — С именем Аллаха в начале и в конце.", "adam", ("#C9734F", "#F6E0D3")),
 ("after", "После еды", "الْحَمْدُ لِلَّهِ الَّذِي أَطْعَمَنِي هَذَا وَرَزَقَنِيهِ مِنْ غَيْرِ حَوْلٍ مِنِّي وَلَا قُوَّةٍ",
  "Альхамду лилляхиллязи атъамани хаза ва разаканихи мин гайри хаулин минни ва ля куввах",
  "Хвала Аллаху, Который накормил меня этим и дал мне это без всякой силы и мощи с моей стороны.", "А можно коротко: «Альхамдулиллях»!", "maryam", ("#C76A86", "#F6DCE4")),
 ("adhan", "После азана", "اللَّهُمَّ رَبَّ هَذِهِ الدَّعْوَةِ التَّامَّةِ، وَالصَّلَاةِ الْقَائِمَةِ، آتِ مُحَمَّدًا الْوَسِيلَةَ وَالْفَضِيلَةَ، وَابْعَثْهُ مَقَامًا مَحْمُودًا الَّذِي وَعَدْتَهُ",
  "Аллахумма рабба хазихид-дааватит-таммати, вас-салятиль-каимати, ати Мухаммаданиль-василяти валь-фадыля, вабъасху макамам-махмуданиллязи ваадтах",
  "О Аллах, Господь этого совершенного призыва и наступающей молитвы! Даруй Мухаммаду ﷺ высокую степень и достоинство и вознеси его на славное место, которое Ты ему обещал.", "Пока звучит азан — слушаем и повторяем за муэдзином.", "adam", ("#3C7FB0", "#D8E8F3")),
 ("quran", "Перед чтением Корана", "أَعُوذُ بِاللَّهِ مِنَ الشَّيْطَانِ الرَّجِيمِ", "Аузу билляхи минаш-шайтанир-раджим",
  "Прибегаю к защите Аллаха от проклятого шайтана.", "Потом говорим «Бисмилляхир-Рахманир-Рахим» и читаем.", "maryam", ("#5E7F4E", "#DCE8D2")),
 ("sleep", "Перед сном", "بِاسْمِكَ اللَّهُمَّ أَمُوتُ وَأَحْيَا", "Бисмика-ллахумма амуту ва ахья",
  "С Твоим именем, о Аллах, я засыпаю и просыпаюсь.", "Ложимся на правый бочок — как Пророк ﷺ.", "adam", ("#4B3A8C", "#E3DDF3")),
 ("wake", "Когда проснулся", "الْحَمْدُ لِلَّهِ الَّذِي أَحْيَانَا بَعْدَ مَا أَمَاتَنَا وَإِلَيْهِ النُّشُورُ", "Альхамду лилляхиллязи ахьяна бадама аматана ва иляйхин-нушур",
  "Хвала Аллаху, Который пробудил нас после сна, и к Нему — возвращение.", "Доброе утро! Новый день — новый подарок от Аллаха.", "maryam", ("#B8914A", "#F5E8CC")),
 ("out", "Выходя из дома", "بِسْمِ اللَّهِ، تَوَكَّلْتُ عَلَى اللَّهِ، وَلَا حَوْلَ وَلَا قُوَّةَ إِلَّا بِاللَّهِ", "Бисмиллях, таваккальту аля-ллах, ва ля хауля ва ля куввата илля биллях",
  "С именем Аллаха, я уповаю на Аллаха, и нет силы и мощи ни у кого, кроме Аллаха.", "Аллах бережёт нас везде!", "adam", ("#3F8F86", "#D6ECE8")),
 ("home", "Входя домой", "بِسْمِ اللَّهِ وَلَجْنَا، وَبِسْمِ اللَّهِ خَرَجْنَا، وَعَلَى اللَّهِ رَبِّنَا تَوَكَّلْنَا", "Бисмилляхи валяджна, ва бисмилляхи хараджна, ва аля-ллахи раббина таваккальна",
  "С именем Аллаха мы вошли, с именем Аллаха вышли, и на Аллаха, нашего Господа, мы уповаем.", "И не забудь сказать дома «Ассаляму алейкум»!", "maryam", ("#A8473B", "#F6E1D8")),
 ("study", "Перед учёбой", "رَبِّ زِدْنِي عِلْمًا", "Рабби зидни ильма", "Господи, прибавь мне знаний.", "Это дуа из Корана — просим полезных знаний.", "adam", ("#6F86C2", "#E4EAF6")),
 ("parents", "За маму и папу", "رَبِّ ارْحَمْهُمَا كَمَا رَبَّيَانِي صَغِيرًا", "Раббир-хамхума кама раббаяни сагира",
  "Господи, помилуй их, как они растили меня маленьким.", "Это дуа из Корана. Скажи его и обними родителей!", "maryam", ("#C76A86", "#FBEEF1")),
 ("parents", "За маму и папу · 2", "رَبَّنَا اغْفِرْ لِي وَلِوَالِدَيَّ وَلِلْمُؤْمِنِينَ يَوْمَ يَقُومُ الْحِسَابُ",
  "Раббана-гфир ли ва ли-валидаййа ва лиль-муминина йаума якумуль-хисаб",
  "Господь наш, прости меня, моих родителей и всех верующих в тот День, когда будет расчёт.", "Так просил Аллаха пророк Ибрахим. Это дуа из Корана.", "adam", ("#C9734F", "#F6E0D3")),
 ("parents", "За маму и папу · 3", "رَبِّ اغْفِرْ لِي وَلِوَالِدَيَّ", "Раббиг-фир ли ва ли-валидаййа",
  "Господи, прости меня и моих родителей.", "Короткое дуа пророка Нуха из Корана — его легко выучить!", "maryam", ("#E9A0B8", "#FBEEF1")),
 ("sneeze", "Когда чихнул", "الْحَمْدُ لِلَّهِ", "Альхамдулиллях", "Хвала Аллаху.",
  "Тебе скажут: «Ярхамука-ллах» (Да помилует тебя Аллах), а ты ответь: «Яхдикуму-ллаху ва юслиху бялякум» (Да наставит вас Аллах и улучшит ваше состояние).", "adam", ("#8C6BB8", "#EADFF5")),
 ("wc", "Перед туалетом", "بِسْمِ اللَّهِ، اللَّهُمَّ إِنِّي أَعُوذُ بِكَ مِنَ الْخُبُثِ وَالْخَبَائِثِ", "Бисмиллях, Аллахумма инни аузу бика миналь-хубуси валь-хабаис",
  "С именем Аллаха. О Аллах, я прибегаю к Тебе от всякого зла и вредных существ.", "Входим с левой ноги. Выходя, говорим «Гуфранака» — Прошу Твоего прощения.", "maryam", ("#5E7F4E", "#E4EDDC")),
]

DUAS += [
 ("mosque", "Входя в мечеть", "اللَّهُمَّ افْتَحْ لِي أَبْوَابَ رَحْمَتِكَ", "Аллахумма-фтах ли абваба рахматик",
  "О Аллах, открой для меня врата Твоей милости.", "Входим с правой ноги и говорим «Ассаляму алейкум».", "adam", ("#5E7F4E", "#DCE8D2")),
 ("mosque_out", "Выходя из мечети", "اللَّهُمَّ إِنِّي أَسْأَلُكَ مِنْ فَضْلِكَ", "Аллахумма инни ас-алюка мин фадлик",
  "О Аллах, я прошу у Тебя Твоей щедрости.", "Выходим с левой ноги.", "maryam", ("#3C7FB0", "#D8E8F3")),
 ("clothes", "Надевая одежду", "الْحَمْدُ لِلَّهِ الَّذِي كَسَانِي هَذَا وَرَزَقَنِيهِ مِنْ غَيْرِ حَوْلٍ مِنِّي وَلَا قُوَّةٍ",
  "Альхамду лилляхиллязи касани хаза ва разаканихи мин гайри хаулин минни ва ля куввах",
  "Хвала Аллаху, Который одел меня в это и дал мне это без всякой силы и мощи с моей стороны.", "Одеваемся с правой стороны — сначала правый рукав!", "adam", ("#C9734F", "#F6E0D3")),
 ("mirror", "Глядя в зеркало", "اللَّهُمَّ أَنْتَ حَسَّنْتَ خَلْقِي فَحَسِّنْ خُلُقِي", "Аллахумма анта хассанта хальки фа хассин хулюки",
  "О Аллах, Ты сделал красивой мою внешность — сделай красивым и мой характер.", "Самая лучшая красота — доброе сердце!", "maryam", ("#8C6BB8", "#EADFF5")),
 ("rain", "Когда идёт дождь", "اللَّهُمَّ صَيِّبًا نَافِعًا", "Аллахумма саййибан нафиа",
  "О Аллах, пусть этот дождь будет полезным.", "Во время дождя дуа принимаются — попроси Аллаха о хорошем!", "adam", ("#6F86C2", "#E4EAF6")),
 ("car", "В дороге", "سُبْحَانَ الَّذِي سَخَّرَ لَنَا هَذَا وَمَا كُنَّا لَهُ مُقْرِنِينَ، وَإِنَّا إِلَى رَبِّنَا لَمُنْقَلِبُونَ",
  "Субханаллязи саххара ляна хаза ва ма кунна ляху мукринин, ва инна иля раббина ля мункалибун",
  "Пречист Тот, Кто подчинил нам это, а мы сами не смогли бы, и к нашему Господу мы вернёмся.", "Это дуа из Корана. Говорим, садясь в машину или автобус.", "maryam", ("#A8473B", "#F6E1D8")),
 ("hard", "Когда трудно", "لَا حَوْلَ وَلَا قُوَّةَ إِلَّا بِاللَّهِ", "Ля хауля ва ля куввата илля биллях",
  "Нет силы и мощи ни у кого, кроме Аллаха.", "Аллах поможет тебе справиться!", "adam", ("#5E7F4E", "#E4EDDC")),
 ("yunus", "Когда грустно или страшно", "لَا إِلَهَ إِلَّا أَنْتَ سُبْحَانَكَ إِنِّي كُنْتُ مِنَ الظَّالِمِينَ", "Ля иляха илля анта субханака инни кунту миназ-залимин",
  "Нет божества, кроме Тебя, Ты пречист, а я был из ошибающихся.", "Так молился пророк Юнус в животе у кита — и Аллах спас его!", "maryam", ("#3F8F86", "#D6ECE8")),
 ("nice", "Когда что-то понравилось", "مَا شَاءَ اللَّهُ، تَبَارَكَ اللَّهُ", "Ма ша-аллах, табарак-аллах",
  "Так пожелал Аллах. Благословен Аллах.", "Хвалим не только вещь, но и Того, Кто её создал!", "adam", ("#C76A86", "#F6DCE4")),
 ("thanks", "Когда благодарим", "جَزَاكَ اللَّهُ خَيْرًا", "Джазака-ллаху хайран",
  "Пусть Аллах вознаградит тебя добром.", "Девочке говорим: «Джазаки-ллаху хайран».", "maryam", ("#B8914A", "#F5E8CC")),
 ("salam", "Когда встречаемся", "السَّلَامُ عَلَيْكُمْ وَرَحْمَةُ اللَّهِ وَبَرَكَاتُهُ", "Ассаляму алейкум ва рахмату-ллахи ва баракатух",
  "Мир вам, милость Аллаха и Его благословение.", "Отвечаем: «Ва алейкум ассалям ва рахмату-ллахи ва баракатух».", "adam", ("#4B3A8C", "#E3DDF3")),
 ("istighfar", "Когда ошибся", "أَسْتَغْفِرُ اللَّهَ", "Астагфируллах",
  "Прошу прощения у Аллаха.", "Ошибаются все. Главное — попросить прощения и исправиться!", "maryam", ("#6F86C2", "#E4EAF6")),
]

def card(d):
    key, title, ar, tr, ru, note, who, (dark, light) = d
    size = 30 if len(ar) < 40 else (24 if len(ar) < 80 else 19)
    kid = adam(62, right="wave") if who == "adam" else maryam(62, left="wave")
    return (f'<div class="dc"><div class="dc-in" style="--dd:{dark};--dl:{light}">'
            f'<div class="dc-top"><div class="dc-ico">{ICONS[key]}</div><b>{title}</b></div>'
            f'<div class="dc-ar" lang="ar" dir="rtl" style="font-size:{size}px">{ar}</div>'
            f'<div class="dc-tr">{tr}</div><div class="dc-ru">{ru}</div>'
            f'<div class="dc-note">{kid}<span>{note}</span></div></div></div>')

def build():
    lib.KIDNOTES = [("maryam", "Каждое дуа — маленький разговор с Аллахом.")]
    b = Book()
    b.pages.append(f'''<section class="page cover-min">
<div class="cm-frame"></div>
<div class="cm-in">
<svg class="cm-moon" viewBox="0 0 60 60"><circle cx="28" cy="30" r="20" fill="#D8B26A"/><circle cx="37" cy="25" r="17" fill="#FBF6F0"/>{star(46, 44, 5, "#D8B26A")}</svg>
<div class="cm-ar" lang="ar" dir="rtl">أَدْعِيَتِي الصَّغِيرَةُ</div>
<div class="cm-line"></div>
<div class="cm-ru">Мои первые дуа</div>
<div class="cm-sub">Карточки для детей</div>
<div class="cm-stage">{M.CM_arch()}<div class="cm-kids">{adam(150, right="wave", mood="open")}{maryam(150, left="wave", mood="open")}</div></div>
</div></section>''')
    b.add(f'''<h1 class="title sm">Как играть с карточками</h1>
<div class="soft-card">
<p><b>Дуа</b> — это когда мы просим Аллаха или благодарим Его своими словами. Пророк Мухаммад ﷺ учил нас говорить особые дуа в течение всего дня: перед едой, перед сном, выходя из дома…</p>
<p>Вырежьте карточки и положите там, где они нужны: «перед едой» — на кухне, «перед сном» — у кровати, «выходя из дома» — у двери. Так ребёнок будет видеть дуа каждый день и выучит его незаметно.</p>
<p>Учите по одному дуа в неделю. Говорите его вместе вслух — а когда малыш скажет сам, отметьте звёздочку в таблице в конце.</p></div>
<div class="pair">{adam(150, right="wave", mood="open")}{maryam(150, left="wave", mood="open")}</div>''', section=("أَدْعِيَتِي", "Мои первые дуа", ("#B8914A", "#F5E8CC")))
    for p in range((len(DUAS) + 3) // 4):
        chunk = DUAS[p*4:(p+1)*4]
        cards = "".join(card(d) for d in chunk)
        cards += "".join(f'<div class="dc"><div class="dc-in blank" style="--dd:#D8B26A;--dl:#F5E8CC"><div class="dc-top"><div class="dc-ico">{ICONS["istighfar"]}</div><b>Моё дуа</b></div><p class="dc-ru">Напиши или нарисуй своё дуа — о чём ты хочешь попросить Аллаха?</p><div class="dc-lines"><i></i><i></i><i></i><i></i></div><div class="dc-note">{maryam(62, left="wave")}<span>Аллах слышит каждое дуа — даже тихое!</span></div></div></div>' for _ in range(4 - len(chunk)))
        b.pages.append(f'<section class="page cutpage dsheet"><div class="dcards">{cards}</div></section>')
    rows = "".join(f'<div class="tk"><div class="tk-i">{ICONS[d[0]]}</div><b>{d[1]}</b>' + "".join(f'<svg viewBox="0 0 40 40">{star(20, 21, 17, "#fff", stroke="#D8B26A")}</svg>' for _ in range(5)) + '</div>' for d in DUAS)
    rl = rows.split('</div><div class="tk">')
    rows_all = [r if r.startswith('<div class="tk">') else '<div class="tk">' + r for r in rl]
    rows_all = [r if r.endswith('</div>') else r + '</div>' for r in rows_all]
    for k in range(2):
        b.add(f'''<h1 class="title sm">Я учу дуа! ({k+1}/2)</h1>
<p class="lead">Каждый раз, когда ты сам сказал дуа, закрась звёздочку. Пять звёздочек — и дуа выучено!</p>
<div class="tks">{"".join(rows_all[k*13:(k+1)*13])}</div>''', section=("أَدْعِيَتِي", "Мои первые дуа", ("#B8914A", "#F5E8CC")))
    b.pages.append(f'''<section class="page about-min"><div class="am-in mt-end">
<div class="am-t">Мои первые дуа</div>
<div class="am-line"></div>
<p class="mt-p">Пусть каждое дуа, сказанное маленьким сердцем, станет светом для него и для его семьи.</p>
<div class="mt-kids">{adam(110, right="wave")}{maryam(110, left="wave")}</div>
<p class="mt-p" style="font-size:13px">Подготовила</p>
<div class="mt-name">Эльмаза Темиркалиева</div>
<div class="wa"><span lang="ar" dir="rtl">وَاللَّهُ أَعْلَمُ</span>Аллах знает лучше. Если мы где-то ошиблись — это от нас, а всё верное — от Аллаха.</div>
<div class="bc-y mt-y">2026</div></div></section>''')
    return b

CSS = """
.dsheet .dcards{position:absolute;inset:6mm;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;border-top:1.2px dashed #9C8478;border-left:1.2px dashed #9C8478}
.dc{border-right:1.2px dashed #9C8478;border-bottom:1.2px dashed #9C8478;padding:4mm}
.dc-in{height:100%;border-radius:6mm;background:linear-gradient(180deg,var(--dl) 0%,#FFFDF9 38%,#FFFDF9 100%);border:1.5px solid var(--dd);
  display:flex;flex-direction:column;align-items:center;text-align:center;padding:4mm 5mm;gap:2mm;position:relative}
.dc-top{display:flex;flex-direction:column;align-items:center;gap:1mm}
.dc-ico{width:24mm;height:24mm;background:#fff;border-radius:50%;border:1.5px solid var(--dd);display:grid;place-items:center}
.dic{width:17mm;height:17mm}
.dc-top b{font-weight:900;font-size:17px;color:var(--dd)}
.dc-ar{font-family:"Amiri";font-weight:700;line-height:1.85;color:#2E1A16;flex:1;display:flex;align-items:center;justify-content:center}
.dc-tr{font-size:11.5px;font-weight:700;color:var(--dd);line-height:1.45}
.dc-ru{font-size:11px;font-style:italic;color:#5C342E;line-height:1.45}
.dc-note{display:flex;align-items:center;gap:2mm;text-align:left;border-top:1px dashed #E6D8C6;padding-top:2mm;width:100%}
.dc-note .char{flex:none;width:12mm;height:auto}
.dc-note span{font-size:10px;line-height:1.4;color:#7A5A52}
.dc-lines{flex:1;width:100%;display:flex;flex-direction:column;justify-content:space-around}.dc-lines i{border-bottom:1.5px dashed #DCC08A;height:6mm}
.tks{display:flex;flex-direction:column;gap:1.4mm}
.tk{display:grid;grid-template-columns:12mm 1fr repeat(5,10mm);gap:2mm;align-items:center;background:#FFFDF9;border:1px solid #E6D8C6;border-radius:4mm;padding:.6mm 4mm}
.tk-i .dic{width:10mm;height:10mm}.tk b{font-size:14px;color:#5C342E}
.tk svg{width:8mm;height:8mm}
"""

if __name__ == "__main__":
    b = build()
    css = "".join((ROOT / f).read_text(encoding="utf-8") for f in ["style.css", "style2.css", "style3.css"]) + F.CSS + CM.CSS + E.CSS + (ROOT / "style4.css").read_text(encoding="utf-8") + M.CSS + CSS
    (ROOT / "duas.html").write_text(f'<!doctype html><html lang="ru"><head><meta charset="utf-8"><title>Мои первые дуа</title><style>{css}</style></head><body>{"".join(b.pages)}</body></html>', encoding="utf-8")
    print("pages", len(b.pages))
