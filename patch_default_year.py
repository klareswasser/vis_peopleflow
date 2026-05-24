with open('/Users/hiroki/Library/CloudStorage/GoogleDrive-g.shimizu.hiroki@gmail.com/マイドライブ/02_Projects/分析_exp/02_アイデア/2605_都道府県人口移動円環/pref_migration_ring.html', 'r', encoding='utf-8') as f:
    text = f.read()

old_slider = """  // ── スライダー ──
  slider.max=YEARS.length-1;
  slider.value=YEARS.length-1;
  slider.addEventListener('input',()=>{
    renderYear(YEARS[+slider.value]);
    updateYearTabs();
  });"""

new_slider = """  // ── スライダー ──
  let defaultIdx = YEARS.indexOf(2025);
  if (defaultIdx === -1) defaultIdx = YEARS.length - 1;
  slider.max = YEARS.length - 1;
  slider.value = defaultIdx;
  slider.addEventListener('input',()=>{
    renderYear(YEARS[+slider.value]);
    updateYearTabs();
  });"""

text = text.replace(old_slider, new_slider)

old_init = """  // 初期描画
  renderYear(YEARS[YEARS.length-1]);
  updateYearTabs();"""

new_init = """  // 初期描画
  renderYear(YEARS[defaultIdx]);
  updateYearTabs();"""

text = text.replace(old_init, new_init)

with open('/Users/hiroki/Library/CloudStorage/GoogleDrive-g.shimizu.hiroki@gmail.com/マイドライブ/02_Projects/分析_exp/02_アイデア/2605_都道府県人口移動円環/pref_migration_ring.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("done")
