// ---------- Разделы 2, 4, 5: огласовки, танвин, мадд (общий движок) ----------
const HV = [
  {m:'َ', name:'Фатха', ar:'فَتْحَةٌ', v:'а', where:'чёрточка <b>сверху</b>', mouth:'Ротик открываем широко'},
  {m:'ِ', name:'Касра', ar:'كَسْرَةٌ', v:'и', where:'чёрточка <b>снизу</b>', mouth:'Уголки губ тянутся в улыбку'},
  {m:'ُ', name:'Дамма', ar:'ضَمَّةٌ', v:'у', where:'маленький завиток <b>сверху</b>', mouth:'Губы собираются в трубочку'}];
const SL = ['أ', ...LET.slice(1).map(l=>l.ch)];
const syl = (l, k) => l === 'أ' ? ['أَ','إِ','أُ'][k] : l + HV[k].m;
// буквы, у которых русский звук однозначный — для игр «найди слог по звуку»
const TRL = {'ب':'б','ت':'т','ج':'дж','د':'д','ر':'р','ف':'ф','ل':'л','م':'м','ن':'н','ك':'к','ش':'ш'};
const UL = Object.keys(TRL);
const snd = (l, k) => TRL[l] + HV[k].v;
const rnd = a => a[Math.floor(Math.random()*a.length)];
let hk = 0, hpage = 0, hround = 0, hseq = [], hspins = 0, SET = null;
const hkOf = () => hk < 3 ? hk : Math.floor(Math.random()*3);

const SV = (top, bot) => `<svg viewBox="0 0 60 70" aria-hidden="true"><rect x="14" y="22" width="32" height="26" rx="8" fill="#EDE3D3"/>${top||''}${bot||''}</svg>`;
const STK = (y) => `<path d="M20 ${y+7} L40 ${y}" stroke="#D9998A" stroke-width="6" stroke-linecap="round"/>`;
const CURL = '<path d="M34 16 c-6 0 -8 -9 -2 -10 c5 -1 6 5 2 9 c-3 4 -8 6 -12 7" stroke="#D9998A" stroke-width="5" fill="none" stroke-linecap="round"/>';

