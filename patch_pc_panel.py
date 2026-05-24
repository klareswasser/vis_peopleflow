import re
with open('pref_migration_ring.html', 'r', encoding='utf-8') as f:
    text = f.read()

pc_css = """/* ── 詳細パネル ── */
  .stat-box{
    padding:0;
    margin-bottom:16px;
    background:transparent;
    border:none;
  }
  .stat-head{display:flex;justify-content:space-between;align-items:center;gap:10px;flex-wrap:wrap}
  .stat-head-l{display:flex;align-items:center;gap:10px;flex-wrap:wrap;min-width:0}
  .stat-name{font-size:1.7rem;font-weight:600;letter-spacing:-.02em;color:#fff}
  .stat-year-chip{font-size:.8rem;color:rgba(255,255,255,.9);background:rgba(255,255,255,.15);padding:3px 10px;border-radius:8px;font-weight:500;white-space:nowrap}
  .net-big{
    font-family:-apple-system,"SF Pro Display",sans-serif;
    font-size:1.6rem;font-weight:600;letter-spacing:-.02em;
    font-variant-numeric:tabular-nums;white-space:nowrap;
  }
  .net-big.pos{color:var(--pos)}
  .net-big.neg{color:var(--neg)}
  .net-cap{font-size:.6rem;color:var(--mute);letter-spacing:.2em;margin-top:-2px}
  .io-row{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:16px}
  .io-cell{background:rgba(255,255,255,.05);padding:14px 16px;border-radius:12px;text-align:center}
  .io-cap{font-size:.7rem;color:rgba(235,235,245,.6);margin-bottom:4px;font-weight:400;letter-spacing:0}
  .io-val{font-family:-apple-system,"SF Mono",monospace;font-size:1.15rem;font-weight:600;font-variant-numeric:tabular-nums;letter-spacing:-.01em}
  .io-val.pos{color:var(--pos-d)}
  .io-val.neg{color:var(--neg-d)}
  .flow-section{flex:1;min-height:0;display:flex;flex-direction:column;gap:8px}
  .flow-section h4{
    font-size:.75rem;color:rgba(235,235,245,.6);letter-spacing:0.02em;font-weight:600;
    display:flex;justify-content:space-between;padding:12px 2px 6px;
    border-bottom:1px solid rgba(255,255,255,.1);margin:0;
  }
  .flow-section h4.pos{color:var(--pos-d)}
  .flow-section h4.neg{color:var(--neg-d)}
  .flow-list{display:flex;flex-direction:column;gap:3px;max-height:180px;overflow-y:auto;background:transparent;border-radius:0;padding:0}
  .flow-list::-webkit-scrollbar{width:8px}
  .flow-list::-webkit-scrollbar-track{background:transparent}
  .flow-list::-webkit-scrollbar-thumb{background:rgba(255,255,255,.15);border:2px solid transparent;background-clip:padding-box;border-radius:999px}
  .flow-list::-webkit-scrollbar-thumb:hover{background:rgba(255,255,255,.25);border:2px solid transparent;background-clip:padding-box}
  .flow-row{position:relative;font-size:.85rem;padding:9px 12px;border-radius:8px;overflow:hidden;cursor:default;letter-spacing:-.01em;background:rgba(255,255,255,.02)}
  .flow-row .bar{position:absolute;left:0;top:0;bottom:0;opacity:.22}
  .flow-row .bar.pos{background:var(--pos)}
  .flow-row .bar.neg{background:var(--neg)}
  .flow-row .content{position:relative;display:flex;justify-content:space-between;align-items:center}
  .flow-row .v{font-family:-apple-system,"SF Mono",monospace;color:rgba(235,235,245,.9);font-variant-numeric:tabular-nums;font-weight:500}
  .placeholder{
    flex:1;display:flex;align-items:center;justify-content:center;text-align:center;
    color:rgba(235,235,245,.45);font-size:.9rem;line-height:1.7;
    background:rgba(255,255,255,.03);border:none;
    border-radius:14px;padding:36px 20px;font-weight:400;letter-spacing:0;
  }
"""

# We replace exactly from "/* ── 詳細パネル ── */" up to the line right before "/* スマホ用ヘッダー（PCでは非表示） */"
new_text = re.sub(r'/\* ── 詳細パネル ── \*/.*?(?=  /\* スマホ用ヘッダー（PCでは非表示） \*/)', pc_css, text, flags=re.DOTALL)

with open('pref_migration_ring.html', 'w', encoding='utf-8') as f:
    f.write(new_text)

