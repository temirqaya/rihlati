"""Турецкий слой для разделов 2–9. Ключи — из ct2 (русские), значения — по-турецки, в том же порядке."""
import re
import ct2

NAMES = {'ا': 'Elif', 'ب': 'Be', 'ت': 'Te', 'ث': 'Se', 'ج': 'Cim', 'ح': 'Ha', 'خ': 'Ho', 'د': 'Dal', 'ذ': 'Zel', 'ر': 'Ra', 'ز': 'Ze',
         'س': 'Sin', 'ش': 'Şın', 'ص': 'Sad', 'ض': 'Dad', 'ط': 'Ta', 'ظ': 'Za', 'ع': 'Ayn', 'غ': 'Ğayn', 'ف': 'Fe', 'ق': 'Kaf', 'ك': 'Kef',
         'ل': 'Lam', 'م': 'Mim', 'ن': 'Nun', 'ه': 'He', 'و': 'Vav', 'ي': 'Ye'}

SETS_JS = r'''
(function(){
 Object.assign(TRL, {'ب':'b','ت':'t','ج':'c','د':'d','ر':'r','ف':'f','ل':'l','م':'m','ن':'n','ك':'k','ش':'ş'});
 HV[0].v='a'; HV[1].v='i'; HV[2].v='u';
 const h = SETS.h, t = SETS.t, m = SETS.m;
 const HN = ['Fetha','Kesra','Damme'];
 HV[0].name='Fetha'; HV[1].name='Kesra'; HV[2].name='Damme';
 h.sec='Harekeler'; h.hat='Harekeyi'; h.hats='harekeyi';
 h.V[0].name='Fetha'; h.V[0].v='a'; h.V[0].where='<b>üstünde</b> küçük bir çizgi'; h.V[0].mouth='Ağzımızı geniş açarız';
 h.V[1].name='Kesra'; h.V[1].v='i'; h.V[1].where='<b>altında</b> küçük bir çizgi'; h.V[1].mouth='Dudaklarımızın kenarı gülümser';
 h.V[2].name='Damme'; h.V[2].v='u'; h.V[2].where='<b>üstünde</b> küçük bir kıvrım'; h.V[2].mouth='Dudaklarımız boru gibi toplanır';
 ['Fetha','Kesra','Damme','Hepsi bir arada'].forEach((x,i)=>h.lessons[i].title=x);
 h.greet = k => k===0 ? 'Harfler sihirli şapkalar giyiyor! İlk şapka — Fetha.' : k<3 ? `${HN[k-1]} şapkasını biliyoruz. Bugün yeni şapka — ${HN[k]}!` : 'Bugün üç şapkayı bir araya toplayıp çarkı çevireceğiz!';
 h.baseText='Bu, Be harfi. Tek başına sadece «b» der. Ona bir şapka giydirelim!'; h.btn='Şapka giydir';
 h.note = v => `${v.mouth}. Kısa okuruz, tek hareke: «b${v.v}», «b${v.v}-${v.v}-${v.v}» değil.`;
 h.readHint='Sağdan sola, kısa ve net okuruz. Heceye dokun — zıplayacak!'; h.threeTitle='Üç sihirli şapka'; h.wheelTitle='Hareke çarkı';
 const TN = ['Fethatan','Kesratan','Dammetan'];
 t.sec='Tenvin'; t.hat='Tenvini'; t.hats='tenvini';
 t.snd = (l,k) => TRL[l] + ['an','in','un'][k];
 TN.forEach((x,i)=>t.V[i].name=x); ['an','in','un'].forEach((x,i)=>t.V[i].v=x);
 t.V[0].where='<b>üstünde</b> iki çizgi ve sonunda elif'; t.V[0].mouth='Devam ederek okurken tenvinden sonraki elif okunmaz';
 t.V[1].where='<b>altında</b> iki çizgi'; t.V[1].mouth='Gülümseriz ve «n» ekleriz';
 t.V[2].where='<b>üstünde</b> çift kıvrım'; t.V[2].mouth='Dudaklar boru gibi ve «n» ekleriz';
 [...TN,'Hepsi bir arada'].forEach((x,i)=>t.lessons[i].title=x);
 t.greet = k => k===0 ? 'Şapka iki olursa ne olur? Bir «n» yankısı çıkar! Bu, tenvin.' : k<3 ? `${TN[k-1]}ı biliyoruz. Bugün — ${TN[k]}!` : 'Bugün üç tenvini bir araya toplayıp çarkı çevireceğiz!';
 t.baseText='Bu hecede bir şapka var. Ya iki olursa?'; t.btn='Şapkayı ikile';
 t.note = v => `${v.mouth}. Tenvin bir yankı gibidir: «b${v.v}».`;
 t.readHint='Sağdan sola okuruz: her hecenin sonunda hafif bir «n» duyulur.'; t.threeTitle='Üç tenvin'; t.wheelTitle='Tenvin çarkı';
 const MN = ['Elifle med','Ye ile med','Vav ile med'];
 m.sec='Med'; m.hat='Meddi'; m.hats='meddi';
 m.snd = (l,k) => TRL[l] + ['a-a','i-i','u-u'][k];
 MN.forEach((x,i)=>m.V[i].name=x); ['a-a','i-i','u-u'].forEach((x,i)=>m.V[i].v=x);
 m.V[0].where='fetha, ardından <b>elif</b>'; m.V[0].mouth='«a»yı 2 hareke uzatırız — iki adım';
 m.V[1].where='kesra, ardından <b>ye</b>'; m.V[1].mouth='«i»yi 2 hareke uzatırız — iki adım';
 m.V[2].where='damme, ardından <b>vav</b>'; m.V[2].mouth='«u»yu 2 hareke uzatırız — iki adım';
 ['Elifle','Ye ile','Vav ile','Hepsi bir arada'].forEach((x,i)=>m.lessons[i].title=x);
 m.greet = k => k===0 ? 'Sesler kısa da olur, uzun da! Bugün «a» sesini uzatmayı öğreniyoruz.' : k<3 ? `«${['a','i'][k-1]}» sesini uzatmayı biliyoruz. Bugün «${['','i','u'][k]}» sesini uzatıyoruz!` : 'Bugün bütün uzun sesleri bir araya topluyoruz!';
 m.baseText='Bu kısa bir hece — tek adım. Ya ardından bir med harfi gelirse?'; m.btn='Med harfini ekle';
 m.note = v => `${v.mouth}: «b${v.v}». Kısa ses — bir adım, uzun ses — iki adım!`;
 m.readHint='Sağdan sola okuruz ve her sesi tam 2 hareke uzatırız.'; m.threeTitle='Üç uzun ses'; m.wheelTitle='Med çarkı';
 SKL[0].t='Cezm'; SKL[1].t='Şedde';
})();
'''