const SETS = {
  h: { id:'h', sec:'Огласовки', hat:'шапочку', hats:'шапочки', letters: SL, syl, snd,
       V: HV.map((v,k)=>({...v, svg: SV(k===0?STK(7):k===2?CURL:'', k===1?STK(56):'')})),
       lessons: [{k:0,title:'Фатха',icon:'بَ'},{k:1,title:'Касра',icon:'بِ'},{k:2,title:'Дамма',icon:'بُ'},{k:3,title:'Все вместе',icon:'بَ بِ بُ'}],
       greet: k => k===0 ? 'Буквы умеют надевать волшебные шапочки! Первая шапочка — Фатха.' : k<3 ? `Мы уже знаем шапочку ${HV[k-1].name}. Сегодня новая шапочка — ${HV[k].name}!` : 'Сегодня соберём все три шапочки вместе и будем крутить колесо!',
       base: k => 'ب', baseText: 'Это буква Ба. Сама по себе она говорит только «б». Давай наденем на неё шапочку!', btn: 'Надеть шапочку',
       note: v => `${v.mouth}. Читаем коротко, на один счёт: «б${v.v}», а не «б${v.v}-${v.v}-${v.v}».`,
       readHint: 'Читаем вслух справа налево, коротко и чётко. Нажми на слог — он подпрыгнет!',
       threeTitle: 'Три волшебные шапочки', wheelTitle: 'Колесо огласовок' },
  t: { id:'t', sec:'Танвин', hat:'танвин', hats:'танвина', letters: SL.slice(1),
       syl: (l,k) => l + ['ًا','ٍ','ٌ'][k], snd: (l,k) => TRL[l] + ['ан','ин','ун'][k],
       V: [{name:'Фатхатан', ar:'فَتْحَتَانِ', v:'ан', where:'две чёрточки <b>сверху</b> и алиф после', mouth:'Алиф после фатхатана при чтении подряд не произносится', svg: SV(STK(3)+STK(12)+'<path d="M8 20 V48" stroke="#9C8478" stroke-width="5" stroke-linecap="round"/>')},
           {name:'Касратан', ar:'كَسْرَتَانِ', v:'ин', where:'две чёрточки <b>снизу</b>', mouth:'Улыбаемся и добавляем «н»', svg: SV('', STK(52)+STK(61))},
           {name:'Дамматан', ar:'ضَمَّتَانِ', v:'ун', where:'двойной завиток <b>сверху</b>', mouth:'Губы трубочкой и добавляем «н»', svg: SV(CURL+'<path d="M24 16 c-6 0 -8 -9 -2 -10 c5 -1 6 5 2 9" stroke="#D9998A" stroke-width="4" fill="none" stroke-linecap="round"/>')}],
       lessons: [{k:0,title:'Фатхатан',icon:'بًا'},{k:1,title:'Касратан',icon:'بٍ'},{k:2,title:'Дамматан',icon:'بٌ'},{k:3,title:'Все вместе',icon:'بًا بٍ بٌ'}],
       greet: k => k===0 ? 'Знаешь, что бывает, когда шапочек две? Появляется эхо «н»! Это танвин.' : k<3 ? `Мы уже знаем ${['фатхатан','касратан'][k-1]}. Сегодня — ${['','касратан','дамматан'][k]}!` : 'Сегодня соберём все три танвина вместе и покрутим колесо!',
       base: k => 'ب' + HV[k].m, baseText: 'Это слог с одной шапочкой. А если шапочек будет две?', btn: 'Удвоить шапочку',
       note: v => `${v.mouth}. Танвин — как эхо: «б${v.v}-н».`,
       readHint: 'Читаем справа налево: в конце каждого слога звучит лёгкое «н».',
       threeTitle: 'Три танвина', wheelTitle: 'Колесо танвина' },
  m: { id:'m', sec:'Мадд', hat:'мадд', hats:'мадда', letters: SL.slice(1).filter(l => !'وي'.includes(l)),
       syl: (l,k) => l + ['َا','ِي','ُو'][k], snd: (l,k) => TRL[l] + ['а-а','и-и','у-у'][k],
       V: [{name:'Мадд с алифом', ar:'ا', v:'а-а', where:'фатха, а после неё <b>алиф</b>', mouth:'Тянем «а» на 2 счёта — два шажка', svg: SV(STK(7)+'<path d="M8 20 V48" stroke="#53669B" stroke-width="5" stroke-linecap="round"/>')},
           {name:'Мадд с йе', ar:'ي', v:'и-и', where:'касра, а после неё <b>йе</b>', mouth:'Тянем «и» на 2 счёта — два шажка', svg: SV('', STK(56)+'<path d="M4 40 q6 10 10 0" stroke="#53669B" stroke-width="5" fill="none" stroke-linecap="round"/>')},
           {name:'Мадд с вав', ar:'و', v:'у-у', where:'дамма, а после неё <b>вав</b>', mouth:'Тянем «у» на 2 счёта — два шажка', svg: SV(CURL+'<circle cx="8" cy="34" r="5" fill="none" stroke="#53669B" stroke-width="4"/><path d="M12 36 q0 12 -8 14" stroke="#53669B" stroke-width="4" fill="none" stroke-linecap="round"/>')}],
       lessons: [{k:0,title:'С алифом',icon:'بَا'},{k:1,title:'С йе',icon:'بِي'},{k:2,title:'С вав',icon:'بُو'},{k:3,title:'Все вместе',icon:'بَا بِي بُو'}],
       greet: k => k===0 ? 'Звуки бывают короткие и длинные! Сегодня научимся тянуть звук «а».' : k<3 ? `Мы уже умеем тянуть «${['а','и'][k-1]}». Сегодня потянем «${['','и','у'][k]}»!` : 'Сегодня соберём все длинные звуки вместе!',
       base: k => 'ب' + HV[k].m, baseText: 'Это короткий слог — один шажок. А если после него встанет буква мадда?', btn: 'Добавить букву мадда',
       note: v => `${v.mouth}: «б${v.v}». Короткий звук — шажок, длинный — два шага!`,
       readHint: 'Читаем справа налево и тянем каждый звук ровно на 2 счёта.',
       threeTitle: 'Три длинных звука', wheelTitle: 'Колесо мадда' }
};

