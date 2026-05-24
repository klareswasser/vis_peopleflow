with open('pref_migration_ring.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace(
    '<span>${PREFS[oi]}<span style="color:#888">→</span>${name}</span>',
    '<span>${PREFS[oi]}<span style="color:rgba(235,235,245,0.4);font-size:0.8em;margin:0 4px">→</span>${name}</span>'
)
text = text.replace(
    '<span>${name}<span style="color:#888">→</span>${PREFS[di]}</span>',
    '<span>${name}<span style="color:rgba(235,235,245,0.4);font-size:0.8em;margin:0 4px">→</span>${PREFS[di]}</span>'
)

with open('pref_migration_ring.html', 'w', encoding='utf-8') as f:
    f.write(text)

