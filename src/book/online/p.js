// ---------- Разделы 6–9: гибкий движок уроков из готовых экранов ----------
// где на рисунке показывать буквы зоны (в процентах от рисунка)
const MVB = [16, 6, 274, 330];
// где ставить подпись буквы, если точки слишком близко (с линией к точке)
const LPOS = {'ث':[30,120],'ذ':[30,139],'ظ':[30,158],'ت':[30,177],'د':[30,196],'ط':[30,215],'ص':[30,234],'س':[30,253],'ز':[30,272],
  'ل':[134,165],'ن':[116,165],'ر':[100,165],'ج':[172,206],'ش':[154,206],'ي':[136,206],'ض':[152,230],'ك':[192,200],'ق':[214,184],
  'ف':[36,158],'ب':[36,177],'م':[36,196],'و':[36,215]};
const mpos = (x, y) => `left:${(x-MVB[0])/MVB[2]*100}%;top:${(y-MVB[1])/MVB[3]*100}%`;
const ZPOS = {throat: [[199,314,'ء'],[199,294,'ه'],[226,252,'ع'],[226,232,'ح'],[228,204,'غ'],[228,184,'خ']],
  tongue: [[158,198,'ق ك ج ش ي ض'],[160,217,'ل ن ر ت د ط'],[176,236,'ص س ز ث ذ ظ']],
  lips: [[36,158,'ف'],[36,177,'ب'],[36,196,'م'],[36,215,'و']], nose: [[150,131,'نّ مّ']], mouth: [[150,173,'ا و ي']]};
let PS = null, PLs = null, PSI = '', PLI = 0, PST = {};
// звук буквы для раздела «Откуда выходят звуки»: своя запись (MKH_V) или слог с фатхой из алфавита
// по решению автора — звук как в алфавите: название буквы (VOICE_N), иначе слог с фатхой
const mkhSrc = ch => { const M = window.MKH_V || {}, V = window.VOICE || {}, N = window.VOICE_N || {}; if(M[ch]) return M[ch];
  if(ch === 'ء') return V['أَ']; if(ch.length > 1 && ch[1] === 'ّ') return V['أَ' + ch[0] + 'َّ'];
  if(ch.length > 1) return null; return N[ch] || V[ch + 'َ']; };
let MKQ = 0;
const mkhPlay = (src, done) => { try { if(VA) VA.pause(); VA = new Audio(src); let f = false; const fin = () => { if(!f){ f = true; done && done(); } };
  VA.onended = () => setTimeout(fin, 180); VA.onerror = fin; if(MUTE) setTimeout(fin, 500); else VA.play().catch(() => setTimeout(fin, 500)); setTimeout(fin, 2500); } catch(e){ done && done(); } };
const dirAr = t => /[؀-ۿ]/.test(t);

function buildP(si, li){
  PSI = si; PLI = li; PS = PL.sections[si]; PLs = PS.lessons[li]; got = new Set(); cur = 0; idx = li;
  const SC = PLs.screens;
  MODE = 'P'; KEY = 'p'+si+'-'+li; N = SC.length;
  STEPS = SC.map((s,k) => s.star ? k : -1).filter(k => k >= 0);
  AGAIN = () => { buildP(si, li); go(0); };
  const sameW = j => PL.sections[j] && (PL.sections[j].world || '') === (PS.world || '');
  NEXTH = li < PS.lessons.length-1 ? `p${si}-${li+2}` : (PS.world === 'r' ? 'map' : sameW(si+1) ? `p${si+1}-1` : (PS.world ? 'namaz' : 'about'));
  const [s1, s2] = speaker(li);
  const hero = (who, kind) => CH[who + '_' + kind];
  const nextT = li < PS.lessons.length-1 ? PS.lessons[li+1].title : (sameW(si+1) ? PL.sections[si+1].lessons[0].title : '');
  $('#tAr').innerHTML = dirAr(PLs.icon) ? g(PLs.icon) : PLs.icon;
  $('#tRu').textContent = `${PS.title.replace(/^Раздел \d+\. /,'')} · ${PLs.title}`;
  $('#screens').innerHTML = SC.map((s,k) => `<section data-s="${k}">${renderP(s, k, s1, s2, hero, nextT)}</section>`).join('');
  $('#path').innerHTML = Array.from({length:N},(_,k)=>(k?'<i></i>':'')+'<b></b>').join('');
  drawStars($('#stars'));
  $$('[data-go]').forEach(b => b.onclick = () => go(+b.dataset.go));
  const ag = $('#again'); if(ag) ag.onclick = () => AGAIN();
  const tm = $('#toMap2'); if(tm) tm.onclick = () => { location.hash = PS.world === 'n' ? 'namaz' : 'map'; };
  const nl = $('#nextLetter'); if(nl) nl.onclick = () => { location.hash = NEXTH; };
}

