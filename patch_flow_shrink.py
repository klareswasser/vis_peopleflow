with open('pref_migration_ring.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace(
    '.flow-row{position:relative;',
    '.flow-row{position:relative;flex-shrink:0;white-space:nowrap;'
)
text = text.replace(
    'flex:0 0 360px;',
    'flex:0 0 380px;'
)

with open('pref_migration_ring.html', 'w', encoding='utf-8') as f:
    f.write(text)