# дополнительные замены (применяются первыми): звуки на латинице
PRE = [
 ('Следующая буква →', 'Sonraki harf →'),
 ('<span class="hc-s">«б${v.v}»</span>', '<span class="hc-s">«b${v.v}»</span>'),
 ("'«б'+v.v+'»'", "'«b'+v.v+'»'"),
 ('<div class="bubble">Ассаляму алейкум!</div>', '<div class="bubble">Esselâmü aleyküm!</div>'),
 ('<button class="btn" id="say">Скажем вместе: «б${V.v}!»</button>', '<button class="btn" id="say">Hep birlikte: «b${V.v}!»</button>'),
 ('<button class="btn" id="say">Скажем вместе: «аб!»</button>', '<button class="btn" id="say">Hep birlikte: «ab!»</button>'),
 ('<button class="btn" id="say">Скажем вместе: «абба!»</button>', '<button class="btn" id="say">Hep birlikte: «abba!»</button>'),
 ("const shdSnd = (l, v) => 'а' + TRL[l] + TRL[l] + HV[v].v;", "const shdSnd = (l, v) => 'a' + TRL[l] + TRL[l] + HV[v].v;"),
]

JS_V = [
 "<span>${V.where} — <b>«${V.v}»</b> sesi</span>",
 "`${C.sec} ${i+1} / 4 · ${H.title}`",
 "Düğmeye bas — hece yeni bir sesle konuşacak!",
 "Her karta dokun ve oku: ",
 "Çarkı çevir! Çıkan harfi üç şekilde oku.",
 ">Çarkı çevir</button><span class=\"count\">Çevrildi: <b id=\"spinN\">0</b> / 5</span>",
 "Heceyi çiz: önce harfi, sonra işaretleri!",
 "<h2>${C.hat} yakala!</h2>",
 "Bu hece nasıl okunur? Yüksek sesle söyleyin, sonra kontrol edelim.",
 "`Artık biliyorsun: ${V.name}!` : `Üç ${C.hats} de biliyorsun!`",
 "'Sonraki ders — '+C.lessons[i+1].title+'. Görüşmek üzere, inşallah!' : 'Yakında yeni dersler, inşallah!'",
 "`<button class=\"btn sage\" id=\"nextLetter\">İleri: ${C.lessons[i+1].title} →</button>`",
 "CLEAD = `Sadece <b>${v.name}</b> <span class=\"hsvg-in\">${v.svg}</span> olan balonları patlat — «${v.v}» sesi`;",
 "$('#meetText').textContent = 'İşte! Oldu:'; $('#meetBubble').textContent = 'Heceye dokun — zıplayacak!';",
 "`«b${C.V[hk].v}»! Maşallah, ne kadar güzel!`",
 "`${hpage+1} / ${readPages()}`",
 "hpage < readPages()-1 ? 'İleri' : 'Okuduk!'",
 "`<b>${V.name}</b> nerede? Bu, ${V.where}.`",
 "`Bu «${C.snd(l,k)}», ${C.V[k].name}. Bir daha dene!` : `Bu <b>${C.V[k].name}</b>: ${C.V[k].where}. Bir daha dene!`",
 # sk.js
 "`Cezm ve şedde ${i+1} / 2 · ${T.t}`",
 "'Bugün harfin nasıl uyuduğunu öğreneceğiz!' : 'Bugün ikiz harfle tanışacağız!'",
 "Be harfinin üstündeki küçük yuvarlağı gördün mü? Bu, <b>cezm</b>. Onunla harf uyur: kendi harekesi yoktur.",
 "Heceye yapıştır",
 "<b>Üstte</b> yuvarlak — harf uyur, onu önceki heceyle birlikte okuruz: <b>«ab»</b>",
 "Cezm küçük bir yastık gibidir: harf onun üstünde uyur! Kısa ve net okuruz.",
 "Düğmeye bas — uyuyan harf heceye yapışacak.",
 "Bir Be uyuyor, öbürü «ba» diyor. Onları birleştirirsek?",
 "İkizleri birleştir",
 "<div class=\"name\">Şedde <span class=\"arn\">",
 "İşaret küçük bir «w» gibi — harf <b>iki kez</b> duyulur: <b>«abba»</b>",
 "Şedde ikiz harftir: ilk yarısı uyur, ikincisi harekesiyle okunur. Özel ikizler <span class=\"arin sm\">نّ</span> ve <span class=\"arin sm\">مّ</span> burundan 2 hareke uzatılır — bu, gunne.",
 "Düğmeye bas — harfler ikiz olacak.",
 "'Sağdan sola okuruz: «ab — ib — ub». Son harf uyuyor.' : 'Okuruz: «abba — abbi — abbu». Harf iki kez duyulur.'",
 "'Heceyi çiz, cezm yuvarlağını unutma!' : 'Heceyi çiz: hem şeddeyi hem harekeyi!'",
 "'Uyuyan harfi bul!' : 'İkizi yakala!'",
 "'Artık cezmi biliyorsun — uyuyan harf!' : 'Artık şeddeyi biliyorsun — ikiz harf!'",
 "'Sonraki ders — Şedde. Görüşmek üzere, inşallah!' : 'Yakında yeni dersler, inşallah!'",
 "'<button class=\"btn sage\" id=\"nextLetter\">İleri: Şedde →</button>'",
 "CLEAD = 'Sadece harfin <b>uyuduğu</b> balonları patlat — cezm yuvarlağıyla';",
 "CLEAD = 'Sadece <b>ikiz</b> harfli balonları patlat — şedde işaretiyle';",
 "SKi===0 ? 'İşte! Uyuyan harf yapıştı:' : 'İşte! İkiz oldu:'; $('#meetBubble').textContent = 'Heceye dokun — zıplayacak!';",
 "SKi===0 ? '«ab»! Maşallah!' : '«abba»! Maşallah, ne kadar güzel!'",
 "`${hpage+1} / ${skPages()}`",
 "hpage < skPages()-1 ? 'İleri' : 'Okuduk!'",
 "SKi===0 ? 'Harf nerede <b>uyuyor</b>? Cezmli heceyi bul.' : '<b>İkiz</b> nerede? Şeddeli heceyi bul.'",
 "SKi===0 ? 'Burada cezm yok. Bir daha dene!' : 'Burada şedde yok. Bir daha dene!'",
 "`Bu «${sn(l,+c.dataset.v)}». Bir daha dene!`",
 # p.js
 "`${PS.title.replace(/^Bölüm \\d+\\. /,'')} · ${PLs.title}`",
 "<p class=\"lead\">İstediğin harfe dokun!</p></div><div class=\"count\">Bakıldı: <b id=\"pfN${k}\">0</b> / ${s.need}</div>",
 ">Sonraki kelime</button>",
 "'Her örneği öğretmeninle birlikte oku. Karta dokun — zıplayacak!'",
 ">Okuduk!</button>",
 ">Sonraki ayet</button>",
 "'Her yıldızcık senin emeğin. Maşallah!'",
 "<div class=\"dip-t\">Diploma</div><div class=\"dip-s\">Kur'an'ın gerçek dostuna</div>",
 "Verildi: <input id=\"dipName\" type=\"text\" placeholder=\"adını yaz\"",
 "harfleri, harekeleri, cezmi, şeddeyi, tenvini, meddi ve tecvidin ilk kurallarını öğrenip Kur'an-ı Kerim'in surelerini okumaya başlayarak bütün yolculuğu tamamladığı için.",
 ">Diplomamı al!</button>",
 "`${page+1} / ${pages}`",
 "page < pages-1 ? 'İleri' : 'Okuduk!'",
 "`Soru ${n+1} / ${s.qs.length}`",
 "'Bütün sorular bitti!'",
 "'Bir daha düşün — başarabilirsin!'",
 "`Kelime ${n+1} / ${s.items.length}`",
 "'Bütün kelimeler toplandı!'",
 "'Sağdan başlıyoruz: ilk hece hangisi?'",
 "CDONE = 'kelime';",
 "'Bütün sure'; $(`#ayNext${k}`).textContent = 'Okuduk!';",
 "<small>Bismillah</small>`; $(`#ayN${k}`).textContent = ''; $(`#ayNext${k}`).textContent = 'İlk ayet';",
 "`Ayet ${n+1} / ${total}`",
 "n < total-1 ? 'Sonraki ayet' : 'Bütün sure'",
 "[['Harfler', LET.map(l=>l.ch), 'l'], ['Harekeler', [0,1,2,3].map(x=>'h'+x)], ['Cezm ve şedde', ['s0','s1']], ['Tenvin', [0,1,2,3].map(x=>'t'+x)], ['Med', [0,1,2,3].map(x=>'m'+x)],",
 "S.title.replace(/^Bölüm \\d+\\. /,'')",
 "<b>${done} / ${keys.length}</b>",
 # общие
 "Bismillah, başlayalım!",
 "Maşallah! Aferin!",
 "«Rabbim, ilmimi artır»",
 ">Bir daha</button>",
 ">Haritaya</button>",
 "İleri: ${nextT} →",
 ">← Geri</button>",
 "<h2>Hızlı bakış</h2>",
 ">Kontrol et</button>",
 ">Sonraki</button>",
 ">Sil</button>",
 ">Başka hece</button>",
 ">Tamam!</button>",
 "<span class=\"count\">Yakalanan: <b id=\"ccount\">0</b></span>",
 ">Başla!</button>",
 ">İleri</button>",
 "`Soru ${Math.min(hround+1,5)} / 5`",
 "'Doğru! Maşallah!'",
 "'5 sorunun hepsi!'",
 "`Hangi hece <b>«${C.snd(l,t)}»</b> okunur?`",
 "`Hangi hece <b>«${sn(l,t)}»</b> okunur?`",
 "'Bitir' : 'Sonraki'",
 "`${fr+1} / ${hseq.length}`",
]
assert len(JS_V) <= len(ct2.JS), (len(JS_V), len(ct2.JS))
JS = PRE + [(a, b) for (a, _), b in zip(ct2.JS[:len(JS_V)], JS_V)]