function buildSet(id, i){
  const C = SET = SETS[id], H = C.lessons[i]; hk = H.k; got = new Set(); cur = 0; idx = i; N = 8; STEPS = [2,3,4,5,6]; CSTEP = 5;
  MODE = id.toUpperCase(); KEY = id+i; AGAIN = () => { buildSet(id, i); go(0); }; NEXTH = i < C.lessons.length-1 ? id+'-'+(i+2) : ({h:'s-1', t:'m-1', m:'p0-1'})[id] || 'map';
  const [s1, s2] = speaker(i);
  const hero = (who, kind) => CH[who + '_' + kind];
  const V = C.V[hk] || null;
  $('#tAr').innerHTML = g(C.syl('ب', hk<3 ? hk : 0)); $('#tRu').textContent = `${C.sec} ${i+1} из 4 · ${H.title}`;
  const meet = hk<3 ? `
    <div class="meet">
      <div class="letterbox"><span class="big swap hbig" id="swap" tabindex="0" role="button" aria-label="Слог"><span class="a" style="transform:translateY(${sh(C.base(hk))})">${C.base(hk)}</span><span class="b" style="transform:translateY(${sh(C.syl('ب',hk))})">${C.syl('ب',hk)}</span></span></div>
      <div class="meetcol">
        <p class="lead" id="meetText">${C.baseText}</p>
        <button class="btn rose" id="addDot">${C.btn}</button>
        <div id="meetMore" hidden style="display:flex;flex-direction:column;gap:12px;align-items:center">
          <div class="name">${V.name} <span class="arn">${V.ar}</span></div>
          <div class="mnemo"><span class="hsign">${V.svg}</span><span>${V.where} — звук <b>«${V.v}»</b></span></div>
          <div class="snd">${C.note(V)}</div>
          <button class="btn" id="say">Скажем вместе: «б${V.v}!»</button>
        </div>
      </div>
    </div>
    <div class="side"><div class="hero sm">${hero(s1,'point')}</div><div class="bubble" id="meetBubble">Нажми на кнопку — и слог заговорит по-новому!</div></div>` : `
    <h2>${C.threeTitle}</h2>
    <div class="cards hthree">${C.V.map((v,k)=>`<button class="card hcard" data-k="${k}">${g(C.syl('ب',k))}<span class="hc-n">${v.name}</span><span class="hc-s">«б${v.v}»</span></button>`).join('')}</div>
    <div class="side"><div class="hero sm">${hero(s1,'point')}</div><div class="bubble">Нажми на каждую карточку и прочитай: ${C.V.map(v=>'«б'+v.v+'»').join(', ')}.</div></div>`;
  const read = hk<3 ? `
    <div class="side"><div class="hero sm">${hero(s2,'book')}</div><div class="bubble">${C.readHint}</div></div>
    <div class="grid hread" id="hread"></div>
    <div class="row"><span class="count" id="hpageN"></span><button class="btn" id="hpageNext">Дальше</button></div>` : `
    <h2>${C.wheelTitle}</h2>
    <p class="lead">Крути колесо! Выпадет буква — прочитай её тремя способами.</p>
    <div class="wheel"><div class="wl" id="wl">${g('ب')}</div><div class="wsyl" id="wsyl">${[0,1,2].map(k=>`<span class="card wcard">${g(C.syl('ب',k))}</span>`).join('')}</div></div>
    <div class="row"><button class="btn rose" id="spin">Крутить колесо</button><span class="count">Прокрутили: <b id="spinN">0</b> из 5</span></div>`;
  $('#screens').innerHTML = `
  <section data-s="0">
    <div class="duo">
      <div class="hero"><div class="bubble">Ассаляму алейкум!</div>${hero(s1,'wave')}</div>
      <div class="hero"><div class="bubble">${C.greet(hk)}</div>${hero(s2,'wave')}</div>
    </div>
    <button class="btn" data-go="1">Бисмиллях, начинаем!</button>
  </section>
  <section data-s="1">${meet}</section>
  <section data-s="2">${read}</section>
  <section data-s="3">
    <div class="side"><div class="hero sm">${hero(s2,'point')}</div><div class="bubble" id="hqQ"></div></div>
    <div class="cards tall" id="hq"></div>
    <div class="hint" id="hqHint"></div>
    <div class="count" id="hqN"></div>
  </section>
  <section data-s="4">
    <div class="side"><div class="hero sm">${hero(s1,'book')}</div><div class="bubble">Обведи слог: сначала букву, потом знаки!</div></div>
    <div class="tracewrap" id="tracewrap"><canvas id="cv"></canvas></div>
    <div class="row"><div class="colors" id="colors"></div><button class="btn soft" id="clear">Стереть</button><button class="btn soft" id="newSyl">Другой слог</button><button class="btn" id="traceDone">Готово!</button></div>
  </section>
  <section data-s="5">
    <div class="row"><h2>Поймай ${C.hat}!</h2><span class="timer" id="timer"></span><span class="count">Поймали: <b id="ccount">0</b></span></div>
    <div class="field" id="field"><div class="overlay" id="catchStart"><p class="lead" id="catchLead"></p><button class="btn rose" id="catchGo">Старт!</button></div></div>
  </section>
  <section data-s="6">
    <h2>Быстрый взгляд</h2>
    <p class="lead">Как читается этот слог? Скажите вслух, а потом проверим.</p>
    <div class="flash tall"><span class="g" id="flash"></span></div>
    <div class="answer" id="answer"></div>
    <div class="row"><button class="btn soft" id="reveal">Проверить</button><button class="btn" id="flashNext">Следующий</button></div>
    <div class="count" id="fround"></div>
  </section>
  <section data-s="7" class="final">
    <h2>Машаллах! Ты молодец!</h2>
    <div class="stars" id="finalStars"></div>
    <div class="duo">
      <div class="hero sm"><div class="bubble">${hk<3 ? `Теперь ты знаешь: ${V.name}!` : `Ты знаешь все три ${C.hats}!`}</div>${hero(s1,'open')}</div>
      <div class="hero sm"><div class="bubble">${i < C.lessons.length-1 ? 'Следующий урок — '+C.lessons[i+1].title+'. До встречи, ин шаа Аллах!' : 'Скоро новые уроки, ин шаа Аллах!'}</div>${hero(s2,'wink')}</div>
    </div>
    <div class="dua">رَبِّ زِدْنِي عِلْمًا</div>
    <p class="lead">«Господи, прибавь мне знаний»</p>
    <div class="row"><button class="btn soft" id="again">Ещё раз</button>${i < C.lessons.length-1 ? `<button class="btn sage" id="nextLetter">Дальше: ${C.lessons[i+1].title} →</button>` : ''}<button class="btn soft" id="toMap2">На карту</button></div>
  </section>`;
  $('#path').innerHTML = Array.from({length:N},(_,k)=>(k?'<i></i>':'')+'<b></b>').join('');
  drawStars($('#stars'));
  setCatch(hk<3 ? hk : 0);
  TR = C.syl(rnd(UL), hkOf());
  wire(); wireSet();
}

