"""
CRESTA LODGE — HOTEL MANAGEMENT SYSTEM
Daily pricing, booking, and review tool. CLEAR TEXT COLORS.
Run: streamlit run 04_software.py --server.port 8502
"""

import streamlit as st
import pandas as pd
from datetime import datetime, date, timedelta

st.set_page_config(page_title="Cresta Lodge | System", page_icon="🏨", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
html,body,[class*="css"]{font-family:'Inter',sans-serif;background:#f8f9fa;color:#212529;}
.topbar{background:linear-gradient(135deg,#d4af37,#c5a028);color:white;padding:1.2rem 1.5rem;border-radius:12px;margin-bottom:1.2rem;}
.topbar h1{margin:0;font-size:1.4rem;color:white;}
.topbar p{margin:.2rem 0 0;color:#fff;opacity:.9;font-size:.82rem;}
.kcard{background:white;border-radius:10px;padding:1.1rem 1.3rem;box-shadow:0 2px 10px rgba(0,0,0,.08);border-top:3px solid #dee2e6;margin-bottom:.3rem;}
.kcard.gold{border-top-color:#d4af37;} .kcard.green{border-top-color:#388e3c;} .kcard.blue{border-top-color:#1976d2;}
.kval{font-size:1.8rem;font-weight:700;color:#212529;}
.klbl{font-size:.7rem;text-transform:uppercase;letter-spacing:1.5px;color:#6c757d;margin-top:.3rem;}
.ksub{font-size:.76rem;color:#495057;margin-top:.3rem;}
section[data-testid="stSidebar"]{background:#c5a028!important;}
section[data-testid="stSidebar"] *{color:#fff!important;}
.stButton>button{background:#d4af37;color:white;border:none;border-radius:8px;padding:.6rem 1.5rem;font-weight:600;}
#MainMenu,footer,header{visibility:hidden;}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load():
    bookings = pd.read_csv("daily_bookings_analyzed.csv", parse_dates=["date"])
    reviews  = pd.read_csv("guest_reviews_analyzed.csv", parse_dates=["date"])
    return bookings, reviews

bookings, reviews = load()

with st.sidebar:
    st.markdown("## 🏨 Hotel System")
    st.markdown("*Cresta Lodge Gaborone*")
    st.markdown("---")
    nav = st.radio("Go to", ["💰 Pricing Calculator","⭐ Review Dashboard","📊 Today's Status"])
    st.markdown("---")

def kcard(color, val, lbl, sub=""):
    return f'<div class="kcard {color}"><div class="kval">{val}</div><div class="klbl">{lbl}</div>{"<div class=ksub>"+sub+"</div>" if sub else ""}</div>'

if nav == "💰 Pricing Calculator":
    st.markdown('<div class="topbar"><h1>💰 Dynamic Pricing Calculator</h1><p>Get optimal room rates based on demand and events</p></div>', unsafe_allow_html=True)
    
    col1,col2 = st.columns(2)
    with col1:
        check_in = st.date_input("Check-In Date", value=date.today())
        room_type = st.selectbox("Room Type", ["Standard","Deluxe","Executive Suite","Family Room"])
        current_occ = st.slider("Current Occupancy %", 0, 100, 65)
    
    with col2:
        local_event = st.checkbox("Local Event / Holiday?")
        is_weekend = check_in.weekday() >= 5
        st.info(f"{'🎉 Weekend' if is_weekend else '📅 Weekday'}")
    
    base_rates = {"Standard":850,"Deluxe":1250,"Executive Suite":2100,"Family Room":1450}
    base = base_rates[room_type]
    multiplier = 1.0
    
    if current_occ > 85: multiplier = 1.20
    elif current_occ > 70: multiplier = 1.10
    elif current_occ < 50: multiplier = 0.90
    
    if local_event: multiplier *= 1.15
    if is_weekend: multiplier *= 1.08
    
    optimal_rate = round(base * multiplier, 2)
    
    st.markdown(f"""
    <div style="background:#fff3cd;border:2px solid #d4af37;border-radius:12px;padding:2rem;text-align:center;margin:1rem 0;">
        <div style="font-size:2.5rem;font-weight:800;color:#d4af37">P{optimal_rate:,.2f}</div>
        <div style="color:#6c757d;margin-top:.5rem">Recommended Rate per Night</div>
        <div style="color:#495057;font-size:.85rem;margin-top:.5rem">Base: P{base} × {multiplier:.2f} multiplier</div>
    </div>
    """, unsafe_allow_html=True)

elif nav == "⭐ Review Dashboard":
    st.markdown('<div class="topbar"><h1>⭐ Guest Reviews — All Platforms</h1><p>Centralized view of all guest feedback</p></div>', unsafe_allow_html=True)
    
    recent = reviews.sort_values("date", ascending=False).head(20)
    for _, r in recent.iterrows():
        sentiment_color = "green" if r["sentiment"]=="Positive" else "red" if r["sentiment"]=="Negative" else "orange"
        stars = "⭐" * r["rating"]
        st.markdown(f"""
        <div style="background:white;border-left:4px solid {'#388e3c' if sentiment_color=='green' else '#d32f2f' if sentiment_color=='red' else '#f57c00'};
                    border-radius:8px;padding:1rem;margin:.5rem 0;">
            <div><b>{stars}</b> · {r['platform']} · {r['date'].strftime('%Y-%m-%d')}</div>
            <div style="font-size:.9rem;color:#495057;margin-top:.3rem">{r['comment']}</div>
            {f"<div style='font-size:.8rem;color:#d32f2f;margin-top:.3rem'>Issues: {r['issues']}</div>" if r['issues'] != 'None' else ''}
        </div>
        """, unsafe_allow_html=True)

elif nav == "📊 Today's Status":
    st.markdown('<div class="topbar"><h1>📊 Today\'s Operations</h1><p>Current occupancy and revenue</p></div>', unsafe_allow_html=True)
    
    today = bookings.iloc[-1]
    c1,c2,c3 = st.columns(3)
    c1.markdown(kcard("gold", f"{today['rooms_occupied']}/90","Rooms Occupied",f"{today['occupancy_rate_pct']:.0f}%"), unsafe_allow_html=True)
    c2.markdown(kcard("green", f"P{today['daily_revenue_bwp']:,.0f}","Today's Revenue",""), unsafe_allow_html=True)
    c3.markdown(kcard("blue", f"{today['staff_on_duty']}","Staff on Duty",""), unsafe_allow_html=True)

st.markdown("---")
st.markdown("<div style='text-align:center;color:#6c757d;font-size:.78rem'>Cresta Lodge Gaborone · Unaswi Leonard · 2026</div>", unsafe_allow_html=True)