def apply_js(src):
    for a, b in JS:
        src = src.replace(a, b)
    return src

POS = {'отдельно': 'tek başına', 'в начале': 'başta', 'в середине': 'ortada', 'в конце': 'sonda'}
SUR = {'Аль-Фатиха': 'Fâtiha', 'Аль-Ихлас': 'İhlâs', 'Аль-Каусар': 'Kevser', 'Аль-Фаляк': 'Felak', 'Ан-Нас': 'Nâs', 'Аль-Аср': 'Asr'}
MEAN = {
 'Fâtiha': 'Fâtiha — «Açan». Bu surede Allah\'a — âlemlerin Rabbine, Rahmân ve Rahîm olana — hamdederiz ve O\'ndan bizi doğru yola iletmesini isteriz. Müslümanlar onu her namazda okur.',
 'İhlâs': 'İhlâs — «Samimiyet». Bu sure Allah\'ın bir olduğunu, O\'nun ne çocuğu ne de anne babası olduğunu ve hiçbir şeyin O\'na denk olmadığını anlatır.',
 'Kevser': 'Kevser — «Bolluk». Allah Peygamberimize ﷺ büyük bir nimet — cennetteki Kevser ırmağını verdi. Bunun için Allah\'a namazla şükrederiz.',
 'Felak': 'Felak — «Sabah aydınlığı». Bu surede Allah\'tan bizi her türlü kötülükten, gecenin karanlığından ve hasetten korumasını isteriz.',
 'Nâs': 'Nâs — «İnsanlar». İnsanların Rabbine, kötü düşünceler fısıldayan şeytandan sığınırız.',
 'Asr': 'Asr — «Zaman». Allah, iman eden, iyi işler yapan, birbirine hakkı ve sabrı tavsiye edenlerin kurtuluşta olduğunu bildirir.',
}
EXACT_V = [
 'Bölüm 6. Kelimede harfler', 'Dört şekil', 'Esselâmü aleyküm!',
 'Kelimede harfler el ele tutuşur — ve bu yüzden biraz değişir!',
 'Harfler el ele tutuşur', 'Bak: bunların hepsi Be harfi!', 'Harfe dokun — şekillerini gör', 'Harfi tanı',
 'Artık harfleri her şekilde tanıyorsun!', 'Sırada — harflerin elleri. Görüşmek üzere!',
 'Harflerin elleri', 'Düşün: her harfin iki eli var. Bakalım kim kimi tutuyor!',
 'Açık avuç mu, yumruk mu?', 'Kelimenin başında harf elini ileri uzatır, sonunda geri!',
 'Harfe dokun — şekillerini ellerinle göster', 'Ellerini göster!',
 'Harflerin ellerini biliyorsun!', 'Sırada — yalnız harfler. Görüşmek üzere!',
 'Yalnızlar', 'Ayrı durmayı seven altı harf var. Bil bakalım hangileri?',
 'Altı yalnız harf', 'Elif, Dal, Zel, Ra, Ze ve Vav — ayrı durmayı severler!',
 'Birleşir mi, birleşmez mi?', 'Evet', 'Hayır',
 'Yalnız harfli kelimeleri okuyoruz', 'Bak, yalnız harf «köprüyü» nerede koparıyor.',
 'Altı yalnız harfin hepsini biliyorsun!', 'Sırada kelime toplayacağız. Görüşmek üzere!',
 'Kelime topla', 'Bugün hecelerden kelimeler kuracağız, küplerden kurar gibi!',
 'Hece + hece + hece = kelime', 'Önce heceleyerek, sonra bütün olarak!',
 'Hecelere sırayla dokun — sağdan sola',
 'ketebe — yazdı', 'haleka — yarattı', 'nasara — yardım etti',
 'ceale — yaptı', 'fetaha — açtı', 'zehebe — gitti',
 'Kelimeleri gerçek bir usta gibi kuruyorsun!', 'Sırada — ilk kelimeler. Görüşmek üzere!',
 'İlk kelimeler', 'Bugün gerçek Arapça kelimeler okuyacaksın!',
 'İlk kelimeleri okuyoruz', 'Yavaş oku. Kelimeye dokun — ne demek olduğunu göreceksin.',
 'kalem', 'kapı', 'nur', 'ev', 'güneş', 'ay', 'dağ', 'erkek çocuk',
 'kitap', 'mescit', 'işitti', 'yazdı', 'Kelimeyi bul',
 '<b>Med</b> (uzun ses) olan kelimeyi bul.',
 'كِتَابٌ kelimesinde fethadan sonra elif var — «tâ» diye uzatırız.',
 '<b>Cezm</b> olan kelimeyi bul.', 'شَمْسٌ kelimesinde Mim harfi uyuyor.',
 '<b>Tenvinsiz</b> kelimeyi bul.', 'كَتَبَ kelimesinin sonunda tek bir fetha var.',
 '<span class="arin">نُورٌ</span> kelimesi nasıl okunur?',
 'Dammeli nun ve med vavı — «nû», sonunda dammetan «run».',
 '<span class="arin">شَمْسٌ</span> ne demek?', 'شَمْسٌ — güneş.',
 '«Mescit» kelimesini bul.', 'مَسْجِدٌ — mescit.',
 'Medli kelimeleri yakala!', 'Sadece sesi uzayan kelimeleri patlat: med elifi, vavı ya da yesi olan',
 'Maşallah! Kelime okuyorsun!', 'Sırada — tecvidin ilk kuralları. Görüşmek üzere!',
 'Bölüm 7. Tecvidin ilk kuralları', 'Mahreç',
 'Her harfin ağızda kendi evciği var. Hadi misafirliğe gidelim!',
 'Sesler nereden çıkar?', 'Dudaklar, dil, boğaz — her harfin kendi evciği var!',
 'Harfin evciğini bul', 'Boğaz', 'Dil', 'Dudaklar',
 'Harflerin nerede yaşadığını biliyorsun!', 'Sırada — harflerin karakteri. Görüşmek üzere!',
 'Kalın harfler', 'İnsanlar gibi harflerin de karakteri var! Kalın harfler ve ince harfler var.',
 'Kalın harfler «dolu ağızla» duyulur!', 'İnce mi, kalın mı — farkı hisset',
 'Çiftleri oku: önce inceyi, sonra kalını.', 'Kalın mı, ince mi?',
 'Kalın', 'İnce', 'Kalın ve ince harfleri ayırt ediyorsun!',
 'Sırada — cezmli nun. Görüşmek üzere!', 'Cezmli nun',
 'Cezmli nun hünerli bir harftir: farklı farklı okunur!', 'Nunun dört kuralı',
 'Önce nundan sonraki harfe bak — o sana kuralı söyler!', 'Kur\'an\'dan örnekler',
 'izhar', 'gunneli idgam', 'gunnesiz idgam', 'iklâb', 'ihfâ',
 'Trafik ışığı: hangi kural?', 'İzhar', 'İdgam', 'İklâb', 'İhfâ',
 'Zeynep\'e yardım et: ayetteki kural', 'Nunun dört kuralını da biliyorsun!',
 'Sırada — cezmli mim. Görüşmek üzere!', 'Cezmli mim',
 'Cezmli mimin sadece üç kuralı var — ezberlemesi kolay!', 'Mimin üç kuralı',
 'Be — gizleriz, Mim — birleştiririz, diğerleri — açık!', 'ihfâ-i şefevî', 'idgam',
 'Mimin kuralı hangisi?', 'İhfâ-i şefevî', 'İzhar-ı şefevî',
 'Be\'den önce — gunneli ihfâ-i şefevî.', 'Mim\'den önce — gunneli idgam.',
 'Diğer harflerden önce — izhar: «m» açık okunur.', 'Vav\'dan önce — izhar, özellikle dikkat!',
 'Fe\'den önce — izhar, özellikle dikkat!', 'Be\'den önce — ihfâ-i şefevî.',
 'Mimin kurallarını biliyorsun!', 'Sırada — kalkale, top gibi zıplayan harfler. Görüşmek üzere!',
 'Kalkale', 'Top gibi zıplayan beş harf var!', 'Kalkale — yankı',
 'Kalkale bir top gibidir: harf zıplar!',
 'Harf uyur ama biraz zıplar.', 'ortada', 'durakta', 'Kalkale nerede?',
 'Hangi hecede <b>kalkale</b> (yankı) var?', 'Kalkale — cezmli ق ط ب ج د harflerinde.',
 'Zıplayan harfleri duyuyorsun!', 'Sırada — uzun med. Görüşmek üzere!',
 'Uzun med', 'Bazen ses iki harekeden uzun çekilir. Ne zaman olduğunu öğrenelim!',
 'Ne kadar uzatmalı?', '2 hareke', '4–5 hareke', '6 hareke',
 'Tabiî med — 2 hareke.', 'Muttasıl med — 4–5 hareke.', 'Lâzım med — 6 hareke.',
 'Sesleri ne kadar uzatacağını biliyorsun!', 'Sırada — nerede durabileceğimiz. Görüşmek üzere!',
 'Vakf (durak)', 'Kur\'an okurken dinlenip nefes alabiliriz. Nerede olduğunu öğrenelim!',
 'Rakamlı yuvarlakta dinlenebilirsin!', 'İşaret ne demek?',
 'Mutlaka durulur', 'Durulmaz', 'Devam etmek daha iyi',
 'İkisi de olur', 'Durmak daha iyi', 'Durak işaretlerini biliyorsun!',
 'Artık sureleri okuyabiliriz!', 'Bölüm 8. Kur\'an okuyoruz', 'Kur\'an\'ı nasıl okuruz',
 'Hadi birlikte okuyalım!', 'Kelime kelime okuyoruz', 'Her kelimeyi yavaşça, öğretmeninle birlikte oku.',
 'Bu sure ne anlatıyor?', 'Bu sureyi her gün oku — Allah Kur\'an okumamızı sever!',
 'Onu öğretmeninle tekrarla — o artık senin olacak!',
 'Bölüm 9. Ben Kur\'an\'ın dostuyum', 'Kontrol', 'Uzun bir yol geldin! Hadi neler bildiğini kontrol edelim.',
 'Harfleri söyle', 'Heceleri oku', 'Tecvid kuralları', 'Maşallah! Harika iş çıkardın!',
 'Şimdi de — diploman!', 'Diplomam', 'Sen Kur\'an\'ın gerçek dostusun! Yıldızlarına bak.',
 'Bârekallâhu fîk!', 'Her gün Kur\'an okumaya devam et, inşallah!',
 'Başarılarım', 'Med kuralları', 'Durak kuralları', 'Yankıyla okuyoruz',
] + [SUR[k] for k in SUR] + [POS[k] for k in ['отдельно', 'в начале', 'в конце']]
assert len(EXACT_V) == len(ct2.EXACT), (len(EXACT_V), len(ct2.EXACT))
EXACT = dict(zip(ct2.EXACT.keys(), EXACT_V))

