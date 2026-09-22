"""
Savannah Gates Hotel - HOTEL MANAGEMENT SYSTEM
Daily pricing, booking, and review tool. CLEAR TEXT COLORS.
Run: streamlit run 04_software.py --server.port 8502
"""

import streamlit as st

# Respect report links even when Streamlit Cloud starts this file directly.
if st.query_params.get("view") == "dashboard":
    import runpy
    from pathlib import Path
    runpy.run_path(str(Path(__file__).resolve().parent / "03_dashboard.py"), run_name="__main__")
    st.stop()
import pandas as pd
import base64
from pathlib import Path
from datetime import datetime, date, timedelta

BASE_DIR = Path(__file__).resolve().parent


st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Momo+Trust+Display&family=Red+Hat+Display:wght@500;600;700;800&family=Stack+Sans+Text:wght@400;500;600;700&display=swap');
:root{--night:#162a25;--teal:#175568;--coral:#9b4934;--gold:#c5822f;--sand:#f1e5d5;--paper:#fbf7ef;--ink:#1d302b;--muted:#596762;--line:#d4cabb}
html,body,[class*="css"],input,button,select{font-family:'Work Sans',sans-serif!important;color:var(--ink)}.stApp{background:var(--paper)}.block-container{max-width:1200px;padding:0 2.4rem 3rem}h1,h2,h3{font-family:'Syne',sans-serif!important;color:var(--ink);font-weight:600;letter-spacing:-.045em}
.masthead{display:flex;align-items:center;justify-content:space-between;padding:1rem 0}.brand{border-left:5px solid var(--gold);padding:.18rem 0 .18rem .85rem}.brand strong{font-family:'Syne',sans-serif;font-size:1.18rem;color:var(--night);letter-spacing:-.04em;font-weight:700}.brand small{display:block;color:#596762;font-size:.52rem;letter-spacing:.17em;text-transform:uppercase;margin-top:.15rem}.meta{font-size:.58rem;letter-spacing:.15em;text-transform:uppercase;color:#596762}.meta span{color:var(--coral);margin-left:1rem}
.destination-hero{height:455px;background-size:cover;background-position:center;position:relative;display:flex;justify-content:flex-start;padding:2.8rem}.hero-copy{text-align:left;max-width:650px}.hero-copy .eyebrow{font-size:.61rem;letter-spacing:.17em;text-transform:uppercase;color:#f1c77c;font-weight:600}.hero-copy h1{font-size:3.25rem;line-height:.96;color:#fff;margin:.6rem 0 .8rem;text-shadow:0 2px 15px rgba(0,0,0,.4)}.hero-copy p{color:#f5eadc;font-size:.8rem;max-width:430px;line-height:1.55}.trust{position:absolute;right:2rem;bottom:1.8rem;display:grid;gap:.45rem}.trust div{background:rgba(241,229,213,.93);backdrop-filter:blur(8px);padding:.7rem .9rem;min-width:190px;color:var(--night);font-size:.66rem;border-left:4px solid var(--gold)}.trust b{display:block;font-family:'Syne',sans-serif;font-size:.72rem;letter-spacing:-.02em}
.nav-label{text-align:center;font-size:.57rem;letter-spacing:.16em;text-transform:uppercase;color:#687678;font-weight:700;margin:1.2rem 0 .4rem}div[data-testid="stRadio"]>div{justify-content:center;gap:.35rem;background:rgba(255,255,255,.88);border:1px solid var(--line);padding:.4rem;margin-bottom:1.3rem}div[data-testid="stRadio"] label{padding:.65rem 1.2rem;margin:0!important}div[data-testid="stRadio"] label:has(input:checked){background:var(--night)}div[data-testid="stRadio"] label p{font-size:.73rem;font-weight:600;color:#385056!important;white-space:nowrap}div[data-testid="stRadio"] label:has(input:checked) p{color:#fff!important}div[data-testid="stRadio"] div[role="radiogroup"]>label>div:first-child{display:none}
.topbar{background:var(--sand);padding:1.55rem 1.8rem;border-left:5px solid var(--gold);margin-bottom:1.1rem}.topbar h1{margin:0;font-size:1.75rem;color:var(--night)}.topbar p{margin:.4rem 0 0;color:var(--muted);font-size:.75rem}.kcard{background:#fff;padding:1.15rem 1.3rem;border:1px solid var(--line);margin-bottom:.3rem}.kcard.gold{border-top:4px solid var(--gold)}.kcard.green{border-top:4px solid var(--teal)}.kcard.blue{border-top:4px solid #607e86}.kval{font-family:'Syne',sans-serif;font-size:1.75rem;font-weight:600;color:var(--night);letter-spacing:-.05em}.klbl{font-size:.61rem;text-transform:uppercase;letter-spacing:1.35px;color:#3e5550;margin-top:.4rem;font-weight:600}.ksub{font-size:.7rem;color:var(--muted);margin-top:.3rem}
section[data-testid="stSidebar"]{display:none!important}.stButton>button{background:var(--coral);color:#fff;border:0;border-radius:2px;padding:.65rem 1.3rem;font-weight:700}.stButton>button *{color:#fff!important}.stTextInput input,.stNumberInput input{border-radius:2px!important}#MainMenu,footer,header{visibility:hidden}@media(max-width:800px){.block-container{padding:0 1rem 2rem}.destination-hero{height:380px}.hero-copy h1{font-size:2.1rem}.trust{right:1rem;left:1rem;grid-template-columns:1fr 1fr}.meta{display:none}div[data-testid="stRadio"]>div{justify-content:flex-start;overflow-x:auto}}
div[data-testid="stAlert"]{background:#dcebf5!important;border:1px solid #b8d1df!important;border-radius:6px!important}div[data-testid="stAlert"] *{color:#173f4a!important;font-weight:600!important}.stDateInput label,.stSelectbox label,.stSlider label,.stCheckbox label{color:#243e43!important;font-weight:600!important}.stCheckbox label p{color:#243e43!important}.stSlider [data-testid="stTickBar"]{color:#52686c!important}
.topbar p{font-size:.75rem!important}
.workspace-intro{display:flex;align-items:end;justify-content:space-between;margin:1.65rem 0 .7rem}.workspace-intro .eyebrow{font-size:.56rem;letter-spacing:.17em;text-transform:uppercase;color:var(--coral);font-weight:600}.workspace-intro h2{font-size:1.45rem;margin:.2rem 0 0}.workspace-intro p{font-size:.68rem;color:var(--muted);margin:0;max-width:390px;text-align:right}
div[data-testid="stRadio"]>div{display:grid!important;grid-template-columns:repeat(3,1fr);gap:8px!important;background:transparent!important;border:0!important;padding:0!important}div[data-testid="stRadio"] label{position:relative;min-height:76px;padding:1.65rem 1rem .65rem!important;background:#fff;border:1px solid var(--line);transition:transform .18s ease,border-color .18s ease,background .18s ease}div[data-testid="stRadio"] label:before{position:absolute;top:.6rem;left:1rem;font-size:.52rem;letter-spacing:.14em;color:var(--gold);font-weight:600}div[data-testid="stRadio"] label:nth-child(1):before{content:"01 · REVENUE"}div[data-testid="stRadio"] label:nth-child(2):before{content:"02 · EXPERIENCE"}div[data-testid="stRadio"] label:nth-child(3):before{content:"03 · OPERATIONS"}div[data-testid="stRadio"] label:hover{transform:translateY(-2px);border-color:#a99a86}div[data-testid="stRadio"] label:has(input:checked){background:var(--night);border-color:var(--night);box-shadow:0 8px 22px rgba(22,42,37,.15)}div[data-testid="stRadio"] label:has(input:checked):before{color:#efbd6b}div[data-testid="stRadio"] label p{font-family:'Syne',sans-serif!important;font-size:.78rem!important;letter-spacing:-.02em}
.topbar{margin-top:1.4rem;box-shadow:inset 0 1px rgba(255,255,255,.5)}.stDateInput>div,.stSelectbox>div{margin-bottom:.55rem}.stDateInput input,.stSelectbox div[data-baseweb="select"]>div{background:#fff!important;border:1px solid #c9bda9!important;border-radius:3px!important;min-height:44px}.stSlider{padding:.45rem 0}.stCheckbox{background:#f3eadf;padding:.65rem .8rem;border-left:3px solid var(--gold);margin-bottom:.7rem}.stCheckbox label{margin:0}.rate-card{background:linear-gradient(110deg,#efe1cf,#f7efe5);border:1px solid #dac5a8;border-left:6px solid var(--gold);padding:2rem;text-align:left;margin:1.2rem 0;display:grid;grid-template-columns:1fr auto;align-items:center}.rate-card .rate-label{font-size:.59rem;letter-spacing:.15em;text-transform:uppercase;color:#675b4c;font-weight:600}.rate-card .rate-value{font-family:'Syne',sans-serif;font-size:2.45rem;font-weight:600;letter-spacing:-.07em;color:var(--night)}.rate-card .rate-detail{text-align:right;font-size:.72rem;color:#56645f}.rate-card .rate-detail b{display:block;color:var(--night);font-size:.82rem;margin-bottom:.25rem}
.review-card{background:#fff;border:1px solid var(--line);padding:1rem 1.15rem;margin:.55rem 0;display:grid;grid-template-columns:110px 1fr;gap:1rem}.review-card.positive{border-left:5px solid #47765c}.review-card.negative{border-left:5px solid #9b4934}.review-card.neutral{border-left:5px solid var(--gold)}.review-score{font-family:'Syne',sans-serif;font-size:1.25rem;font-weight:600;color:var(--night)}.review-source{font-size:.62rem;color:var(--muted);margin-top:.2rem}.review-comment{font-size:.82rem;color:#304943;line-height:1.55}.review-issue{font-size:.7rem;color:#8a382a;margin-top:.4rem;font-weight:500}.kcard{min-height:145px;padding:1.35rem;box-shadow:0 9px 24px rgba(29,48,43,.05)}.kval{font-size:2rem}.klbl{margin-top:.65rem}.block-container>hr{margin-top:2rem!important}
@media(max-width:800px){.workspace-intro{display:block}.workspace-intro p{text-align:left;margin-top:.4rem}div[data-testid="stRadio"]>div{grid-template-columns:1fr!important}.rate-card{grid-template-columns:1fr}.rate-card .rate-detail{text-align:left;margin-top:.7rem}.review-card{grid-template-columns:1fr}.trust{display:none}}
/* Portfolio typography: expressive brand, editorial headings, highly legible UI. */
html,body,[class*="css"],p,label,input,button,select,textarea{font-family:'Stack Sans Text','Segoe UI',sans-serif!important}
h1,h2,h3,h4,.topbar h1,.workspace-intro h2{font-family:'Red Hat Display','Segoe UI',sans-serif!important;letter-spacing:-.035em}
.brand strong{font-family:'Momo Trust Display','Red Hat Display',sans-serif!important;letter-spacing:.01em}
.hero-copy h1{font-family:'Red Hat Display','Segoe UI',sans-serif!important;font-weight:700;letter-spacing:-.055em}
.kval,.rate-value,.review-score{font-family:'Red Hat Display','Segoe UI',sans-serif!important;font-variant-numeric:tabular-nums}
button,div[data-testid="stRadio"] label p,.eyebrow,.meta,.rate-label,.klbl{font-family:'Stack Sans Text','Segoe UI',sans-serif!important}
.destination-hero{height:330px}.workspace-note{display:flex;justify-content:space-between;gap:1.2rem;align-items:center;background:#efe4d6;border-left:4px solid var(--gold);padding:.8rem 1rem;margin:.2rem 0 .85rem}.workspace-note b{font-size:.78rem}.workspace-note span{font-size:.72rem;color:var(--muted)}div[data-testid="stRadio"]{position:sticky;top:0;z-index:50;background:rgba(251,247,239,.96);padding:.35rem 0;backdrop-filter:blur(10px)}input:focus,button:focus,[data-baseweb="select"]:focus-within{outline:3px solid rgba(197,130,47,.24)!important;outline-offset:2px}.data-hint{font-size:.72rem;color:var(--muted);margin:.2rem 0 .8rem}
.topbar p{max-width:720px!important;font-size:.84rem!important;line-height:1.55!important;color:#465852!important}.rate-card *,.review-card *,.kcard *,.workspace-note *{opacity:1!important}.stAlert,.stAlert *{color:#173f4a!important}.stTextInput label p,.stNumberInput label p,.stSelectbox label p,.stMultiSelect label p,.stCheckbox label p,.stDateInput label p,.stSlider label p{color:#203c3a!important;font-size:.82rem!important}.composition{display:grid;grid-template-columns:160px 1fr;gap:1rem;padding:1rem 1.2rem;background:#efe4d6;border-left:4px solid var(--gold);margin:.8rem 0}.composition b{font-size:.72rem;text-transform:uppercase;letter-spacing:.1em;color:#8a5320}.composition p{margin:0;max-width:760px;color:#465852;line-height:1.55;font-size:.82rem}@media(max-width:700px){.composition,.workspace-note{grid-template-columns:1fr;display:grid}}
#MainMenu,footer,header{visibility:hidden;}
.workspace-note b{color:#603d18!important;opacity:1!important;font-weight:700!important}.workspace-note span{color:#40514c!important;opacity:1!important}
.cross-app-link{position:fixed;top:1rem;right:1.7rem;z-index:9999;display:inline-flex;align-items:center;justify-content:center;padding:.62rem 1rem;background:#11131a;color:#fff!important;border:1px solid rgba(255,255,255,.18);border-radius:5px;font:650 .78rem "Stack Sans Text","Segoe UI",sans-serif;text-decoration:none!important;box-shadow:0 3px 12px rgba(0,0,0,.18)}.cross-app-link:hover{filter:brightness(1.12)}</style>
""", unsafe_allow_html=True)

@st.cache_data
def load():
    bookings = pd.read_csv(BASE_DIR / "daily_bookings_analyzed.csv", parse_dates=["date"])
    reviews  = pd.read_csv(BASE_DIR / "guest_reviews_analyzed.csv", parse_dates=["date"])
    return bookings, reviews

@st.cache_data(show_spinner=False)
def load_image_b64(filename):
    return base64.b64encode((Path(__file__).parent / "assets" / filename).read_bytes()).decode("ascii")

bookings, reviews = load()
hero_b64 = load_image_b64("savannah-hero.webp")
if "rate_history" not in st.session_state: st.session_state.rate_history = []
if "review_actions" not in st.session_state: st.session_state.review_actions = {}

st.markdown(f"""
<div class="masthead"><div class="brand"><strong>Savannah Gates</strong><small>Hospitality operations · Botswana</small></div><div class="meta">Revenue <span>Guest experience</span></div></div>
<div class="destination-hero" style="background-image:linear-gradient(180deg,rgba(12,36,40,.48),rgba(12,36,40,.08) 55%,rgba(12,36,40,.28)),url('data:image/webp;base64,{hero_b64}')">
  <div class="hero-copy"><div class="eyebrow">Hospitality intelligence for every stay</div><h1>Better Rates. Better Stays.<br>One Clear View.</h1><p>Set confident room prices, listen to every guest and keep today’s operation in view.</p></div>
  <div class="trust"><div><b>Daily pricing</b>Demand-aware room recommendations</div><div><b>Guest voice</b>Reviews gathered across platforms</div><div><b>Live operations</b>Occupancy, revenue and staffing</div></div>
</div><div class="workspace-intro"><div><div class="eyebrow">Operations workspace</div><h2>What would you like to manage?</h2></div><p>Move between revenue decisions, guest feedback and today’s operating position.</p></div>
""", unsafe_allow_html=True)

st.markdown('<div class="workspace-note"><b>Hospitality action workspace</b><span>Set room rates and review individual guest feedback here. Use the separate dashboard for revenue and experience trends.</span></div>', unsafe_allow_html=True)
nav = st.radio("Hotel operations", ["Room pricing", "Guest reviews", "Today’s status"], horizontal=True, label_visibility="collapsed")

def kcard(color, val, lbl, sub=""):
    return f'<div class="kcard {color}"><div class="kval">{val}</div><div class="klbl">{lbl}</div>{"<div class=ksub>"+sub+"</div>" if sub else ""}</div>'

if nav == "Room pricing":
    st.markdown('<div class="topbar"><h1>Room Rate Recommendation</h1><p>Set a nightly rate using occupancy, calendar demand and local events.</p></div>', unsafe_allow_html=True)
    
    col1,col2 = st.columns(2)
    with col1:
        check_in = st.date_input("Check-In Date", value=date.today())
        room_type = st.selectbox("Room Type", ["Standard","Deluxe","Executive Suite","Family Room"])
        current_occ = st.slider("Current Occupancy %", 0, 100, 65)
    
    with col2:
        local_event = st.checkbox("Local Event / Holiday?")
        is_weekend = check_in.weekday() >= 5
        st.info("Weekend demand period" if is_weekend else "Weekday demand period")
    
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
    <div class="rate-card">
        <div><div class="rate-label">Recommended nightly rate</div><div class="rate-value">P{optimal_rate:,.2f}</div></div>
        <div class="rate-detail"><b>{room_type} room</b>Base P{base:,.0f} × {multiplier:.2f} demand multiplier</div>
    </div>
    """, unsafe_allow_html=True)
    reasons = []
    if current_occ > 85: reasons.append("occupancy above 85%")
    elif current_occ > 70: reasons.append("occupancy above 70%")
    elif current_occ < 50: reasons.append("occupancy below 50%")
    else: reasons.append("occupancy within the normal band")
    if is_weekend: reasons.append("weekend demand")
    if local_event: reasons.append("a local event or holiday")
    difference = optimal_rate - base
    direction = "above" if difference > 0 else "below" if difference < 0 else "equal to"
    st.info(f"Why this rate: {', '.join(reasons)}. It is P{abs(difference):,.2f} {direction} the base rate.")
    st.markdown('<div class="composition"><b>Decision step</b><p>Accept the recommendation or enter an override. The calculated rate remains visible so the final decision can always be compared with the original recommendation.</p></div>', unsafe_allow_html=True)
    d1, d2 = st.columns([1, 1.4])
    with d1:
        accepted_rate = st.number_input("Final nightly rate (BWP)", min_value=1.0, value=float(optimal_rate), step=50.0)
    with d2:
        override_reason = st.text_input("Reason for override", placeholder="Required only when changing the recommendation")
    override_valid = accepted_rate == optimal_rate or bool(override_reason.strip())
    if not override_valid:
        st.caption("Explain why the final rate differs from the recommendation.")
    if st.button("Record pricing decision", use_container_width=True, disabled=not override_valid):
        entry = {"recorded_at": datetime.now().strftime("%d %b %Y, %H:%M"), "stay_date": str(check_in), "room": room_type, "recommended_rate": optimal_rate, "final_rate": accepted_rate, "reason": override_reason or "Recommendation accepted"}
        st.session_state.rate_history.append(entry)
        st.success(f"Rate decision recorded: {room_type}, {check_in:%d %b %Y}, P{accepted_rate:,.2f}.")
    if st.session_state.rate_history:
        with st.expander(f"Pricing decision history ({len(st.session_state.rate_history)})"):
            st.dataframe(pd.DataFrame(st.session_state.rate_history), use_container_width=True, hide_index=True)

elif nav == "Guest reviews":
    st.markdown('<div class="topbar"><h1>Guest Feedback</h1><p>Recent guest reviews gathered across booking and review platforms.</p></div>', unsafe_allow_html=True)
    filter_a, filter_b, filter_c = st.columns(3)
    with filter_a:
        platform_filter = st.multiselect("Platform", sorted(reviews["platform"].dropna().unique()))
    with filter_b:
        sentiment_filter = st.multiselect("Sentiment", sorted(reviews["sentiment"].dropna().unique()))
    with filter_c:
        issues_only = st.checkbox("Only reviews with an issue")
    recent = reviews.copy()
    if platform_filter:
        recent = recent[recent["platform"].isin(platform_filter)]
    if sentiment_filter:
        recent = recent[recent["sentiment"].isin(sentiment_filter)]
    if issues_only:
        recent = recent[recent["issues"].notna() & ~recent["issues"].astype(str).str.strip().str.lower().isin(["", "none", "nan"])]
    recent = recent.sort_values("date", ascending=False).head(50)
    st.markdown(f'<div class="data-hint">Showing {len(recent)} guest reviews. Use the filters to isolate a platform, sentiment or service issue.</div>', unsafe_allow_html=True)
    if recent.empty:
        st.info("No guest reviews match the selected filters.")
    for _, r in recent.iterrows():
        sentiment_color = "green" if r["sentiment"]=="Positive" else "red" if r["sentiment"]=="Negative" else "orange"
        stars = f'{r["rating"]}/5'
        issue_html = ""
        if pd.notna(r["issues"]) and str(r["issues"]).strip().lower() not in ("", "none", "nan"):
            issue_html = f"<div class='review-issue'>Issue noted: {r['issues']}</div>"
        st.markdown(f"""
        <div class="review-card {'positive' if sentiment_color=='green' else 'negative' if sentiment_color=='red' else 'neutral'}">
            <div><div class="review-score">{stars}</div><div class="review-source">{r['platform']}<br>{r['date'].strftime('%d %b %Y')}</div></div>
            <div><div class="review-comment">{r['comment']}</div>{issue_html}</div>
        </div>
        """, unsafe_allow_html=True)
        if pd.notna(r["issues"]) and str(r["issues"]).strip().lower() not in ("", "none", "nan"):
            review_key = str(r.get("review_id", r.name))
            current_action = st.session_state.review_actions.get(review_key, {"status": "Open", "owner": "Unassigned"})
            action_cols = st.columns([1, 1, 1])
            owner = action_cols[0].selectbox("Assign issue", ["Unassigned", "Front desk", "Housekeeping", "Food & beverage", "Management"], index=["Unassigned", "Front desk", "Housekeeping", "Food & beverage", "Management"].index(current_action["owner"]), key=f"owner_{review_key}")
            status = action_cols[1].selectbox("Issue status", ["Open", "In progress", "Resolved"], index=["Open", "In progress", "Resolved"].index(current_action["status"]), key=f"status_{review_key}")
            if action_cols[2].button("Save response", key=f"save_{review_key}", use_container_width=True):
                st.session_state.review_actions[review_key] = {"status": status, "owner": owner, "updated": datetime.now().strftime("%d %b, %H:%M")}
                st.success(f"Guest issue assigned to {owner} and marked {status.lower()}.")

elif nav == "Today’s status":
    st.markdown('<div class="topbar"><h1>Today\'s Hotel Status</h1><p>Latest occupancy, revenue and staffing position.</p></div>', unsafe_allow_html=True)
    
    today = bookings.iloc[-1]
    c1,c2,c3 = st.columns(3)
    c1.markdown(kcard("gold", f"{today['rooms_occupied']}/90","Rooms Occupied",f"{today['occupancy_rate_pct']:.0f}%"), unsafe_allow_html=True)
    c2.markdown(kcard("green", f"P{today['daily_revenue_bwp']:,.0f}","Today's Revenue",""), unsafe_allow_html=True)
    c3.markdown(kcard("blue", f"{today['staff_on_duty']}","Staff on Duty",""), unsafe_allow_html=True)

st.markdown("---")
st.markdown("<div style='text-align:center;color:#5b6a6c;font-size:.7rem'>Savannah Gates · Hospitality Operations · Botswana · 2026</div>", unsafe_allow_html=True)
