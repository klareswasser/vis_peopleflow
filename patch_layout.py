with open('/Users/hiroki/Library/CloudStorage/GoogleDrive-g.shimizu.hiroki@gmail.com/マイドライブ/02_Projects/分析_exp/02_アイデア/2605_都道府県人口移動円環/pref_migration_ring.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Update #stage to flex:none
text = re.sub(
    r'#stage\{height:100vw;min-height:0;aspect-ratio:1/1;padding:0\}',
    r'#stage{flex:none;height:100vw;min-height:0;aspect-ratio:1/1;padding:0}',
    text
)

# Update #panel to flex:1
text = re.sub(
    r'#panel\{\n\s*flex:none;width:auto;margin:0;border-radius:0;box-shadow:none;',
    r'#panel{\n      flex:1;width:auto;margin:0;border-radius:0;box-shadow:none;',
    text
)

with open('/Users/hiroki/Library/CloudStorage/GoogleDrive-g.shimizu.hiroki@gmail.com/マイドライブ/02_Projects/分析_exp/02_アイデア/2605_都道府県人口移動円環/pref_migration_ring.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("Mobile layout shift fixed")