FRAG_V = [
 'Her harfin <b>dört şekli</b> olabilir: tek başına, kelimenin başında, ortasında ve sonunda. Harfi noktaları ve ana gövdesi tanıtır.',
 '<span>tek başına</span><span>başta</span><span>ortada</span><span>sonda</span>',
 '<b>açık avuç</b><small>harf komşusunu tutar — birleşir</small>',
 '<b>yumruk</b><small>tutmaz — birleşmez</small>',
 'Sağ el <b>önceki</b> harfe, sol el <b>sonraki</b> harfe bakar. Sağdan sola okuruz!',
 'Bu harfler sadece <b>önlerindeki</b> harfin elinden tutar. Sonraki harfle <b>birleşmezler</b> — onlardan sonra kelime yeni bir «elle» devam eder.',
 'Önce heceleyerek okuruz: «ke-te-be». Sonra hızlıca: «ketebe» — «yazdı».',
 'Sesin çıktığı yere <b>mahreç</b> denir. 5 ana yer vardır:',
 '<b>Ağız boşluğu</b>', '<small>med harfleri</small>', '<b>Boğaz</b>',
 '<small>derini · ortası · üstü</small>', '<b>Dil</b>', '<small>18 harf</small>',
 '<b>Dudaklar</b>', '<b>Burun</b>', '<small>gunne</small>',
 'Avucunu boğazına koy ve <span class="arin">هَ — عَ — غَ</span> de: ses yukarı çıkar. <span class="arin">بَ — مَ — فَ</span> harflerini de aynanın karşısında söyle ve dudaklarına bak!',
 'Kalın harflerde dilin arka kısmı yükselir — ses büyük bir borudaki gibi «dolu» çıkar. Ezberle:',
 'Nunda cezm <span class="arin">نْ</span> ya da kelime sonunda tenvin olursa, «n» farklı farklı okunur — <b>ondan sonra hangi harf geldiğine</b> bakarız.',
 '<b>İzhar — açık</b>', '<small>boğaz harfleri</small>', '<b>İdgam — katma</b>',
 '<small>gunneli: ي ن م و</small>', '<b>İklâb — çevirme</b>', '<small>«n» «m»ye dönüşür</small>',
 '<b>İhfâ — gizleme</b>', '<small>15 harf, gunne</small>',
 '<b>İhfâ-i şefevî</b>', '<small>gunneli</small>', '<b>İdgam</b>', '<b>İzhar-ı şefevî</b>',
 '<span>diğer bütün harfler</span>', '<small>özellikle و ve ف önünde</small>',
 'Bu harfler cezmle <b>hafif bir yankıyla</b> duyulur. Ezberle:',
 'Kelimenin ortasında yankı küçüktür, sonunda durunca daha güçlüdür.',
 '<b>Tabiî</b>', '<b>Muttasıl: hemze aynı kelimede</b>', '<b>Munfasıl: hemze sonraki kelimede</b>',
 '<b>Lâzım: medden sonra şedde</b>', '<b>Vakıfta</b>', '2, 4 ya da 6',
 'Hareke sayısı — Âsım\'dan Hafs rivayetine göredir. Med harfinin üstündeki dalgalı çizgi şunu söyler: daha uzun çek.',
 'En iyisi <b>ayet sonunda</b> — rakamlı yuvarlakta durmaktır. Dururken son hareke cezme dönüşür:',
 '<p><b>mutlaka</b> durulur</p>', '<p>durulmaz</p>', '<p>ikisi de olur</p>',
 '<p><b>devam</b> etmek daha iyi</p>', '<p><b>durmak</b> daha iyi</p>',
 '<b>Temiz eller ve sakin bir yer.</b> Rahatça otururuz, acele etmeyiz, dikkatle dinleriz.',
 '<b>İstiâze ile başlarız</b> — bu bir ayet değil, okumaya başlarken söylediğimiz sözlerdir:',
 '<b>Sonra besmele</b> — «Tevbe» suresi hariç her surenin başında:',
 '<b>Yavaş ve güzel okuruz</b> — buna tertil denir.',
]
assert len(FRAG_V) == len(ct2.FRAG), (len(FRAG_V), len(ct2.FRAG))
FRAG = [(a, b) for (a, _), b in zip(ct2.FRAG, FRAG_V)]

