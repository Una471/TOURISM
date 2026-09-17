"""
Savannah Gates Hotel GABORONE - REVENUE & GUEST SATISFACTION DASHBOARD
Management dashboard with CLEAR TEXT COLORS.
Run: streamlit run 03_dashboard.py --server.port 8501
"""

import streamlit as st
from pathlib import Path
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

BASE_DIR = Path(__file__).resolve().parent


st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Red+Hat+Display:wght@500;600;700;800&family=Stack+Sans+Text:wght@400;500;600;700&display=swap');
html,body,[class*="css"]{font-family:'Inter',sans-serif;background:#f8f9fa;color:#212529;}
.topbar{background:linear-gradient(135deg,#e2ad59,#b77c29);color:white;padding:1.4rem 2rem;border-radius:12px;margin-bottom:1.5rem;}
.topbar h1{margin:0;font-size:1.5rem;font-weight:700;color:white;}
.topbar p{margin:.3rem 0 0;color:#fff;opacity:.9;font-size:.85rem;}
.kcard{background:white;border-radius:12px;padding:1.2rem 1.4rem;box-shadow:0 2px 10px rgba(0,0,0,.08);border-left:5px solid #dee2e6;margin-bottom:.4rem;}
.kcard.red{border-left-color:#d32f2f;} .kcard.orange{border-left-color:#f57c00;}
.kcard.green{border-left-color:#388e3c;} .kcard.blue{border-left-color:#1976d2;}
.kcard.gold{border-left-color:#e2ad59;}
.kval{font-size:1.9rem;font-weight:700;line-height:1.1;color:#212529;}
.klbl{font-size:.72rem;text-transform:uppercase;letter-spacing:1.5px;color:#6c757d;margin-top:.3rem;}
.ksub{font-size:.78rem;color:#495057;margin-top:.3rem;}
.ccard{background:white;border-radius:12px;padding:1.2rem 1.4rem;box-shadow:0 2px 10px rgba(0,0,0,.08);margin-bottom:1rem;}
.ctitle{font-size:.95rem;font-weight:600;color:#212529;margin-bottom:.2rem;}
.csub{font-size:.78rem;color:#6c757d;margin-bottom:.7rem;}
section[data-testid="stSidebar"]{background:#b77c29!important;}
section[data-testid="stSidebar"] *{color:#fff!important;}
#MainMenu,footer,header{visibility:hidden;}
/* Professional analytics console */
:root{--dash-bg:#0d0d14;--dash-side:#15151f;--dash-card:#1a1a24;--dash-card-2:#20202c;--dash-line:#2c2c3a;--dash-text:#f5f5f7;--dash-muted:#9a9aaa;--dash-accent:#e2ad59;--dash-soft:#f0cf94}
html,body,[class*="css"],.stApp{font-family:'Stack Sans Text','Red Hat Display','Segoe UI',sans-serif!important;background:var(--dash-bg)!important;color:var(--dash-text)!important}.stApp{background:radial-gradient(circle at 86% 0%,rgba(226,173,89,.08),transparent 30%),var(--dash-bg)!important}.block-container{max-width:1500px;padding:1.25rem 2rem 3rem!important}h1,h2,h3,h4,p,label,span{color:var(--dash-text)}h1,h2,h3,h4{font-family:'Red Hat Display','Segoe UI',sans-serif!important;letter-spacing:-.025em}
section[data-testid="stSidebar"]{width:228px!important;background:var(--dash-side)!important;border-right:1px solid var(--dash-line)!important}section[data-testid="stSidebar"]>div{padding:1.3rem .85rem!important}section[data-testid="stSidebar"] h3{font-size:1.05rem!important;margin:.2rem .55rem 0!important;color:#fff!important}section[data-testid="stSidebar"] p{color:var(--dash-muted)!important;font-size:.72rem!important}section[data-testid="stSidebar"] hr{border-color:var(--dash-line)!important;margin:1rem 0!important}section[data-testid="stSidebar"] div[role="radiogroup"]{gap:.3rem}section[data-testid="stSidebar"] div[role="radiogroup"] label{padding:.65rem .7rem!important;border-radius:7px!important;background:transparent!important;margin:0!important;transition:background .16s ease}section[data-testid="stSidebar"] div[role="radiogroup"] label:hover{background:var(--dash-card-2)!important}section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked){background:var(--dash-accent)!important}section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) p{color:#101018!important;font-weight:700!important}section[data-testid="stSidebar"] div[role="radiogroup"] label>div:first-child{display:none}section[data-testid="stSidebar"] [data-baseweb="select"]>div{background:var(--dash-card)!important;border-color:var(--dash-line)!important;color:#fff!important;border-radius:7px!important}section[data-testid="stSidebar"] svg{fill:var(--dash-muted)!important}
.topbar{position:relative;background:transparent!important;border:0!important;border-bottom:1px solid var(--dash-line)!important;border-radius:0!important;box-shadow:none!important;padding:.4rem 0 1rem!important;margin-bottom:1.1rem!important}.topbar:before{content:'ANALYTICS';display:block;color:var(--dash-accent);font-size:.58rem;letter-spacing:.18em;font-weight:700;margin-bottom:.45rem}.topbar h1{font-size:1.65rem!important;color:#fff!important}.topbar p{color:var(--dash-muted)!important;opacity:1!important;font-size:.73rem!important}
.kcard{min-height:118px;background:var(--dash-card)!important;border:1px solid var(--dash-line)!important;border-left:1px solid var(--dash-line)!important;border-top:3px solid var(--dash-accent)!important;border-radius:8px!important;box-shadow:none!important;padding:1rem 1.05rem!important;color:var(--dash-text)!important}.kcard.red{border-top-color:#ff6b6b!important}.kcard.orange{border-top-color:#f4a261!important}.kcard.green{border-top-color:#59d98e!important}.kcard.blue,.kcard.gold{border-top-color:var(--dash-accent)!important}.kval{font-family:'Red Hat Display','Segoe UI',sans-serif!important;font-size:1.75rem!important;color:#fff!important;font-variant-numeric:tabular-nums}.klbl{color:#d7d7df!important;font-size:.62rem!important;letter-spacing:.1em!important}.ksub{color:var(--dash-muted)!important;font-size:.66rem!important}
.ccard{background:var(--dash-card)!important;border:1px solid var(--dash-line)!important;border-radius:8px!important;box-shadow:none!important;padding:1rem!important}.ctitle{color:#fff!important;font-size:.86rem!important}.csub{color:var(--dash-muted)!important;font-size:.68rem!important}.ar,.ao,.ag{background:var(--dash-card)!important;border:1px solid var(--dash-line)!important;border-left:3px solid var(--dash-accent)!important;border-radius:7px!important;color:#dcdce4!important;line-height:1.5!important}.ar{border-left-color:#ff6b6b!important}.ao{border-left-color:#f4a261!important}.ag{border-left-color:#59d98e!important}.ar *,.ao *,.ag *{color:inherit!important}.ar b,.ao b,.ag b{color:#fff!important}
[data-testid="stPlotlyChart"]{background:var(--dash-card)!important;border:1px solid var(--dash-line);border-radius:8px;padding:.35rem}[data-testid="stDataFrame"]{border:1px solid var(--dash-line);border-radius:8px;overflow:hidden}.stSelectbox label p,.stMultiSelect label p,.stSlider label p{color:#d7d7df!important}.stAlert{background:var(--dash-card-2)!important;border-color:var(--dash-line)!important}.stAlert *{color:#eeeef3!important}hr{border-color:var(--dash-line)!important}#MainMenu,footer,header{visibility:hidden}@media(max-width:900px){.block-container{padding:1rem!important}.kcard{min-height:auto}section[data-testid="stSidebar"]{width:250px!important}}
section[data-testid='stSidebar'] h3:before{content:'';display:inline-block;width:9px;height:9px;background:var(--dash-accent);transform:rotate(45deg);margin-right:.55rem;border-radius:2px}.modebar{display:none!important}[data-testid='stPlotlyChart']:hover{border-color:rgba(255,255,255,.2)}[data-testid='stDataFrame']{background:var(--dash-card)!important}
/* Reference dashboard rebuild */
:root{--canvas:#0c0c13;--sidebar:#171720;--panel:#1b1b25;--panel-hover:#20202c;--stroke:#2b2b38;--ink:#f7f7fa;--muted:#a8a8b7}
html,body,.stApp,[class*="css"]{font-family:"Stack Sans Text","Segoe UI",Arial,sans-serif!important}.stApp{background:var(--canvas)!important}.block-container{max-width:1440px!important;padding:1.65rem 2.25rem 3rem!important}
section[data-testid="stSidebar"]{width:205px!important;background:var(--sidebar)!important;border-right:1px solid var(--stroke)!important}section[data-testid="stSidebar"]>div{padding:2.1rem 1rem!important}section[data-testid="stSidebar"] h3{font-family:"Stack Sans Text","Segoe UI",sans-serif!important;font-size:1.12rem!important;font-weight:720!important;line-height:1.18!important;letter-spacing:-.02em!important;margin:1.8rem .45rem .3rem!important}section[data-testid="stSidebar"] h3:before{width:8px!important;height:8px!important;margin-right:.55rem!important;border-radius:1px!important}section[data-testid="stSidebar"] p{font-size:.75rem!important;line-height:1.45!important;color:#aaaaba!important}section[data-testid="stSidebar"] hr{margin:1.15rem .25rem!important;border-color:var(--stroke)!important}section[data-testid="stSidebar"] div[role="radiogroup"]{gap:.28rem!important}section[data-testid="stSidebar"] div[role="radiogroup"] label{min-height:39px!important;padding:.6rem .72rem!important;border-radius:7px!important}section[data-testid="stSidebar"] div[role="radiogroup"] label p{font-size:.76rem!important;line-height:1.15!important;color:#bcbccc!important}section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked){background:var(--dash-accent)!important;box-shadow:0 5px 18px color-mix(in srgb,var(--dash-accent) 22%,transparent)!important}section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) p{color:#fff!important;font-weight:700!important}section[data-testid="stSidebar"] [data-baseweb="select"]>div{min-height:42px!important;border-radius:7px!important}
.topbar{padding:.1rem 0 1rem!important;margin:0 0 1.2rem!important;border-bottom:1px solid var(--stroke)!important}.topbar:before{display:none!important}.topbar h1{font-family:"Stack Sans Text","Segoe UI",sans-serif!important;font-size:1.65rem!important;font-weight:680!important;letter-spacing:-.035em!important;line-height:1.15!important}.topbar p{font-size:.78rem!important;line-height:1.5!important;margin-top:.5rem!important;color:var(--muted)!important}
[data-testid="stHorizontalBlock"]{gap:.78rem!important}.kcard{min-height:128px!important;display:flex!important;flex-direction:column!important;justify-content:center!important;padding:1.05rem 1.1rem!important;background:var(--panel)!important;border:1px solid var(--stroke)!important;border-top:1px solid var(--stroke)!important;border-radius:9px!important;position:relative!important;overflow:hidden!important}.kcard:before{content:"";position:absolute;inset:0 auto 0 0;width:3px;background:var(--dash-accent)}.kcard.red:before{background:#ff6969}.kcard.orange:before{background:#f0a34a}.kcard.green:before{background:#48cf8b}.kval{font-family:"Stack Sans Text","Segoe UI",sans-serif!important;font-size:1.85rem!important;font-weight:690!important;line-height:1!important;letter-spacing:-.045em!important}.klbl{margin-top:.7rem!important;font-size:.72rem!important;font-weight:680!important;line-height:1.25!important;letter-spacing:0!important;text-transform:none!important;color:#ededf2!important}.ksub{margin-top:.32rem!important;font-size:.68rem!important;line-height:1.35!important;color:var(--muted)!important}
.ccard{padding:1rem 1.05rem!important;margin:0 0 .7rem!important;background:var(--panel)!important;border:1px solid var(--stroke)!important;border-radius:9px 9px 0 0!important}.ctitle{font-size:.88rem!important;font-weight:680!important;line-height:1.3!important;letter-spacing:-.01em!important}.csub{margin-top:.35rem!important;font-size:.7rem!important;line-height:1.4!important;color:var(--muted)!important}[data-testid="stPlotlyChart"]{margin-top:-.72rem!important;padding:.35rem!important;background:var(--panel)!important;border:1px solid var(--stroke)!important;border-top:0!important;border-radius:0 0 9px 9px!important}.modebar{display:none!important}
h1,h2,h3,h4{font-family:"Stack Sans Text","Segoe UI",sans-serif!important}h2{font-size:1.35rem!important;font-weight:680!important;letter-spacing:-.025em!important;margin-top:1.4rem!important}p,li,label,[data-testid="stMarkdownContainer"]{line-height:1.5}.ar,.ao,.ag{padding:1rem!important;border-radius:8px!important;font-size:.76rem!important;line-height:1.55!important;background:var(--panel)!important}.stDataFrame,[data-testid="stDataFrame"]{font-size:.78rem!important;background:var(--panel)!important;border-color:var(--stroke)!important}.stAlert{border-radius:8px!important}.stSelectbox label p,.stMultiSelect label p,.stSlider label p{font-size:.72rem!important;text-transform:none!important;letter-spacing:0!important}
@media(max-width:900px){section[data-testid="stSidebar"]{width:245px!important}.block-container{padding:1rem!important}[data-testid="stHorizontalBlock"]{gap:.55rem!important}.kcard{min-height:105px!important}}
/* Single viewport dashboard proportions */
.block-container{max-width:none!important;padding:.8rem 1.55rem 1.3rem!important}.topbar{padding:0 0 .65rem!important;margin:0 0 .72rem!important}.topbar h1{font-size:1.38rem!important;line-height:1.1!important}.topbar p{font-size:.7rem!important;margin-top:.32rem!important}.topbar a,.topbar svg,a.header-anchor,[data-testid="stHeaderActionElements"]{display:none!important}
[data-testid="stHorizontalBlock"]{gap:.62rem!important}.kcard{min-height:88px!important;padding:.72rem .82rem!important;border-radius:8px!important}.kval{font-size:1.48rem!important}.klbl{font-size:.65rem!important;margin-top:.46rem!important}.ksub{font-size:.59rem!important;margin-top:.2rem!important}.ccard{padding:.68rem .8rem!important;margin:0 0 .55rem!important;min-height:48px!important}.ctitle{font-size:.75rem!important}.csub{font-size:.61rem!important;margin-top:.2rem!important}[data-testid="stPlotlyChart"]{margin-top:-.57rem!important;padding:.15rem!important}h2{font-size:1.12rem!important;margin:.75rem 0 .5rem!important}.ar,.ao,.ag{padding:.68rem .75rem!important;font-size:.67rem!important;line-height:1.4!important;margin-bottom:.35rem!important}hr{margin:.72rem 0!important}
section[data-testid="stSidebar"]{width:184px!important}section[data-testid="stSidebar"]>div{padding:1rem .75rem!important}section[data-testid="stSidebar"] h3{font-size:.93rem!important;margin:1rem .38rem .18rem!important}section[data-testid="stSidebar"] p{font-size:.62rem!important}section[data-testid="stSidebar"] hr{margin:.72rem .2rem!important}section[data-testid="stSidebar"] div[role="radiogroup"]{gap:.16rem!important}section[data-testid="stSidebar"] div[role="radiogroup"] label{min-height:32px!important;padding:.42rem .58rem!important}section[data-testid="stSidebar"] div[role="radiogroup"] label p{font-size:.64rem!important}section[data-testid="stSidebar"] div[role="radiogroup"] label:nth-child(1) p:before{content:"▦";margin-right:.5rem}section[data-testid="stSidebar"] div[role="radiogroup"] label:nth-child(2) p:before{content:"◫";margin-right:.5rem}section[data-testid="stSidebar"] div[role="radiogroup"] label:nth-child(3) p:before{content:"▤";margin-right:.5rem}section[data-testid="stSidebar"] div[role="radiogroup"] label:nth-child(4) p:before{content:"◎";margin-right:.5rem}section[data-testid="stSidebar"] div[role="radiogroup"] label:nth-child(5) p:before{content:"⌁";margin-right:.5rem}section[data-testid="stSidebar"] [data-baseweb="select"]>div{min-height:34px!important;font-size:.65rem!important}
[data-testid="stDataFrame"]{font-size:.68rem!important}@media(max-width:900px){.block-container{padding:.75rem!important}section[data-testid="stSidebar"]{width:235px!important}}
.csub{display:none!important}
/* Reference composition final */
.block-container{padding:1.35rem 2rem 2rem!important}.topbar{padding:.2rem 0 .8rem!important;margin-bottom:1rem!important}.topbar h1{font-size:1.65rem!important}.topbar p{font-size:.78rem!important}.kcard{min-height:112px!important;padding:1rem 1.05rem!important;border:0!important;border-radius:9px!important;background:#1c1c27!important}.kcard:before{display:none!important}.kval{font-size:1.72rem!important}.klbl{font-size:.73rem!important;margin-top:.65rem!important}.ksub{font-size:.66rem!important}.ccard{min-height:auto!important;padding:.85rem 1rem!important;border:0!important;border-radius:9px 9px 0 0!important;background:#1c1c27!important}.ctitle{font-size:.86rem!important}[data-testid="stPlotlyChart"]{border:0!important;border-radius:0 0 9px 9px!important;background:#1c1c27!important;padding:.25rem .6rem!important}section[data-testid="stSidebar"]{width:220px!important}section[data-testid="stSidebar"]>div{padding:1.5rem 1rem!important}section[data-testid="stSidebar"] h3{font-size:1.05rem!important}section[data-testid="stSidebar"] p{font-size:.7rem!important}section[data-testid="stSidebar"] div[role="radiogroup"] label{min-height:38px!important;padding:.58rem .7rem!important}section[data-testid="stSidebar"] div[role="radiogroup"] label p{font-size:.72rem!important}section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked){background:#f5f5f7!important;box-shadow:none!important}section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) p{color:#14141d!important}div[data-testid="stVerticalBlock"]{gap:.55rem!important}[data-testid="stExpander"]{border:1px solid #2b2b38!important;background:#171720!important;border-radius:8px!important}
/* Accessible colour and interaction */
.kcard{transition:transform .16s ease,background .16s ease!important;border-top:2px solid var(--dash-accent)!important}.kcard:hover{transform:translateY(-2px)!important;background:#22222e!important}.kcard.red{border-top-color:#ff6b72!important}.kcard.orange{border-top-color:#f3b64b!important}.kcard.green{border-top-color:#4fcf91!important}.kcard.blue,.kcard.gold{border-top-color:var(--dash-accent)!important}[data-testid="stPlotlyChart"]{transition:background .16s ease!important}[data-testid="stPlotlyChart"]:hover{background:#1e1e2a!important}.stSelectbox [data-baseweb="select"]>div:focus-within{border-color:var(--dash-accent)!important}
/* Power BI KPI cards */
.kcard{min-height:108px!important;display:flex!important;flex-direction:column!important;justify-content:flex-start!important;background:#191922!important;border:1px solid #30303c!important;border-radius:5px!important;padding:.9rem 1rem .82rem!important;box-shadow:0 1px 2px rgba(0,0,0,.16)!important;transform:none!important;transition:background .12s ease,border-color .12s ease!important}.kcard:hover{transform:none!important;background:#1d1d27!important;border-color:#414152!important}.kcard:before,.kcard:after{display:none!important}.klbl{order:1!important;display:flex!important;align-items:center!important;gap:.48rem!important;margin:0!important;color:#c9c9d3!important;font-size:.7rem!important;font-weight:560!important;line-height:1.25!important;letter-spacing:0!important;text-transform:none!important}.klbl:before{content:"";width:6px;height:6px;flex:0 0 6px;border-radius:50%;background:var(--dash-accent)}.kcard.red .klbl:before{background:#f06b72}.kcard.orange .klbl:before{background:#e9aa49}.kcard.green .klbl:before{background:#4bc589}.kcard.blue .klbl:before,.kcard.gold .klbl:before{background:var(--dash-accent)}.kval{order:2!important;margin:.5rem 0 0!important;color:#f8f8fb!important;font-family:"Stack Sans Text","Segoe UI",sans-serif!important;font-size:1.72rem!important;font-weight:650!important;line-height:1!important;letter-spacing:-.035em!important;font-variant-numeric:tabular-nums!important;white-space:nowrap!important}.ksub{order:3!important;margin-top:auto!important;padding-top:.5rem!important;color:#8f8f9e!important;font-size:.61rem!important;font-weight:450!important;line-height:1.2!important;white-space:nowrap!important;overflow:hidden!important;text-overflow:ellipsis!important}
.cross-app-link{position:fixed;top:1rem;right:1.7rem;z-index:9999;display:inline-flex;align-items:center;justify-content:center;padding:.55rem .85rem;background:#f5f5f7;color:#15151f!important;border:1px solid #f5f5f7;border-radius:5px;font:600 .72rem "Stack Sans Text","Segoe UI",sans-serif;text-decoration:none!important;box-shadow:0 2px 8px rgba(0,0,0,.18)}.cross-app-link:hover{background:var(--dash-accent);border-color:var(--dash-accent);color:#fff!important}</style>
""", unsafe_allow_html=True)

def load():
    bookings = pd.read_csv(BASE_DIR / "daily_bookings_analyzed.csv", parse_dates=["date"])
    reviews  = pd.read_csv(BASE_DIR / "guest_reviews_analyzed.csv", parse_dates=["date"])
    staffing = pd.read_csv(BASE_DIR / "staffing_data_analyzed.csv", parse_dates=["date"])
    return bookings, reviews, staffing

bookings, reviews, staffing = load()

with st.sidebar:
    st.markdown("###  Savannah Gates Hotel")
    st.markdown("Management Dashboard")
    st.markdown("---")
    page = st.radio("Go to", [
        "  Revenue Overview",
        "  Guest Satisfaction",
        "  Staffing Optimization",
        "  Pricing Strategy",
    ])
    st.markdown("---")
    st.caption("Data: Full Year 2025")

def kcard(color, val, lbl, sub=""):
    return f'<div class="kcard {color}"><div class="klbl">{lbl}</div><div class="kval">{val}</div>{"<div class=ksub>"+sub+"</div>" if sub else ""}</div>'

def wchart(fig, h=230):
    palette = ['#DCA552','#E8795B','#4F9EAD','#8A7BC8']
    for i, trace in enumerate(fig.data):
        if trace.type == "bar":
            point_count = len(trace.x) if trace.x is not None else len(trace.y)
            trace.marker.color = ([palette[j % len(palette)] for j in range(point_count)]
                                  if len(fig.data) == 1 else palette[i % len(palette)])
            trace.marker.line = dict(width=0)
            trace.opacity = 0.94
            trace.hovertemplate = "%{x}<br><b>%{y}</b><extra></extra>"
        elif trace.type in ("scatter", "scattergl"):
            trace.line.color = palette[i % len(palette)]
            trace.line.width = 2.5
            if getattr(trace, "marker", None):
                trace.marker.color = palette[i % len(palette)]
                trace.marker.size = 6
        elif trace.type == "pie":
            trace.marker.colors = palette
            trace.textinfo = "percent"
            trace.textposition = "outside"
    fig.update_layout(plot_bgcolor="#1b1b25", paper_bgcolor="#1b1b25", font_color="#d8d8e2", font=dict(family="Stack Sans Text, Segoe UI, sans-serif",size=11), height=h, margin=dict(t=12,b=18,l=8,r=8), coloraxis_showscale=False, hovermode="closest", legend=dict(orientation="h",yanchor="bottom",y=1.02,xanchor="right",x=1,font=dict(size=10),bgcolor="rgba(0,0,0,0)"), hoverlabel=dict(bgcolor="#272735",bordercolor="#3a3a4a",font=dict(color="#ffffff",size=12)))
    fig.update_xaxes(showgrid=False,linecolor="#343443",tickfont=dict(color="#a8a8b7",size=10),title=None,automargin=True,zeroline=False)
    fig.update_yaxes(gridcolor="#2b2b38",linecolor="#343443",tickfont=dict(color="#a8a8b7",size=10),title=None,automargin=True,zeroline=False)
    return fig

if page == "  Revenue Overview":
    st.markdown('<div class="topbar"><h1> Revenue Overview</h1><p>Savannah Gates Hotel Gaborone | Annual Performance 2025</p></div>', unsafe_allow_html=True)
    
    total_rev = bookings["daily_revenue_bwp"].sum()
    monthly_rev = total_rev / 12
    avg_occ = bookings["occupancy_rate_pct"].mean()
    avg_rate = bookings["avg_room_rate_bwp"].mean()
    optimized_monthly = monthly_rev * 1.12
    
    c1,c2,c3,c4,c5 = st.columns(5)
    c1.markdown(kcard("gold", f"P{total_rev/1e6:.2f}M","Annual Revenue","Full year 2025"), unsafe_allow_html=True)
    c2.markdown(kcard("blue", f"P{monthly_rev:,.0f}","Monthly Average","Current"), unsafe_allow_html=True)
    c3.markdown(kcard("green", f"P{optimized_monthly:,.0f}","With Optimization","12% increase"), unsafe_allow_html=True)
    c4.markdown(kcard("orange", f"{avg_occ:.1f}%","Avg Occupancy",""), unsafe_allow_html=True)
    c5.markdown(kcard("blue", f"P{avg_rate:.0f}","Avg Room Rate","Per night"), unsafe_allow_html=True)
    
    st.markdown("---")
    col1,col2 = st.columns(2)
    with col1:
        st.markdown('<div class="ccard"><div class="ctitle"> Monthly Revenue Trend</div><div class="csub">Shows seasonal patterns and peak periods</div>', unsafe_allow_html=True)
        monthly = bookings.groupby(bookings["date"].dt.to_period("M"))["daily_revenue_bwp"].sum().reset_index()
        monthly["Month"] = monthly["date"].astype(str)
        monthly["label"] = monthly["daily_revenue_bwp"].apply(lambda x: f"P{x/1e3:.0f}K")
        fig = px.bar(monthly, x="Month", y="daily_revenue_bwp", color="daily_revenue_bwp",
                     color_continuous_scale=["#f0cf94","#e2ad59"], text="label",
                     labels={"daily_revenue_bwp":"Revenue (BWP)"})
        fig.update_traces(textposition="outside")
        fig.update_layout(showlegend=False)
        st.plotly_chart(wchart(fig), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="ccard"><div class="ctitle"> Occupancy Rate by Day of Week</div><div class="csub">Weekends consistently higher than weekdays</div>', unsafe_allow_html=True)
        dow = bookings.groupby("day_of_week")["occupancy_rate_pct"].mean().reindex(
            ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]).reset_index()
        dow["label"] = dow["occupancy_rate_pct"].apply(lambda x: f"{x:.0f}%")
        fig2 = px.bar(dow, x="day_of_week", y="occupancy_rate_pct", color="occupancy_rate_pct",
                      color_continuous_scale=["#f5e7cc","#e2ad59"], text="label",
                      labels={"occupancy_rate_pct":"Occupancy %","day_of_week":""})
        fig2.update_traces(textposition="outside")
        fig2.update_layout(showlegend=False)
        st.plotly_chart(wchart(fig2), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

elif page == "  Guest Satisfaction":
    st.markdown('<div class="topbar"><h1> Guest Satisfaction Report</h1><p>Reviews from all platforms in one view</p></div>', unsafe_allow_html=True)
    
    avg_rating = reviews["rating"].mean()
    total_reviews = len(reviews)
    positive = (reviews["sentiment"]=="Positive").sum()
    negative = (reviews["sentiment"]=="Negative").sum()
    
    c1,c2,c3,c4 = st.columns(4)
    c1.markdown(kcard("gold", f"{avg_rating:.2f}/5.0","Average Rating","All platforms"), unsafe_allow_html=True)
    c2.markdown(kcard("blue", f"{total_reviews}","Total Reviews","12 months"), unsafe_allow_html=True)
    c3.markdown(kcard("green", f"{positive}","Positive",f"{positive/total_reviews*100:.0f}%"), unsafe_allow_html=True)
    c4.markdown(kcard("red", f"{negative}","Negative",f"{negative/total_reviews*100:.0f}%"), unsafe_allow_html=True)
    
    st.markdown("---")
    col1,col2 = st.columns(2)
    with col1:
        st.markdown('<div class="ccard"><div class="ctitle"> Rating Distribution</div>', unsafe_allow_html=True)
        rating_dist = reviews["rating"].value_counts().sort_index(ascending=False).reset_index()
        rating_dist.columns = ["Rating","Count"]
        rating_dist["Stars"] = rating_dist["Rating"].apply(lambda x: ""*x)
        fig = px.bar(rating_dist, x="Stars", y="Count", color="Rating",
                     color_continuous_scale=["#e74c3c","#f0cf94"], text="Count")
        fig.update_traces(textposition="outside")
        fig.update_layout(showlegend=False)
        st.plotly_chart(wchart(fig), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="ccard"><div class="ctitle"> Reviews by Platform</div>', unsafe_allow_html=True)
        platform = reviews.groupby("platform").agg(
            count=("review_id","count"), avg_rating=("rating","mean")).sort_values("count",ascending=False).reset_index()
        fig2 = px.bar(platform, x="platform", y="count", color="avg_rating",
                      color_continuous_scale=["#e74c3c","#f0cf94"], text="count",
                      labels={"count":"Number of Reviews","platform":"","avg_rating":"Avg Rating"})
        fig2.update_traces(textposition="outside")
        st.plotly_chart(wchart(fig2), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

elif page == "  Staffing Optimization":
    st.markdown('<div class="topbar"><h1> Staffing & Labor Cost</h1><p>Optimizing staff schedules based on occupancy</p></div>', unsafe_allow_html=True)
    
    total_cost = staffing["daily_cost_bwp"].sum()
    overstaffed = staffing["overstaffed"].sum()
    waste = overstaffed * 200 * 0.15
    savings = waste * 0.65
    
    c1,c2,c3,c4 = st.columns(4)
    c1.markdown(kcard("blue", f"P{total_cost/1e6:.2f}M","Annual Labor Cost","All roles"), unsafe_allow_html=True)
    c2.markdown(kcard("orange", f"{overstaffed}","Overstaffed Shifts","Out of 1,825"), unsafe_allow_html=True)
    c3.markdown(kcard("red", f"P{waste:,.0f}","Current Waste","From overstaffing"), unsafe_allow_html=True)
    c4.markdown(kcard("green", f"P{savings:,.0f}","Potential Savings","With predictor"), unsafe_allow_html=True)
    
    st.markdown("---")
    col1,col2 = st.columns(2)
    with col1:
        st.markdown('<div class="ccard"><div class="ctitle"> Labor Cost by Role</div>', unsafe_allow_html=True)
        role_cost = staffing.groupby("role")["daily_cost_bwp"].sum().sort_values(ascending=False).reset_index()
        role_cost["label"] = role_cost["daily_cost_bwp"].apply(lambda x: f"P{x/1e3:.0f}K")
        fig = px.bar(role_cost, x="role", y="daily_cost_bwp", color="daily_cost_bwp",
                     color_continuous_scale=["#c6f6d5","#e2ad59"], text="label",
                     labels={"daily_cost_bwp":"Annual Cost","role":""})
        fig.update_traces(textposition="outside")
        fig.update_layout(showlegend=False)
        st.plotly_chart(wchart(fig), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="ccard"><div class="ctitle"> Occupancy vs Staff Levels</div>', unsafe_allow_html=True)
        daily_staff = staffing.groupby("date").agg(
            rooms=("rooms_occupied","first"), total_staff=("actual_staff","sum")).reset_index()
        fig2 = px.scatter(daily_staff, x="rooms", y="total_staff", trendline="ols",
                          labels={"rooms":"Rooms Occupied","total_staff":"Total Staff on Duty"})
        st.plotly_chart(wchart(fig2), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

elif page == "  Pricing Strategy":
    st.markdown('<div class="topbar"><h1> Dynamic Pricing Strategy</h1><p>Optimizing rates based on demand and events</p></div>', unsafe_allow_html=True)
    
    col1,col2 = st.columns(2)
    with col1:
        st.markdown('<div class="ccard"><div class="ctitle"> Price vs Occupancy</div>', unsafe_allow_html=True)
        fig = px.scatter(bookings, x="occupancy_rate_pct", y="avg_room_rate_bwp",
                         color="event_boost", color_continuous_scale=["#c6f6d5","#e2ad59"],
                         labels={"occupancy_rate_pct":"Occupancy %","avg_room_rate_bwp":"Avg Rate","event_boost":"Event Boost"})
        st.plotly_chart(wchart(fig), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="ccard"><div class="ctitle"> Event Impact on Revenue</div>', unsafe_allow_html=True)
        bookings["Has Event"] = bookings["event_boost"].apply(lambda x: "Event Days" if x > 1.0 else "Normal Days")
        event_comp = bookings.groupby("Has Event")["daily_revenue_bwp"].mean().reset_index()
        fig2 = px.bar(event_comp, x="Has Event", y="daily_revenue_bwp", color="Has Event",
                      color_discrete_map={"Event Days":"#e2ad59","Normal Days":"#6c757d"},
                      labels={"daily_revenue_bwp":"Avg Daily Revenue"})
        st.plotly_chart(wchart(fig2), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.markdown("<div style='text-align:center;color:#6c757d;font-size:.78rem'>Cresta Lodge Gaborone | Management Dashboard | Unaswi Leonard | 2026</div>", unsafe_allow_html=True)
