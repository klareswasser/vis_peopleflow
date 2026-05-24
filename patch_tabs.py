import re
with open('/Users/hiroki/Library/CloudStorage/GoogleDrive-g.shimizu.hiroki@gmail.com/マイドライブ/02_Projects/分析_exp/02_アイデア/2605_都道府県人口移動円環/pref_migration_ring.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add CSS
css = """
  /* ── 年選択タブ ── */
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
  .year-tab.active { background: #fff; color: #000; font-weight: 600; box-shadow: 0 2px 6px rgba(0,0,0,.4); border-color: transparent; }
"""
text = text.replace("/* ── SVG ── */", css + "\n  /* ── SVG ── */")

# Mobile CSS override
mobile_css = """
    #stage{height:100vw;min-height:0;aspect-ratio:1/1;padding:0}
    
    .year-tabs {
      top: 12px; right: 0; left: 0; width: 100vw;
      display: flex; flex-wrap: nowrap; overflow-x: auto;
      padding: 0 16px; justify-content: flex-start;
      -webkit-overflow-scrolling: touch; scrollbar-width: none;
    }
    .year-tabs::-webkit-scrollbar { display: none; }
    .year-tab { flex: 0 0 auto; padding: 6px 14px; font-size: .8rem; }
"""
text = text.replace("#stage{height:100vw;min-height:0;aspect-ratio:1/1;padding:0}", mobile_css)

# 2. Add HTML
html = """<div id="stage">
    <div id="year-tabs" class="year-tabs"></div>"""
text = text.replace('<div id="stage">', html)

# 3. Add JS
# Need to populate #year-tabs and update them
js = """
  // ── スライダー ──
  slider.max=YEARS.length-1;
  slider.value=YEARS.length-1;
  slider.addEventListener('input',()=>{
    renderYear(YEARS[+slider.value]);
    updateYearTabs();
  });

  // ── 年選択タブの生成 ──
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
  }
"""

text = text.replace("""  // ── スライダー ──
  slider.max=YEARS.length-1;
  slider.value=YEARS.length-1;
  slider.addEventListener('input',()=>{
    renderYear(YEARS[+slider.value]);
  });""", js)

text = text.replace("renderYear(YEARS[YEARS.length-1]);", "renderYear(YEARS[YEARS.length-1]);\n  updateYearTabs();")

with open('/Users/hiroki/Library/CloudStorage/GoogleDrive-g.shimizu.hiroki@gmail.com/マイドライブ/02_Projects/分析_exp/02_アイデア/2605_都道府県人口移動円環/pref_migration_ring.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("Patched!")