RX = [
 (r'^Какая буква спряталась в форме (.+)\?$', r'\1 şeklinde hangi harf saklanıyor?'),
 (r'^Какие ручки у формы (.+)\?$', r'\1 şeklinin elleri nasıl?'),
 (r'^Буква (.+) держит за руку следующую букву\?$', r'\1 harfi sonraki harfin elinden tutar mı?'),
 (r'^(.+) не соединяется со следующей буквой\.$', r'\1 sonraki harfle birleşmez.'),
 (r'^(.+) соединяется со следующей буквой\.$', r'\1 sonraki harfle birleşir.'),
 (r'^Это (.+) (отдельно|в начале|в середине|в конце)\.$', lambda m: f'Bu, {m.group(1)} — {POS[m.group(2)]}.'),
 (r'^Это (.+)\.$', r'Bu, \1.'),
 (r'^Откуда выходит звук (.+)\?$', r'\1 sesi nereden çıkar?'),
 (r'^(.+) — из середины горла\.$', r'\1 — boğazın ortasından.'), (r'^(.+) — из верхней части горла\.$', r'\1 — boğazın üst kısmından.'),
 (r'^(.+) — из глубины горла\.$', r'\1 — boğazın derininden.'), (r'^(.+) — губы смыкаются\.$', r'\1 — dudaklar kapanır.'),
 (r'^(.+) — кончик языка\.$', r'\1 — dilin ucu.'), (r'^(.+) — кончик языка у зубов\.$', r'\1 — dilin ucu dişlerin yanında.'),
 (r'^(.+) — зубы и нижняя губа\.$', r'\1 — dişler ve alt dudak.'),
 (r'^Буква (.+) — толстая или тонкая\?$', r'\1 harfi kalın mı, ince mi?'),
 (r'^(.+) — толстая буква\.$', r'\1 — kalın bir harf.'), (r'^(.+) — тонкая буква\.$', r'\1 — ince bir harf.'),
 (r'^После (.+) идёт буква (.+)\. Какое правило\?$', r'\1 harfinden sonra \2 harfi geliyor. Hangi kural?'),
 (r'^(.+) — изхар\.$', r'\1 — izhar.'), (r'^(.+) — идгам\.$', r'\1 — idgam.'), (r'^(.+) — икляб\.$', r'\1 — iklâb.'), (r'^(.+) — ихфа\.$', r'\1 — ihfâ.'),
 (r'^(.+)<br>Какое правило у нуна с сукуном или танвина\?$', r'\1<br>Cezmli nunun ya da tenvinin kuralı hangisi?'),
 (r'^(.+)<br>Сколько тянуть маленький алиф\?$', r'\1<br>Küçük elif ne kadar uzatılır?'),
 (r'^(.+)<br>После мадда хамза в том же слове\. Сколько тянуть\?$', r'\1<br>Medden sonra aynı kelimede hemze var. Ne kadar uzatılır?'),
 (r'^(.+)<br>После мадда — шадда\. Сколько тянуть\?$', r'\1<br>Medden sonra şedde var. Ne kadar uzatılır?'),
 (r'^Что значит знак (.+)\?$', r'\1 işareti ne demek?'),
 (r'^Как называется буква (.+)\?$', r'\1 harfinin adı ne?'),
 (r'^Как читается (.+)\?$', r'\1 nasıl okunur?'),
 (r'^Сегодня мы читаем суру «(.+)»\. Это особая страница — относимся к ней бережно\.$', lambda m: f'Bugün {SUR.get(m.group(1), m.group(1))} suresini okuyoruz. Bu özel bir sayfa — ona özenle davranıyoruz.'),
 (r'^Сура (.+)$', lambda m: f'{SUR.get(m.group(1), m.group(1))} suresi'),
 (r'^Машаллах! Сура «(.+)» прочитана!$', lambda m: f'Maşallah! {SUR.get(m.group(1), m.group(1))} suresi okundu!'),
 (r'^<p class="lead mean">(Аль-Фатиха|Аль-Ихлас|Аль-Каусар|Аль-Фаляк|Ан-Нас|Аль-Аср) — .*</p>$', lambda m: f'<p class="lead mean">{MEAN[SUR[m.group(1)]]}</p>'),
]

