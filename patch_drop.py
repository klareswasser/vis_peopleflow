with open('/Users/hiroki/Library/CloudStorage/GoogleDrive-g.shimizu.hiroki@gmail.com/マイドライブ/02_Projects/分析_exp/02_アイデア/2605_都道府県人口移動円環/pref_migration_ring.html', 'r', encoding='utf-8') as f:
    text = f.read()

old_css = """  /* ── 年選択タブ ── */
  .year-tabs {
    position: absolute;
    top: 24px;
    right: 24px;
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 6px;
    width: 180px;
    z-index: 10;
  }
  .year-tab {
    background: rgba(255,255,255,.05);
    border: .5px solid rgba(255,255,255,.1);
    color: rgba(235,235,245,.6);
    font-size: .7rem;
    font-family: -apple-system, "SF Mono", monospace;
    padding: 6px 0;
    text-align: center;
    border-radius: 8px;
    cursor: pointer;
    transition: .15s;
    backdrop-filter: saturate(150%) blur(10px);
    -webkit-backdrop-filter: saturate(150%) blur(10px);
  }
  .year-tab:hover { background: rgba(255,255,255,.15); color: #fff; }
  .year-tab.active { background: #fff; color: #000; font-weight: 600; box-shadow: 0 2px 6px rgba(0,0,0,.4); border-color: transparent; }"""

new_css = """  /* ── 年セレクター (ビヨーンと出る) ── */
  .year-selector {
    position: absolute;
    top: 24px;
    right: 24px;
    z-index: 20;
    width: 110px;
    font-family: -apple-system, "SF Mono", monospace;
  }
  .year-selector-current {
    background: rgba(255,255,255,.08);
    border: .5px solid rgba(255,255,255,.15);
    color: #fff;
    padding: 10px 14px;
    border-radius: 12px;
    text-align: center;
    font-size: 1.1rem;
    font-weight: 700;
    cursor: pointer;
    backdrop-filter: saturate(150%) blur(12px);
    -webkit-backdrop-filter: saturate(150%) blur(12px);
    box-shadow: 0 4px 12px rgba(0,0,0,.2);
    display: flex;
    justify-content: space-between;
    align-items: center;
    transition: all .2s ease;
  }
  .year-selector-current:hover {
    background: rgba(255,255,255,.15);
  }
  .year-selector-current::after {
    content: '▼';
    font-size: .7rem;
    opacity: 0.8;
    transition: transform .3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  }
  .year-selector.open .year-selector-current::after {
    transform: rotate(180deg);
  }
  .year-selector-list {
    position: absolute;
    top: calc(100% + 8px);
    left: 0;
    width: 100%;
    background: rgba(20,20,30,.85);
    border: .5px solid rgba(255,255,255,.1);
    border-radius: 12px;
    backdrop-filter: saturate(200%) blur(20px);
    -webkit-backdrop-filter: saturate(200%) blur(20px);
    box-shadow: 0 8px 24px rgba(0,0,0,.5);
    
    /* Animation (ビヨーン) */
    opacity: 0;
    visibility: hidden;
    transform: translateY(-10px) scale(0.95);
    transform-origin: top center;
    transition: all 0.35s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    
    display: flex;
    flex-direction: column;
    max-height: 280px;
    overflow-y: auto;
    scrollbar-width: none;
  }
  .year-selector-list::-webkit-scrollbar { display: none; }
  .year-selector.open .year-selector-list {
    opacity: 1;
    visibility: visible;
    transform: translateY(0) scale(1);
  }
  .year-item {
    padding: 10px 0;
    color: rgba(235,235,245,.7);
    font-size: .95rem;
    cursor: pointer;
    text-align: center;
    transition: background .15s, color .15s;
    border-bottom: .5px solid rgba(255,255,255,.05);
  }
  .year-item:last-child { border-bottom: none; }
  .year-item:hover {
    background: rgba(255,255,255,.1);
    color: #fff;
  }
  .year-item.active {
    color: #000;
    background: #fff;
    font-weight: 700;
    box-shadow: 0 2px 6px rgba(0,0,0,.2) inset;
  }"""

if old_css in text:
    text = text.replace(old_css, new_css)
else:
    print("CSS failed to replace")

old_mobile = """    .year-tabs {
      top: 12px; right: 0; left: 0; width: 100%; box-sizing: border-box;
      display: flex; flex-wrap: nowrap; overflow-x: auto;
      padding: 0 16px; justify-content: flex-start;
      -webkit-overflow-scrolling: touch; scrollbar-width: none;
    }
    .year-tabs::-webkit-scrollbar { display: none; }
    .year-tab { flex: 0 0 auto; padding: 6px 14px; font-size: .8rem; }"""

new_mobile = """    .year-selector {
      top: 12px;
      right: 16px;
      width: 100px;
    }"""

if old_mobile in text:
    text = text.replace(old_mobile, new_mobile)
else:
    print("Mobile CSS failed to replace")
    
old_html = """  <div id="stage">
    <div id="year-tabs" class="year-tabs"></div>"""
    
new_html = """  <div id="stage">
    <div id="year-selector" class="year-selector">
      <div id="year-selector-current" class="year-selector-current"></div>
      <div id="year-selector-list" class="year-selector-list"></div>
    </div>"""

text = text.replace(old_html, new_html)

old_js = """  // ── 年選択タブの生成 ──
  const yearTabsContainer = document.getElementById('year-tabs');
  YEARS.forEach((y, i) => {
    const btn = document.createElement('div');
    btn.className = 'year-tab';
    btn.textContent = y;
    btn.addEventListener('click', () => {
      slider.value = i;
      renderYear(y);
      updateYearTabs();
    });
    yearTabsContainer.appendChild(btn);
  });
  function updateYearTabs() {
    Array.from(yearTabsContainer.children).forEach((btn, i) => {
      btn.classList.toggle('active', i === +slider.value);
    });
  }"""

new_js = """  // ── 年セレクターの生成 ──
  const yearSelector = document.getElementById('year-selector');
  const yearCurrent = document.getElementById('year-selector-current');
  const yearList = document.getElementById('year-selector-list');

  YEARS.forEach((y, i) => {
    const item = document.createElement('div');
    item.className = 'year-item';
    item.textContent = y;
    item.addEventListener('click', (e) => {
      slider.value = i;
      renderYear(y);
      updateYearTabs();
      yearSelector.classList.remove('open');
      e.stopPropagation();
    });
    yearList.appendChild(item);
  });

  yearCurrent.addEventListener('click', (e) => {
    yearSelector.classList.toggle('open');
    e.stopPropagation();
  });

  document.addEventListener('click', (e) => {
    if(!yearSelector.contains(e.target)){
      yearSelector.classList.remove('open');
    }
  });

  function updateYearTabs() {
    yearCurrent.textContent = YEARS[+slider.value];
    Array.from(yearList.children).forEach((item, i) => {
      item.classList.toggle('active', i === +slider.value);
    });
  }"""

if old_js in text:
    text = text.replace(old_js, new_js)
else:
    print("JS failed to replace")

with open('/Users/hiroki/Library/CloudStorage/GoogleDrive-g.shimizu.hiroki@gmail.com/マイドライブ/02_Projects/分析_exp/02_アイデア/2605_都道府県人口移動円環/pref_migration_ring.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("Patch applied to html.")
