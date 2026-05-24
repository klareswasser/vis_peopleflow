import re
with open('pref_migration_ring.html', 'r', encoding='utf-8') as f:
    text = f.read()

mob_css = """/* 詳細カード＝フラット */
    .stat-box{
      background:transparent;
      border:none;
      padding:0;
      margin-bottom:12px;
    }
    .stat-head{gap:8px}
    .stat-head-l{gap:8px}
    .stat-name{font-size:1.5rem;font-weight:600;letter-spacing:-.02em;color:#fff}
    .stat-year-chip{font-size:.75rem;padding:3px 8px;border-radius:6px;}
    .net-big{
      font-size:1.4rem !important;font-weight:600;letter-spacing:-.02em;
    }
    .io-row{gap:10px;margin-top:14px}
    .io-cell{background:rgba(255,255,255,.06);padding:12px 10px;border-radius:10px}
    .io-cap{font-size:.7rem;margin-bottom:6px;}
    .io-val{font-size:1.05rem;}
    /* フロー一覧 */
    .flow-section{gap:12px;margin-top:12px}
    .flow-section h4{
      font-size:.75rem;padding:8px 2px 6px;
    }
    .flow-list{max-height:none;background:transparent;border-radius:0;padding:0;gap:3px;}
    .flow-row{
      font-size:.9rem;padding:11px 12px;border-radius:8px;background:rgba(255,255,255,.02);
    }
    .flow-row + .flow-row{border-top:none}"""

text = re.sub(r'/\* 詳細カード＝iOS グループドセル \*/.*?(?=    #controls{)', mob_css + "\n", text, flags=re.DOTALL)

with open('pref_migration_ring.html', 'w', encoding='utf-8') as f:
    f.write(text)

