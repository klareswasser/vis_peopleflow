with open('/Users/hiroki/Library/CloudStorage/GoogleDrive-g.shimizu.hiroki@gmail.com/マイドライブ/02_Projects/分析_exp/02_アイデア/2605_都道府県人口移動円環/pref_migration_ring.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace(
    '<span class="stat-region">${reg}　${year}年</span>',
    '<span class="stat-year-chip">${year}年</span>'
)

old_css1 = '.stat-region{font-size:.78rem;color:rgba(235,235,245,.55);letter-spacing:0;font-weight:400;white-space:nowrap}'
new_css1 = '.stat-year-chip{font-size:.75rem;color:rgba(255,255,255,.9);background:rgba(255,255,255,.15);padding:3px 8px;border-radius:6px;letter-spacing:0;font-weight:500;white-space:nowrap}'
text = text.replace(old_css1, new_css1)

old_css2 = '.stat-region{font-size:.8rem;color:rgba(235,235,245,.55);letter-spacing:0;font-weight:400}'
new_css2 = '.stat-year-chip{font-size:.75rem;padding:3px 8px;border-radius:6px;}'
text = text.replace(old_css2, new_css2)

with open('/Users/hiroki/Library/CloudStorage/GoogleDrive-g.shimizu.hiroki@gmail.com/マイドライブ/02_Projects/分析_exp/02_アイデア/2605_都道府県人口移動円環/pref_migration_ring.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("Updated stat region to year chip")