function renderP(s, k, s1, s2, hero, nextT){
  const side = (who, txt, kind='point') => `<div class="side"><div class="hero sm">${hero(who==='m'?'m':'a', kind)}</div><div class="bubble">${txt}</div></div>`;
  switch(s.t){
    case 'greet': return `<div class="duo"><div class="hero"><div class="bubble">${s.a}</div>${hero(s1,'wave')}</div><div class="hero"><div class="bubble">${s.m}</div>${hero(s2,'wave')}</div></div>${s.song && (window.SONGS||{})[s.song] ? `<button class="btn soft song" data-song="${s.song}">${GT.song}</button>` : ''}<button class="btn" data-go="1">Бисмиллях, начинаем!</button>`;
    case 'info': return `<h2>${s.h}</h2><div class="pinfo">${s.html}</div>${s.who ? side(s.who, s.say) : ''}`;
    case 'forms': return `<h2>${s.h}</h2><div class="pf-pick" id="pfPick${k}">${s.letters.map((l,i)=>`<button class="tile pf-l" data-i="${i}">${g(l.ch)}</button>`).join('')}</div>
      <div class="pf-show" id="pfShow${k}"><p class="lead">Нажми на любую букву!</p></div><div class="count">Посмотрели: <b id="pfN${k}">0</b> из ${s.need}</div>`;
    case 'read': return `${side('m', s.hint, 'book')}<div class="grid pread ${s.cls||''}" id="pr${k}"></div><div class="row"><span class="count" id="prN${k}"></span><button class="btn" id="prNext${k}">Дальше</button></div>`;
    case 'mstep': return `<h2>${s.h}</h2><div class="mth mstep"><div class="ms-svg mwrap" id="msS${k}">${s.svg}<div class="mlay"></div></div><div class="ms-card" id="msC${k}"></div></div><div class="row"><span class="count" id="msN${k}"></span><button class="btn" id="msNext${k}">Следующая буква →</button></div>`;
    case 'mouth': return `<h2>${s.h}</h2><div class="mth mth-play"><div class="mwrap" id="mS${k}">${s.svg}<div class="mlay"></div><div class="mhand"><span>👆</span><b>${GT.tap}</b></div></div><div class="mth-p" id="mP${k}"><p class="lead">${s.tip||''}</p></div></div><div class="count" id="mN${k}"></div>`;
    case 'order': return `<h2>${s.h}</h2><p class="lead">${s.hint}</p><div class="ord-slots" id="ordS${k}">${s.items.map((_,j)=>`<div class="ord-slot"><b>${j+1}</b></div>`).join('')}</div><div class="ord-pool" id="ordP${k}"></div><div class="hint" id="ordH${k}"></div>`;
    case 'quiz': return `<h2>${s.h}</h2><div class="bubble pq" id="pqQ${k}"></div><div class="cards pqo" id="pqO${k}"></div><div class="hint" id="pqH${k}"></div><div class="count" id="pqN${k}"></div>`;
    case 'build': return `<h2>${s.h}</h2><div class="pb-mean" id="pbM${k}"></div><div class="pb-word" id="pbW${k}"></div><div class="cards pb-parts" id="pbP${k}"></div><div class="hint" id="pbH${k}"></div><div class="row"><span class="count" id="pbN${k}"></span><button class="btn" id="pbNext${k}" hidden>Следующее слово</button></div>`;
    case 'examples': return `<h2>${s.h}</h2><div class="pex">${s.items.map(e=>`<button class="pex-i"><span class="arin q">${e.ar}</span><small>${e.lab}</small></button>`).join('')}</div>${side('a','Прочитай каждый пример вместе с учителем. Нажми на карточку — она подпрыгнет!')}<button class="btn" id="pexDone${k}">Прочитали!</button>`;
    case 'catch': return `<div class="row"><h2>${s.h}</h2><span class="timer" id="timer"></span><span class="count">Поймали: <b id="ccount">0</b></span></div>
      <div class="field" id="field"><div class="overlay" id="catchStart"><p class="lead" id="catchLead">${s.lead}</p><button class="btn rose" id="catchGo">Старт!</button></div></div>`;
    case 'ayahs': return `${(window.SONGS||{})['w' + s.sura] ? `<button class="btn soft song ayw" id="ayW${k}">${GT.ay.whole}</button>` : ''}<div class="mus"><div class="mus-head"><span class="arin">${s.ar}</span></div>
      <div class="mus-body" id="musB${k}">${s.basm ? `<div class="mus-basm ay" data-n="-1">${s.basm}</div>` : ''}<div class="mus-text">${s.ayahs.map((a,j)=>`<span class="ay" data-n="${j}">${a}<span class="aend"><span>${s.nums[j]}</span></span></span>`).join(' ')}</div></div></div>
      <div class="row"><button class="btn soft" id="ayPrev${k}">${GT.ay.prev}</button><span class="count" id="ayN${k}"></span><button class="btn" id="ayNext${k}"></button></div>`;
    case 'achieve': return `<h2>${s.h}</h2><div class="ach" id="ach${k}"></div>${side('a','Каждая звёздочка — это твой труд. Машаллах!')}`;
    case 'diploma': return `<div class="dip" id="dip${k}">
      <div class="dip-ar">شَهَادَةٌ</div><div class="dip-t">Диплом</div><div class="dip-s">настоящего друга Корана</div>
      <div class="dip-ar2">أَنَا صَدِيقُ الْقُرْآنِ</div>
      <label class="dip-name">Выдан: <input id="dipName" type="text" placeholder="впиши имя" maxlength="40"></label>
      <p>за то, что прошёл(-ла) всё путешествие: выучил(-а) 28 букв, огласовки, сукун, шадду, танвин, мадд, первые правила таджвида и начал(-а) читать суры Священного Корана.</p>
      <div class="dip-ph">بَارَكَ اللَّهُ فِيكَ</div><div class="dip-y">2026</div></div>
      <button class="btn sage" id="dipOk">Получить диплом!</button>`;
    case 'snake': return `<h2 id="snH${k}"></h2><div class="count" id="snN${k}"></div>
      <div class="sn-field" id="snF${k}"><div class="sn-over" id="snO${k}"><button class="btn" id="snGo${k}">${GT.g.go}</button><small>${GT.g.swipe}</small></div></div>
      <div class="sn-pad" id="snP${k}"><button data-d="0,-1" aria-label="up">▲</button><span><button data-d="1,0" aria-label="right">▶</button><button data-d="-1,0" aria-label="left">◀</button></span><button data-d="0,1" aria-label="down">▼</button></div>
      <div class="hint" id="snHint${k}"></div>`;
    case 'train': return `<h2 id="trH${k}"></h2><div class="count" id="trN${k}"></div>
      <div class="tr-track"><div class="tr-train" id="trT${k}"></div><div class="tr-rail"></div></div>
      <div class="hint" id="trHint${k}"></div><div class="row" id="trA${k}"></div>`;
    case 'basket': return `<h2>${GT.g.basketH}</h2><div class="count" id="bkN${k}"></div>
      <div class="bk-stage"><div class="bk-card" id="bkL${k}"></div></div>
      <div class="bk-row">${['throat','tongue','lips'].map(z => `<button class="bk" data-z="${z}">${s.icons[z]}<b>${GT.g[z]}</b><span class="bk-c">0</span></button>`).join('')}</div>
      <div class="hint" id="bkHint${k}"></div><div class="row" id="bkA${k}"></div>`;
    case 'memory': return `<h2>${GT.g.memH}</h2><div class="count" id="meN${k}"></div><div class="mem" id="mem${k}"></div><div class="row" id="meA${k}"></div>`;
    case 'final': return `<h2>Машаллах! Ты молодец!</h2><div class="stars" id="finalStars"></div>
      <div class="duo"><div class="hero sm"><div class="bubble">${s.a}</div>${hero(s1,'open')}</div><div class="hero sm"><div class="bubble">${s.m}</div>${hero(s2,'wink')}</div></div>
      <div class="dua">رَبِّ زِدْنِي عِلْمًا</div><p class="lead">«Господи, прибавь мне знаний»</p>
      <div class="row"><button class="btn soft" id="again">Ещё раз</button><button class="btn soft" id="toMap2">На карту</button></div>`;
  }
  return '';
}