function setCatch(t){
  const C = SET, v = C.V[t];
  CLEAD = `Лопай только шарики, где <b>${v.name}</b> <span class="hsvg-in">${v.svg}</span> — звук «${v.v}»`;
  CDONE = v.name;
  CPICK = () => { const l = rnd(C.letters), hit = Math.random() < 0.5; const k = hit ? t : rnd([0,1,2].filter(x=>x!==t)); return [C.syl(l,k), hit]; };
}

function wireSet(){
  const C = SET;
  if(hk<3){
    const sw = $('#swap');
    $('#addDot').onclick = () => { sfx('magic'); sw.classList.add('dot'); $('#addDot').hidden = true; $('#meetMore').hidden = false; $('#meetText').textContent = 'Вот так! Получилось:'; $('#meetBubble').textContent = 'Нажми на слог, он подпрыгнет!'; };
    sw.onclick = () => bounceEl(sw);
    $('#say').onclick = () => { bounceEl(sw); say(C.syl('ب', hk)); $('#meetBubble').textContent = `«б${C.V[hk].v}»! Машаллах, как красиво!`; confetti(40); };
    $('#hpageNext').onclick = () => { if(hpage < readPages()-1){ hpage++; drawRead(); } else { award(2); go(3); } };
  } else {
    $$('.hcard').forEach(c => c.onclick = () => { bounceEl(c); say(C.syl('ب', +c.dataset.k)); });
    $('#spin').onclick = spinWheel;
  }
  $('#newSyl').onclick = () => { TR = C.syl(rnd(UL), hkOf()); sizeCanvas(); };
  $('#reveal').onclick = () => { const [l,k] = hseq[fr]; $('#answer').textContent = '«' + C.snd(l,k) + '»'; say(C.syl(l,k)); };
  $('#flashNext').onclick = () => { if(fr < hseq.length-1){ fr++; showHFlash(); } else { award(6); go(7); } };
  $('#catchGo').onclick = () => { if(hk===3) { setCatch(Math.floor(Math.random()*3)); } startCatch(); };
}