RU2TR = {'Ба': 'Be', 'Та': 'Te', 'Фа': 'Fe', 'Ха лёгкая': 'He', 'Хо': 'Ho', 'Айн': 'Ayn', 'Лям': 'Lam', 'Мим': 'Mim'}
def tr(s):
    m = re.match(r'^(Ба|Та|Фа|Ха лёгкая|Хо|Айн|Лям|Мим) — (из|губы|кончик|зубы)', s)
    if m: s = RU2TR[m.group(1)] + s[len(m.group(1)):]
    if s in EXACT: return EXACT[s]
    for pat, rep in RX:
        if re.match(pat, s, flags=re.S):
            return re.sub(pat, rep, s, flags=re.S)
    t = s
    for a, b in FRAG:
        t = t.replace(a, b)
    t = t.replace('«…ин»', '«…în»')
    if re.search('[А-Яа-яЁё]', t) and len(t) < 12:
        t = translit(t)
    return t

TL = [('дж', 'c'), ('а', 'a'), ('б', 'b'), ('в', 'v'), ('г', 'g'), ('д', 'd'), ('е', 'e'), ('з', 'z'), ('и', 'i'), ('й', 'y'), ('к', 'k'),
      ('л', 'l'), ('м', 'm'), ('н', 'n'), ('о', 'o'), ('п', 'p'), ('р', 'r'), ('с', 's'), ('т', 't'), ('у', 'u'), ('ф', 'f'), ('х', 'h'),
      ('ш', 'ş'), ('ъ', ''), ('ы', 'ı'), ('я', 'ya'), ('ю', 'yu')]