function enterP(i){
  const s = PLs.screens[i], k = i;
  if(s.t === 'final'){ drawStars($('#finalStars')); confetti(120); setTimeout(()=>sfx('fanfare'), 250); return; }
  if(s.t === 'forms'){
    const seen = new Set();
    $$(`#pfPick${k} .pf-l`).forEach(b => b.onclick = () => { sfx('tap'); const L = s.letters[+b.dataset.i]; seen.add(L.ch); b.classList.add('ok');
      const H = s.hands;
      $(`#pfShow${k}`).innerHTML = `<div class="pf-name">${L.ru}</div><div class="pf-row" dir="rtl">${L.forms.map(([f,lab,lo,ro])=>`<div class="pf-c">${H ? `<div class="pf-h" dir="ltr">${lo?H.pl:H.fl}<span class="card">${g(f)}</span>${ro?H.pr:H.fr}</div>` : `<span class="card">${g(f)}</span>`}<small>${lab}</small></div>`).join('')}</div>`;
      $(`#pfN${k}`).textContent = Math.min(seen.size, s.need); if(seen.size >= s.need) award(i); });
  }
  if(s.t === 'read'){
    let page = 0; const per = s.per || 6, pages = Math.ceil(s.items.length/per);
    const draw = () => { const part = s.items.slice(page*per, page*per+per);
      $(`#pr${k}`).innerHTML = part.map((t,j) => { const ru = s.ru ? s.ru[page*per+j] : '';
        return `<button class="tile ${s.cls==='q'?'qw':''}${(window.VOICE||{})[t]?' hasv':''}" data-t="${t}" data-i="${page*per+j}">${s.cls==='q' ? `<span class="arin q">${t}</span>` : g(t)}${ru?`<small class="pr-ru" hidden>${ru}</small>`:''}</button>`; }).join('');
      $$(`#pr${k} .tile`).forEach(t => t.onclick = () => { bounceEl(t); const tv = s.ayv && (window.SONGS||{})['t1_' + s.ayv[+t.dataset.i]]; const nm = !tv && PS && PS.id === '7' && t.dataset.t.length === 2 && mkhSrc(t.dataset.t[0] === 'أ' ? 'ء' : t.dataset.t[0]); if(tv || nm){ try { if(VA) VA.pause(); VA = new Audio(tv || nm); if(!MUTE) VA.play().catch(()=>{}); } catch(e){} } else say(t.dataset.t); const r = t.querySelector('.pr-ru'); if(r) r.hidden = false; });
      $(`#prN${k}`).textContent = pages > 1 ? `${page+1} из ${pages}` : '';
      $(`#prNext${k}`).textContent = page < pages-1 ? 'Дальше' : 'Прочитали!'; };
    $(`#prNext${k}`).onclick = () => { if(page < pages-1){ page++; draw(); } else { if(s.star) award(i); go(i+1); } };
    draw();
  }
  if(s.t === 'mstep'){
    let n = 0; const tot = s.items.length;
    const draw = () => { const it = s.items[n], svg = $(`#msS${k} svg`);
      const old = svg.querySelector('.msdot'); if(old) old.remove();
      svg.insertAdjacentHTML('beforeend', `<g class="msdot"><circle class="ms-pulse" cx="${it.x}" cy="${it.y}" r="16"/><circle cx="${it.x}" cy="${it.y}" r="6.5" fill="#F4C96B" stroke="#5C4033" stroke-width="2"/></g>`);
      const lay = $(`#msS${k} .mlay`); lay.querySelectorAll('.mlt.cur').forEach(e => e.classList.remove('cur'));
      if(!lay.querySelector(`[data-n="${n}"]`)){ const L = LPOS[it.ch] && s.items.some(o => o !== it && Math.abs(o.x-it.x) + Math.abs(o.y-it.y) < 40);
        const [lx, ly] = L ? LPOS[it.ch] : [it.x, it.y - 14];
        if(L) svg.insertAdjacentHTML('beforeend', `<line class="msl" x1="${lx + (lx < it.x ? 9 : 0)}" y1="${ly}" x2="${it.x}" y2="${it.y}"/>`);
        lay.insertAdjacentHTML('beforeend', `<span class="mlt cur" data-n="${n}" style="${mpos(lx, ly)}">${it.ch}</span>`); }
      else lay.querySelector(`[data-n="${n}"]`).classList.add('cur');
      const c = $(`#msC${k}`); c.classList.remove('in'); void c.offsetWidth;
      c.innerHTML = `<div class="ms-l">${g(it.ch)}</div><div class="ms-n">${it.n}</div><small>${it.d}</small>`; c.classList.add('in');
      const src = mkhSrc(it.ch); ++MKQ; if(src) mkhPlay(src); else sfx('pop'); c.onclick = () => { const s2 = mkhSrc(it.ch); if(s2) mkhPlay(s2); };
      $(`#msN${k}`).textContent = `${n+1} / ${tot}`;
      $(`#msNext${k}`).textContent = n < tot-1 ? 'Следующая буква →' : 'Готово!'; };
    $(`#msNext${k}`).onclick = () => { if(n < tot-1){ n++; draw(); } else { if(s.star) award(i); go(i+1); } };
    draw();
  }
  $$(`section[data-s="${k}"] .nw-play[data-seq]`).forEach(e => e.onclick = () => {
    const S = window.SONGS || {}, list = e.dataset.seq.split(',').map(x => S[x]).filter(Boolean);
    if(e.classList.contains('on')){ try { VA && VA.pause(); } catch(er){} e.classList.remove('on'); return; }
    $$('.nw-play.on').forEach(x => x.classList.remove('on'));
    let j = 0; e.classList.add('on');
    const next = () => { if(j >= list.length || !e.classList.contains('on')){ e.classList.remove('on'); return; }
      try { if(VA) VA.pause(); VA = new Audio(list[j++]); VA.onended = next; if(!MUTE) VA.play().catch(()=>e.classList.remove('on')); else e.classList.remove('on'); } catch(er){ e.classList.remove('on'); } };
    next();
  });
  $$(`section[data-s="${k}"] .ist[data-song]`).forEach(e => e.onclick = () => { const src = (window.SONGS||{})[e.dataset.song]; if(!src) return; try { if(VA) VA.pause(); VA = new Audio(src); if(!MUTE) VA.play().catch(()=>{}); } catch(er){} });
  if(s.t === 'greet'){ const sb = $(`section[data-s="${k}"] .song`); if(sb) sb.onclick = () => { const src = (window.SONGS||{})[sb.dataset.song];
      try { if(VA && !VA.paused && VA.dataset && VA.dataset.song){ VA.pause(); sb.classList.remove('on'); return; } if(VA) VA.pause(); VA = new Audio(src); VA.dataset = {song: 1}; if(!MUTE){ VA.play().catch(()=>{}); sb.classList.add('on'); VA.onended = () => sb.classList.remove('on'); } } catch(e){} }; }
  if(s.t === 'mouth'){
    const seen = new Set(), tot = Object.keys(s.zones).length;
    $(`#mN${k}`).innerHTML = `<b>0</b> / ${tot}`;
    $$(`#mS${k} .mz`).forEach(z => z.onclick = () => { const Z = s.zones[z.dataset.z]; if(!Z) return; sfx('tap');
      $$(`#mS${k} .mz`).forEach(x => x.classList.toggle('mzon', x === z)); seen.add(z.dataset.z);
      z.classList.add('seen'); const hd = $(`#mS${k} .mhand`); if(hd) hd.remove();
      const lay = $(`#mS${k} .mlay`), zz = z.dataset.z; lay.querySelectorAll('.mlt.cur').forEach(e => e.classList.remove('cur'));
      const have = lay.querySelectorAll(`[data-z="${zz}"]`), fresh = !have.length;
      if(!fresh) have.forEach(e => e.classList.add('cur'));
      else (ZPOS[zz]||[]).forEach(([x, y, t], j) => lay.insertAdjacentHTML('beforeend', `<span class="mlt cur mseq" data-z="${zz}" dir="rtl" style="${mpos(x, y)}">${t.split(' ').map(c => `<i class="h">${c}</i>`).join(' ')}</span>`));
      const seq = [...lay.querySelectorAll(`[data-z="${zz}"] i`)], tok = ++MKQ;
      const step = j => { if(tok !== MKQ) return; seq.forEach(e => e.classList.remove('sing')); if(j >= seq.length) return;
        const e = seq[j]; e.classList.remove('h'); e.classList.add('sing'); const src = mkhSrc(e.textContent);
        if(src) mkhPlay(src, () => step(j+1)); else setTimeout(() => step(j+1), 450); };
      step(0);
      $(`#mP${k}`).innerHTML = `<div class="mg big"><span class="mg-t">${Z.n}</span><small>${Z.d}</small></div>`;
      $(`#mN${k}`).innerHTML = `<b>${seen.size}</b> / ${tot}`; if(seen.size >= s.need) award(i); });
  }
  if(s.t === 'order'){
    let n = 0; const P = $(`#ordP${k}`), S = $$(`#ordS${k} .ord-slot`);
    P.innerHTML = shuffle(s.items.map((it,j)=>[it,j])).map(([it,j]) => `<button class="ord-it" data-j="${j}">${it.html}<span>${it.label}</span></button>`).join('');
    $$(`#ordP${k} .ord-it`).forEach(b => b.onclick = () => {
      if(+b.dataset.j === n){ sfx('ok'); S[n].innerHTML = b.innerHTML; S[n].classList.add('done'); b.classList.add('used'); b.disabled = true; n++;
        if(n >= s.items.length){ const h = $(`#ordH${k}`); h.style.color = 'var(--sage)'; h.textContent = s.done; confetti(60); if(s.star) award(i); } }
      else shakeEl(b); });
  }
  if(s.t === 'quiz'){
    let n = 0; const order = shuffle(s.qs.map((_,j)=>j)).slice(0, s.pick || s.qs.length); const TOT = order.length;
    const draw = () => { if(!$(`#pqH${k}`) || PLs.screens[k] !== s) return; const Q = s.qs[order[n]]; $(`#pqH${k}`).textContent = ''; $(`#pqN${k}`).textContent = `Вопрос ${n+1} из ${TOT}`;
      $(`#pqQ${k}`).innerHTML = Q.q;
      if(Q.snd && !MUTE){ try { if(VA) VA.pause(); VA = new Audio(Q.snd); VA.play().catch(()=>{}); } catch(e){} }
      $(`#pqO${k}`).innerHTML = shuffle(Q.opts.map((o,j)=>[o,j])).map(([o,j]) => `<button class="card ${Q.pic?'pic':(Q.ar?'':'txt')}" data-j="${j}">${Q.ar ? g(o) : o}</button>`).join('');
      $$(`#pqO${k} .card`).forEach(c => c.onclick = () => { const h = $(`#pqH${k}`);
        if(+c.dataset.j === Q.ok){ sfx('ok'); c.classList.add('ok'); h.style.color = 'var(--sage)'; h.innerHTML = 'Правильно! Машаллах!' + (Q.why ? ' ' + Q.why : '');
          $$(`#pqO${k} .card`).forEach(x => x.disabled = true);
          n++; if(n >= TOT){ $(`#pqN${k}`).textContent = 'Все вопросы пройдены!'; if(s.star) award(i); } else setTimeout(draw, 1400); }
        else { shakeEl(c); h.style.color = 'var(--rose)'; h.textContent = 'Подумай ещё — у тебя получится!'; } }); };
    draw();
  }
  if(s.t === 'build'){
    let n = 0;
    const draw = () => { const W = s.items[n]; let pos = 0; $(`#pbH${k}`).textContent = ''; $(`#pbNext${k}`).hidden = true;
      $(`#pbN${k}`).textContent = `Слово ${n+1} из ${s.items.length}`; $(`#pbM${k}`).textContent = '«' + (W.ru.split(' — ')[1] || W.ru) + '»';
      $(`#pbW${k}`).innerHTML = W.parts.map((p,j)=>`<span class="pb-slot" data-j="${j}"></span>`).join('');
      $(`#pbP${k}`).innerHTML = shuffle(W.parts.map((p,j)=>[p,j])).map(([p,j]) => `<button class="card" data-j="${j}">${g(p)}</button>`).join('');
      $$(`#pbP${k} .card`).forEach(c => c.onclick = () => {
        if(+c.dataset.j === pos){ sfx('ok'); c.disabled = true; c.classList.add('ok'); $(`#pbW${k} [data-j="${pos}"]`).innerHTML = g(W.parts[pos]); pos++;
          if(pos === W.parts.length){ sfx('magic'); $(`#pbW${k}`).innerHTML = `<span class="pb-full">${g(W.word)}</span>`; bounceEl($(`#pbW${k}`));
            $(`#pbH${k}`).style.color = 'var(--sage)'; $(`#pbH${k}`).textContent = W.ru;
            if(n < s.items.length-1) $(`#pbNext${k}`).hidden = false; else { if(s.star) award(i); $(`#pbN${k}`).textContent = 'Все слова собраны!'; } } }
        else { shakeEl(c); $(`#pbH${k}`).style.color = 'var(--rose)'; $(`#pbH${k}`).textContent = 'Начинаем справа: какой слог идёт первым?'; } }); };
    $(`#pbNext${k}`).onclick = () => { n++; draw(); };
    draw();
  }
  if(s.t === 'examples'){
    $$('.pex-i').forEach(b => b.onclick = () => bounceEl(b));
    $(`#pexDone${k}`).onclick = () => { if(s.star) award(i); go(i+1); };
  }
  if(s.t === 'catch'){
    CLEAD = s.lead; CDONE = 'слова'; CSTEP = i;
    CPICK = () => { const hit = Math.random() < 0.5; return [rnd(hit ? s.hit : s.miss), hit]; };
    resetCatch(); $('#catchGo').onclick = startCatch;
  }
  if(s.t === 'snake'){
    const W = 9, H = 11, F = $(`#snF${k}`), NEED = 4;
    const ONE = LET.filter(l => l.ch.length === 1);
    let T, snake, dir, nd, items, eaten, timer = null;
    const free = () => { for(let t = 0; t < 200; t++){ const x = Math.floor(Math.random()*W), y = Math.floor(Math.random()*(H-1)); if(!snake.some(p => p[0]===x && p[1]===y) && !items.some(p => p.x===x && p.y===y) && Math.abs(x-snake[0][0]) + Math.abs(y-snake[0][1]) > 2) return [x, y]; } return [0, 0]; };
    const other = () => { const L = ONE.find(l => l.ch === T), pool = (L && L.sim && L.sim.length ? L.sim.concat(ONE.map(l => l.ch)) : ONE.map(l => l.ch)).filter(c => c !== T && c.length === 1); return pool[Math.floor(Math.random()*Math.min(pool.length, 8))]; };
    const pos = (x, y) => `left:${x/W*100}%;top:${y/H*100}%;width:${100/W}%;height:${100/H}%`;
    const draw = () => { F.querySelectorAll('.sn-c').forEach(e => e.remove());
      F.insertAdjacentHTML('beforeend', items.map(it => `<div class="sn-c sn-it" style="${pos(it.x, it.y)}">${g(it.c)}</div>`).join('') +
        snake.map((p, j) => `<div class="sn-c sn-s${j===0?' sn-h':''}" style="${pos(p[0], p[1])}"></div>`).join(''));
      $(`#snN${k}`).innerHTML = GT.g.eaten(eaten, NEED); };
    const round = () => { T = ONE[Math.floor(Math.random()*ONE.length)].ch; snake = [[4,6],[4,7],[4,8]]; dir = nd = [0,-1]; eaten = 0; items = [];
      for(let j = 0; j < NEED; j++){ const [x, y] = free(); items.push({x, y, c: T}); }
      for(let j = 0; j < 4; j++){ const [x, y] = free(); items.push({x, y, c: other()}); }
      $(`#snH${k}`).innerHTML = GT.g.snakeH(`<span class="arin">${T}</span>`); $(`#snHint${k}`).textContent = ''; draw(); };
    const stop = () => { clearInterval(timer); timer = null; };
    const tick = () => { dir = nd; const h = snake[0], nx = [(h[0]+dir[0]+W)%W, (h[1]+dir[1]+H)%H]; snake.unshift(nx);
      const hi = items.findIndex(it => it.x === nx[0] && it.y === nx[1]);
      if(hi >= 0){ const it = items.splice(hi, 1)[0];
        if(it.c === T){ eaten++; sfx('ok'); $(`#snHint${k}`).textContent = '';
          if(eaten >= NEED){ draw(); stop(); sfx('fanfare'); if(s.star) award(i); $(`#snO${k}`).hidden = false; $(`#snGo${k}`).textContent = GT.g.again; $(`#snHint${k}`).style.color = 'var(--sage)'; $(`#snHint${k}`).textContent = GT.done; return; } }
        else { sfx('boing'); snake.pop(); const [x, y] = free(); items.push({x, y, c: other()}); $(`#snHint${k}`).style.color = 'var(--rose)'; $(`#snHint${k}`).innerHTML = GT.g.notThis(`<span class="arin">${T}</span>`); } }
      else snake.pop();
      draw(); };
    const turn = d => { if(d[0] === -dir[0] && d[1] === -dir[1]) return; nd = d; };
    $$(`#snP${k} button`).forEach(b => b.onclick = () => { turn(b.dataset.d.split(',').map(Number)); if(!timer && $(`#snO${k}`).hidden) timer = setInterval(tick, 420); });
    let sx = 0, sy = 0;
    F.addEventListener('pointerdown', e => { sx = e.clientX; sy = e.clientY; });
    F.addEventListener('pointerup', e => { const dx = e.clientX - sx, dy = e.clientY - sy; if(Math.max(Math.abs(dx), Math.abs(dy)) < 18) return;
      turn(Math.abs(dx) > Math.abs(dy) ? [Math.sign(dx), 0] : [0, Math.sign(dy)]); });
    F.style.touchAction = 'none';
    $(`#snGo${k}`).onclick = () => { if(eaten >= NEED) round(); $(`#snO${k}`).hidden = true; stop(); timer = setInterval(tick, 420); sfx('tap'); };
    GAMESTOP = stop;
    round();
  }
  if(s.t === 'train'){
    const ONE = LET.filter(l => l.ch.length === 1), ROUNDS = 5; let r = 0, T, busy = false;
    const others = n => shuffle(ONE.map(l => l.ch).filter(c => c !== T)).slice(0, n);
    const LOCO = '<svg class="tr-loco" viewBox="0 0 90 70"><rect x="34" y="14" width="40" height="34" rx="6" fill="#C2563F"/><rect x="40" y="20" width="16" height="14" rx="3" fill="#E4EEF6"/><rect x="6" y="28" width="34" height="20" rx="8" fill="#245E86"/><rect x="12" y="12" width="9" height="18" rx="2" fill="#3A3F4A"/><circle cx="16" cy="8" r="5" fill="#fff" opacity=".8"/><circle cx="7" cy="2" r="4" fill="#fff" opacity=".6"/><rect x="2" y="44" width="76" height="6" rx="3" fill="#5C4033"/><circle cx="20" cy="56" r="9" fill="#3A3F4A"/><circle cx="56" cy="56" r="9" fill="#3A3F4A"/><circle cx="20" cy="56" r="3" fill="#CF9F45"/><circle cx="56" cy="56" r="3" fill="#CF9F45"/></svg>';
    const COL = ['#7FA2D6', '#E07F67', '#7E9A6A', '#CF9F45'];
    const round = () => { T = ONE[Math.floor(Math.random()*ONE.length)].ch; const w = shuffle([T, ...others(3)]); busy = false;
      $(`#trH${k}`).innerHTML = GT.g.trainH(`<span class="arin">${T}</span>`); $(`#trN${k}`).innerHTML = GT.g.round(r+1, ROUNDS); $(`#trHint${k}`).textContent = '';
      const tr = $(`#trT${k}`); tr.className = 'tr-train';
      tr.innerHTML = LOCO + w.map((c, j) => `<button class="tr-w" data-c="${c}" style="--wc:${COL[j]}">${g(c)}<i></i><i></i></button>`).join('');
      void tr.offsetWidth; tr.classList.add('in'); sfx('page');
      tr.querySelectorAll('.tr-w').forEach(b => b.onclick = () => { if(busy) return;
        if(b.dataset.c === T){ busy = true; sfx('ok'); b.classList.add('ok');
          setTimeout(() => { tr.classList.add('out'); }, 900);
          setTimeout(() => { r++; if(r < ROUNDS) round(); else { sfx('fanfare'); if(s.star) award(i); $(`#trH${k}`).innerHTML = GT.done; $(`#trT${k}`).innerHTML = ''; $(`#trA${k}`).innerHTML = `<button class="btn" id="trAg${k}">${GT.g.again}</button>`; $(`#trAg${k}`).onclick = () => { r = 0; $(`#trA${k}`).innerHTML = ''; round(); }; } }, 1700); }
        else { shakeEl(b); sfx('no'); $(`#trHint${k}`).style.color = 'var(--rose)'; $(`#trHint${k}`).innerHTML = GT.g.notThis(`<span class="arin">${T}</span>`); } }); };
    round();
  }
  if(s.t === 'basket'){
    const Z = {throat: 'ءهعحغخ', tongue: 'قكجشيضلنرتدطصسزثذظ', lips: 'فبمو'};
    const pick = (z, n) => shuffle([...Z[z]]).slice(0, n).map(c => [c, z]);
    let list, n, cnt;
    const show = () => { const c = $(`#bkL${k}`); c.classList.remove('in', 'fly'); void c.offsetWidth; c.innerHTML = g(list[n][0]); c.classList.add('in'); $(`#bkN${k}`).innerHTML = GT.g.sorted(n, list.length); };
    const start = () => { list = shuffle([...pick('throat', 3), ...pick('tongue', 3), ...pick('lips', 3)]); n = 0; cnt = {throat: 0, tongue: 0, lips: 0};
      $$(`section[data-s="${k}"] .bk-c`).forEach(e => e.textContent = '0'); $(`#bkA${k}`).innerHTML = ''; $(`#bkHint${k}`).textContent = ''; show(); };
    $$(`section[data-s="${k}"] .bk`).forEach(b => b.onclick = () => { if(n >= list.length) return; const [c, z] = list[n];
      if(b.dataset.z === z){ sfx('ok'); cnt[z]++; b.querySelector('.bk-c').textContent = cnt[z]; b.classList.remove('got'); void b.offsetWidth; b.classList.add('got');
        $(`#bkL${k}`).classList.add('fly'); $(`#bkHint${k}`).textContent = ''; n++;
        if(n >= list.length){ $(`#bkN${k}`).innerHTML = GT.g.sorted(n, list.length); sfx('fanfare'); if(s.star) award(i); $(`#bkL${k}`).innerHTML = '⭐'; $(`#bkHint${k}`).style.color = 'var(--sage)'; $(`#bkHint${k}`).textContent = GT.done;
          $(`#bkA${k}`).innerHTML = `<button class="btn" id="bkAg${k}">${GT.g.again}</button>`; $(`#bkAg${k}`).onclick = start; }
        else setTimeout(show, 450); }
      else { shakeEl(b); sfx('no'); $(`#bkHint${k}`).style.color = 'var(--rose)'; $(`#bkHint${k}`).textContent = GT.g.wrongZone(GT.g[z]); } });
    start();
  }
  if(s.t === 'memory'){
    const ONE = LET.filter(l => l.ch.length === 1).map(l => l.ch);
    let open = [], got = 0, lock = false;
    const start = () => { const four = shuffle(ONE.slice()).slice(0, 4); const cards = shuffle([...four, ...four]); open = []; got = 0; lock = false;
      $(`#meN${k}`).innerHTML = GT.g.pairs(0, 4); $(`#meA${k}`).innerHTML = '';
      $(`#mem${k}`).innerHTML = cards.map(c => `<button class="mc" data-c="${c}"><span class="mc-b"></span><span class="mc-f">${g(c)}</span></button>`).join('');
      $$(`#mem${k} .mc`).forEach(b => b.onclick = () => { if(lock || b.classList.contains('up')) return; b.classList.add('up'); sfx('tap'); open.push(b);
        if(open.length === 2){ const [a, c] = open; open = [];
          if(a.dataset.c === c.dataset.c){ sfx('ok'); a.classList.add('ok'); c.classList.add('ok'); got++; $(`#meN${k}`).innerHTML = GT.g.pairs(got, 4);
            if(got === 4){ sfx('fanfare'); if(s.star) award(i); $(`#meA${k}`).innerHTML = `<button class="btn" id="meAg${k}">${GT.g.again}</button>`; $(`#meAg${k}`).onclick = start; } }
          else { lock = true; setTimeout(() => { a.classList.remove('up'); c.classList.remove('up'); lock = false; }, 900); } } }); };
    start();
  }
  if(s.t === 'ayahs'){
    const total = s.ayahs.length, start = s.basm ? -1 : 0, body = $(`#musB${k}`);
    let n = start;
    const fit = () => { const sec = body.closest('section'); if(!sec || !sec.classList.contains('show')) return;
      const top = body.getBoundingClientRect().top, maxH = Math.max(220, innerHeight - top - 200);
      let lo = 16, hi = Math.min(46, innerWidth / 9);
      for(let t = 0; t < 12; t++){ const mid = (lo + hi) / 2; body.style.fontSize = mid + 'px'; if(body.scrollHeight <= maxH && body.scrollWidth <= body.clientWidth + 1) lo = mid; else hi = mid; }
      body.style.fontSize = lo + 'px'; };
    const SG = window.SONGS || {}, voiced = !!SG['a' + s.sura + '_1'];
    const playA = src => { if(!src) return; try { if(VA) VA.pause(); VA = new Audio(src); if(!MUTE) VA.play().catch(()=>{}); } catch(e){} };
    const wb = $(`#ayW${k}`); if(wb) wb.onclick = () => { if(VA && !VA.paused && wb.classList.contains('on')){ VA.pause(); wb.classList.remove('on'); return; }
      playA(SG['w' + s.sura]); if(VA && !MUTE){ wb.classList.add('on'); VA.onended = () => wb.classList.remove('on'); } };
    const sayA = () => { if(voiced){ if(wb) wb.classList.remove('on'); playA(SG['a' + s.sura + '_' + (n+1)]); } };
    const draw = () => {
      $$(`#musB${k} .ay`).forEach(e => e.classList.toggle('cur', +e.dataset.n === n));
      $(`#ayN${k}`).textContent = n === -1 ? GT.ay.basm : GT.ay.num(n+1, total);
      $(`#ayNext${k}`).textContent = n === -1 ? GT.ay.first : n < total-1 ? GT.ay.next : GT.ay.done;
      $(`#ayPrev${k}`).disabled = n === start;
      const c = body.querySelector('.ay.cur'); if(c) c.scrollIntoView({block: 'nearest', behavior: 'smooth'}); };
    $(`#ayNext${k}`).onclick = () => { if(n < total-1){ n++; sfx('page'); draw(); sayA(); } else { if(s.star) award(i); go(i+1); } };
    $(`#ayPrev${k}`).onclick = () => { if(n > start){ n--; draw(); sayA(); } };
    $$(`#musB${k} .ay`).forEach(e => e.onclick = () => { n = +e.dataset.n; if(!voiced) sfx('tap'); draw(); sayA(); });
    draw(); requestAnimationFrame(fit); setTimeout(fit, 400); if(document.fonts) document.fonts.ready.then(fit);
    addEventListener('resize', fit);
  }
  if(s.t === 'achieve'){
    const rows = [['Буквы', LET.map(l=>l.ch), 'l'], ['Огласовки', [0,1,2,3].map(x=>'h'+x)], ['Сукун и шадда', ['s0','s1']], ['Танвин', [0,1,2,3].map(x=>'t'+x)], ['Мадд', [0,1,2,3].map(x=>'m'+x)],
      ...PL.sections.slice(0,3).map((S,si)=>[S.title.replace(/^Раздел \d+\. /,''), S.lessons.map((_,li)=>'p'+si+'-'+li)])];
    $(`#ach${k}`).innerHTML = rows.map(([t, keys]) => { const done = keys.filter(x => (SAVE[x]||0) > 0).length;
      return `<div class="ach-r"><span>${t}</span><span class="ach-b"><i style="width:${Math.round(100*done/keys.length)}%"></i></span><b>${done} из ${keys.length}</b></div>`; }).join('');
    award(i);
  }
  if(s.t === 'diploma'){
    let nm = ''; try { nm = localStorage.getItem('rihlati-name') || ''; } catch(e){}
    const inp = $('#dipName'); inp.value = nm;
    const D = $(`#dip${k}`); if(s.sub){ D.querySelector('.dip-s').textContent = s.sub; } if(s.ar2){ D.querySelector('.dip-ar2').textContent = s.ar2; } if(s.txt){ D.querySelector('p').textContent = s.txt; }
    inp.oninput = () => { try { localStorage.setItem('rihlati-name', inp.value); } catch(e){} };
    $('#dipOk').onclick = () => { sfx('fanfare'); confetti(160); bounceEl($(`#dip${k}`)); award(i); };
  }
}
