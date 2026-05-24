with open('/Users/hiroki/Library/CloudStorage/GoogleDrive-g.shimizu.hiroki@gmail.com/マイドライブ/02_Projects/分析_exp/02_アイデア/2605_都道府県人口移動円環/pref_migration_ring.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace("renderYear(YEARS[v]);", "renderYear(YEARS[v]);\n        updateYearTabs();")

with open('/Users/hiroki/Library/CloudStorage/GoogleDrive-g.shimizu.hiroki@gmail.com/マイドライブ/02_Projects/分析_exp/02_アイデア/2605_都道府県人口移動円環/pref_migration_ring.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("js patched")