function enterSet(i){
  if(i===1 && hk<3){ $('#swap').classList.remove('dot'); $('#addDot').hidden = false; $('#meetMore').hidden = true; }
  if(i===2){ if(hk<3){ hpage = 0; drawRead(); } else { hspins = 0; $('#spinN').textContent = '0'; } }
  if(i===3){ hround = 0; drawQuiz(); }
  if(i===6){ const ks = hk<3 ? [...Array(hk+1).keys()] : [0,1,2];
    hseq = shuffle(Array.from({length:6}, (_,n) => [rnd(UL), n<3 && hk<3 ? hk : rnd(ks)])); fr = 0; showHFlash(); }
}

// чтение: все буквы раздела, по 7 на странице
const readPages = () => Math.ceil(SET.letters.length / 7);
function drawRead(){
  const part = SET.letters.slice(hpage*7, hpage*7+7);
  $('#hread').innerHTML = part.map(l => `<button class="tile">${g(SET.syl(l,hk))}</button>`).join('');
  $$('#hread .tile').forEach(t => t.onclick = () => { bounceEl(t); say(t.textContent); });
  markVoice($('#hread'));
  $('#hpageN').textContent = `${hpage+1} из ${readPages()}`;
  $('#hpageNext').textContent = hpage < readPages()-1 ? 'Дальше' : 'Прочитали!';
}

// колесо
function spinWheel(){
  const btn = $('#spin'); btn.disabled = true; let n = 0;
  const t = setInterval(() => { const l = rnd(SET.letters.filter(x => x !== 'أ')); $('#wl').innerHTML = g(l); sfx('tap'); n++;
    if(n > 12){ clearInterval(t); btn.disabled = false; $('#wsyl').innerHTML = [0,1,2].map(k=>`<span class="card wcard">${g(SET.syl(l,k))}</span>`).join('');
      bounceEl($('#wl')); hspins++; $('#spinN').textContent = Math.min(hspins,5); if(hspins >= 5) award(2); } }, 90);
}

// викторина: 5 вопросов
function drawQuiz(){
  const C = SET, h = $('#hqHint'); if(!h || !$('#hq')) return; h.textContent = '';
  $('#hqN').textContent = `Вопрос ${Math.min(hround+1,5)} из 5`;
  if(hk<3){
    const l = rnd(C.letters.filter(x => x !== 'أ')), V = C.V[hk];
    $('#hqQ').innerHTML = `Где <b>${V.name}</b>? Это ${V.where}.`;
    $('#hq').innerHTML = shuffle([0,1,2]).map(k => `<button class="card" data-k="${k}">${g(C.syl(l,k))}</button>`).join('');
    $$('#hq .card').forEach(c => c.onclick = () => answer(c, +c.dataset.k === hk, +c.dataset.k));
  } else {
    const l = rnd(UL), t = Math.floor(Math.random()*3);
    $('#hqQ').innerHTML = `Какой слог читается <b>«${C.snd(l,t)}»</b>?`;
    $('#hq').innerHTML = shuffle([0,1,2]).map(k => `<button class="card" data-k="${k}" data-l="${l}">${g(C.syl(l,k))}</button>`).join('');
    $$('#hq .card').forEach(c => c.onclick = () => answer(c, +c.dataset.k === t, +c.dataset.k, l));
  }
}
function answer(c, ok, k, l){
  const C = SET, h = $('#hqHint');
  if(ok){ sfx('ok'); c.classList.add('ok'); h.style.color = 'var(--sage)'; h.textContent = 'Правильно! Машаллах!'; setTimeout(() => say(c.textContent.trim()), 250);
    hround++; if(hround >= 5){ award(3); $('#hqN').textContent = 'Все 5 вопросов!'; } else setTimeout(drawQuiz, 1500); }
  else { shakeEl(c); h.style.color = 'var(--rose)';
    h.innerHTML = l ? `Это «${C.snd(l,k)}» — ${C.V[k].name}. Попробуй ещё!` : `Это <b>${C.V[k].name}</b>: ${C.V[k].where}. Попробуй ещё!`; }
}

function showHFlash(){ const [l,k] = hseq[fr], t = SET.syl(l,k);
  $('#flash').textContent = t; $('#flash').style.transform = `translateY(${sh(t)})`; $('#answer').textContent = '';
  $('#fround').textContent = `${fr+1} из ${hseq.length}`; $('#flashNext').textContent = fr===hseq.length-1 ? 'Закончить' : 'Следующий'; bounceEl($('#flash').parentNode); }

// для обратной совместимости с картой и маршрутами раздела 2
const HL = SETS.h.lessons;