def translit(s):
    for a, b in TL:
        s = s.replace(a, b)
    return s

def walk(x, key=None):
    if isinstance(x, dict): return {k: walk(v, k) for k, v in x.items()}
    if isinstance(x, list): return [walk(v, key) for v in x]
    if isinstance(x, str) and key not in ('ar', 'ayahs', 'basm', 'nums', 'icon', 'parts', 'word', 'hit', 'miss') and re.search('[А-Яа-яЁё]', x):
        return tr(x)
    return x

GT_JS = r'''Object.assign(GT, {
  hunt: a => `Bütün ${a} harflerini bul`,
  fish: a => `Balık avı! ${a} harfi olan balıkları yakala`,
  stars: a => `Yıldızlı gökyüzü! ${a} harfi olan yıldızları yak`,
  meadow: a => `Çiçekli çayır! Arıcığa ${a} harfi olan çiçekleri bulmasında yardım et`,
  apple: a => `Elma ağacı! ${a} harfi olan elmaları topla`,
  count: a => `Say! Her sırada ${a} harfi kaç kez saklanmış?`,
  pair: a => 'Eşini bul! Aynı iki harfe dokun',
  path: a => `Eve giden yol! Sadece ${a} harflerinin üstünden yürü — başlangıçtan eve`,
  found: (k, t) => `Bulundu: <b>${k}</b> / ${t}`, pairs: (k, t) => `Çiftler: <b>${k}</b> / ${t}`,
  reset: '↺ Baştan başla', resetQ: 'Bütün yıldızlar silinecek ve yolculuk baştan başlayacak. Baştan başlansın mı?', yes: 'Evet, baştan başla', no: 'Hayır',
  about: {btn: '💗 Bu uygulama hakkında', back: '← Harita', title: 'Bu uygulama ne için', toMap: 'Haritaya', author: 'Elmaza Temirkaliyeva',
    text: ["Bu uygulama, çocuklar Kur'an‑ı Kerim'i okumaya ilk adımlarını Zeynep ve Yusuf ile birlikte sevinçle ve sevgiyle atsınlar diye hazırlandı.",
           'Okunan her harf çocuğa nur, bu uygulama da onunla öğreten ve öğrenen herkes için sadaka-i cariye olsun.'],
    dedT: 'İthaf', dedN: "her şeyden önce<br>oğlum&nbsp;Yusuf'a&nbsp;—<br>ilham kaynağıma", dedD: "Allah seni Kur'an'ın dostu&nbsp;eylesin<br>ve kalbini onun nuruyla&nbsp;doldursun",
    dua: "«Allah'ım, bizden kabul et ve bunu faydalı bir ilim eyle»", credit: "Sure okumaları: «Bolalar uchun Qur'on» (YouTube). Emeği geçenlere teşekkür ederiz!"},
  ay: {prev: '← Geri', basm: 'Besmele', first: 'İlk ayet', next: 'Sonraki ayet', done: 'Okuduk!', whole: '🔊 Surenin tamamını dinle', num: (n, t) => `Ayet ${n} / ${t}`},
  g: {go: 'Başla!', again: 'Bir daha', swipe: 'Yılancığı parmağınla ya da oklarla yönlendir',
    snakeH: a => `Yılancık! Bütün ${a} harflerini ye`, trainH: a => `Trencik! ${a} harfi olan vagona dokun`,
    basketH: 'Sepetler! Harf hangi evcikte yaşıyor?', memH: 'Eşini bul! Aynı iki kartı aç',
    eaten: (k, t) => `Yedi: <b>${k}</b> / ${t}`, round: (k, t) => `Vagon <b>${k}</b> / ${t}`, sorted: (k, t) => `Yerleşti: <b>${k}</b> / ${t}`, pairs: (k, t) => `Çiftler: <b>${k}</b> / ${t}`,
    notThis: a => `Bu başka bir harf — ${a} harfini ara!`, wrongZone: n => `Bu harf «${n}» evciğinde yaşar`, throat: 'Boğazcık', tongue: 'Dilcik', lips: 'Dudakçıklar'},
  table: {btn: '🔤 Harf tablosu', title: 'Harf tablosu', hint: 'Harfe dokun — üç harekeyi de duy, kareye dokun — tek heceyi', back: '← Harita', cols: ['Harf', '', 'Fetha', 'Kesra', 'Damme'], tabs: ['🔤 Harfler', '📘 Kurallar', '🔗 Birleştir'], join: {hint: 'Harflere dokun — nasıl birleştiklerini gör', alone: 'Ayrı ayrı:', clr: 'Temizle'}, rules: [["Fetha", "بَ", "Üstte çizgi — «a» sesi: ba"], ["Kesra", "بِ", "Altta çizgi — «i» sesi: bi"], ["Damme", "بُ", "Üstte küçük vav — «u» sesi: bu"], ["Cezm", "أَبْ", "Halka: harf uyur, harekesiz — ab"], ["Şedde", "أَبَّ", "İkiz harf — abba"], ["Tenvin", "بًا بٍ بٌ", "Çift hareke — ban, bin, bun"], ["Med", "بَا بِي بُو", "<span class=\"ar\">ا و ي</span> sesi 2 hareke uzatır"], ["Harfin şekilleri", "ب بـ ـبـ ـب", "tek başına · başta · ortada · sonda"], ["Yalnızlar", "ا د ذ ر ز و", "Sonraki harfle birleşmezler"], ["Şemsî harfler", "الشَّمْسُ", "Lam saklanır, harf ikizlenir"], ["Kamerî harfler", "الْقَمَرُ", "Lam görünür ve duyulur"], ["Kalkale", "ق ط ب ج د", "Cezmli harf top gibi zıplar"], ["Kalın harfler", "خ ص ض غ ط ق ظ", "«Dolu ağızla» okunur"], ["Gunne", "نّ مّ", "Burundan 2 hareke uzatırız"], ["Cezmli nun", "نْ", "<div class=\"rw\"><b>İzhar</b><span class=\"ar\">ء ه ع ح غ خ</span></div><div class=\"rw\"><b>İdgam</b><span class=\"ar\">ي ر م ل و ن</span></div><div class=\"rw\"><b>İklâb</b><span class=\"ar\">ب</span></div><div class=\"rw\"><b>İhfâ</b><span>kalan 15</span></div>"], ["Cezmli mim", "مْ", "<div class=\"rw\"><b>İhfâ-i şefevî</b><span class=\"ar\">ب</span></div><div class=\"rw\"><b>İdgam</b><span class=\"ar\">م</span></div><div class=\"rw\"><b>İzhar-ı şefevî</b><span>diğerleri</span></div>"], ["Uzun med", "آ", "<div class=\"rw\"><b>Tabiî</b><span>2 hareke</span></div><div class=\"rw\"><b>Muttasıl</b><span>4–5 hareke</span></div><div class=\"rw\"><b>Lâzım</b><span>6 hareke</span></div>"]]},
  song: '🎵 Şarkıyı dinle',
  tap: 'Dokun!', nextLetter: 'Sonraki harf →', nextLesson: 'Sonraki ders →',
  done: 'Maşallah! Başardın!', start: 'başla', pathHint: 'Harfli komşu kareye dokun', countHint: 'Her sıranın altından sayıyı seç', again: 'Bir daha say!'
});'''
