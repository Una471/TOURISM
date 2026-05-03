"""
Savannah Gates Hotel GABORONE — REVENUE & GUEST SATISFACTION DASHBOARD
Management dashboard with CLEAR TEXT COLORS.
Run: streamlit run 03_dashboard.py --server.port 8501
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Savannah Gates Hotel | Dashboard", page_icon="🏨", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
html,body,[class*="css"]{font-family:'Inter',sans-serif;background:#f8f9fa;color:#212529;}
.topbar{background:linear-gradient(135deg,#d4af37,#c5a028);color:white;padding:1.4rem 2rem;border-radius:12px;margin-bottom:1.5rem;}
.topbar h1{margin:0;font-size:1.5rem;font-weight:700;color:white;}
.topbar p{margin:.3rem 0 0;color:#fff;opacity:.9;font-size:.85rem;}
.kcard{background:white;border-radius:12px;padding:1.2rem 1.4rem;box-shadow:0 2px 10px rgba(0,0,0,.08);border-left:5px solid #dee2e6;margin-bottom:.4rem;}
.kcard.red{border-left-color:#d32f2f;} .kcard.orange{border-left-color:#f57c00;}
.kcard.green{border-left-color:#388e3c;} .kcard.blue{border-left-color:#1976d2;}
.kcard.gold{border-left-color:#d4af37;}
.kval{font-size:1.9rem;font-weight:700;line-height:1.1;color:#212529;}
.klbl{font-size:.72rem;text-transform:uppercase;letter-spacing:1.5px;color:#6c757d;margin-top:.3rem;}
.ksub{font-size:.78rem;color:#495057;margin-top:.3rem;}
.ccard{background:white;border-radius:12px;padding:1.2rem 1.4rem;box-shadow:0 2px 10px rgba(0,0,0,.08);margin-bottom:1rem;}
.ctitle{font-size:.95rem;font-weight:600;color:#212529;margin-bottom:.2rem;}
.csub{font-size:.78rem;color:#6c757d;margin-bottom:.7rem;}
section[data-testid="stSidebar"]{background:#c5a028!important;}
section[data-testid="stSidebar"] *{color:#fff!important;}
#MainMenu,footer,header{visibility:hidden;}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load():
    bookings = pd.read_csv("daily_bookings_analyzed.csv", parse_dates=["date"])
    reviews  = pd.read_csv("guest_reviews_analyzed.csv", parse_dates=["date"])
    staffing = pd.read_csv("staffing_data_analyzed.csv", parse_dates=["date"])
    return bookings, reviews, staffing

bookings, reviews, staffing = load()

with st.sidebar:
    st.markdown("### 🏨 Savannah Gates Hotel")
    st.markdown("Management Dashboard")
    st.markdown("---")
    page = st.radio("Go to", [
        "📊  Revenue Overview",
        "⭐  Guest Satisfaction",
        "👥  Staffing Optimization",
        "📈  Pricing Strategy",
    ])
    st.markdown("---")
    st.caption("Data: Full Year 2025")

def kcard(color, val, lbl, sub=""):
    return f'<div class="kcard {color}"><div class="kval">{val}</div><div class="klbl">{lbl}</div>{"<div class=ksub>"+sub+"</div>" if sub else ""}</div>'

def wchart(fig, h=340):
    fig.update_layout(plot_bgcolor="white",paper_bgcolor="white",font_color="#212529",height=h,margin=dict(t=15,b=20,l=10,r=10))
    return fig

if page == "📊  Revenue Overview":
    st.markdown('<div class="topbar"><h1>🏨 Revenue Overview</h1><p>Savannah Gates Hotel Gaborone · Annual Performance 2025</p></div>', unsafe_allow_html=True)
    
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
        st.markdown('<div class="ccard"><div class="ctitle">📊 Monthly Revenue Trend</div><div class="csub">Shows seasonal patterns and peak periods</div>', unsafe_allow_html=True)
        monthly = bookings.groupby(bookings["date"].dt.to_period("M"))["daily_revenue_bwp"].sum().reset_index()
        monthly["Month"] = monthly["date"].astype(str)
        monthly["label"] = monthly["daily_revenue_bwp"].apply(lambda x: f"P{x/1e3:.0f}K")
        fig = px.bar(monthly, x="Month", y="daily_revenue_bwp", color="daily_revenue_bwp",
                     color_continuous_scale=["#ffd700","#d4af37"], text="label",
                     labels={"daily_revenue_bwp":"Revenue (BWP)"})
        fig.update_traces(textposition="outside")
        fig.update_layout(showlegend=False)
        st.plotly_chart(wchart(fig), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="ccard"><div class="ctitle">📊 Occupancy Rate by Day of Week</div><div class="csub">Weekends consistently higher than weekdays</div>', unsafe_allow_html=True)
        dow = bookings.groupby("day_of_week")["occupancy_rate_pct"].mean().reindex(
            ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]).reset_index()
        dow["label"] = dow["occupancy_rate_pct"].apply(lambda x: f"{x:.0f}%")
        fig2 = px.bar(dow, x="day_of_week", y="occupancy_rate_pct", color="occupancy_rate_pct",
                      color_continuous_scale=["#ffebcd","#d4af37"], text="label",
                      labels={"occupancy_rate_pct":"Occupancy %","day_of_week":""})
        fig2.update_traces(textposition="outside")
        fig2.update_layout(showlegend=False)
        st.plotly_chart(wchart(fig2), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

elif page == "⭐  Guest Satisfaction":
    st.markdown('<div class="topbar"><h1>⭐ Guest Satisfaction Report</h1><p>Reviews from all platforms in one view</p></div>', unsafe_allow_html=True)
    
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
        st.markdown('<div class="ccard"><div class="ctitle">📊 Rating Distribution</div>', unsafe_allow_html=True)
        rating_dist = reviews["rating"].value_counts().sort_index(ascending=False).reset_index()
        rating_dist.columns = ["Rating","Count"]
        rating_dist["Stars"] = rating_dist["Rating"].apply(lambda x: "⭐"*x)
        fig = px.bar(rating_dist, x="Stars", y="Count", color="Rating",
                     color_continuous_scale=["#e74c3c","#ffd700"], text="Count")
        fig.update_traces(textposition="outside")
        fig.update_layout(showlegend=False)
        st.plotly_chart(wchart(fig), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="ccard"><div class="ctitle">📊 Reviews by Platform</div>', unsafe_allow_html=True)
        platform = reviews.groupby("platform").agg(
            count=("review_id","count"), avg_rating=("rating","mean")).sort_values("count",ascending=False).reset_index()
        fig2 = px.bar(platform, x="platform", y="count", color="avg_rating",
                      color_continuous_scale=["#e74c3c","#ffd700"], text="count",
                      labels={"count":"Number of Reviews","platform":"","avg_rating":"Avg Rating"})
        fig2.update_traces(textposition="outside")
        st.plotly_chart(wchart(fig2), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

elif page == "👥  Staffing Optimization":
    st.markdown('<div class="topbar"><h1>👥 Staffing & Labor Cost</h1><p>Optimizing staff schedules based on occupancy</p></div>', unsafe_allow_html=True)
    
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
        st.markdown('<div class="ccard"><div class="ctitle">📊 Labor Cost by Role</div>', unsafe_allow_html=True)
        role_cost = staffing.groupby("role")["daily_cost_bwp"].sum().sort_values(ascending=False).reset_index()
        role_cost["label"] = role_cost["daily_cost_bwp"].apply(lambda x: f"P{x/1e3:.0f}K")
        fig = px.bar(role_cost, x="role", y="daily_cost_bwp", color="daily_cost_bwp",
                     color_continuous_scale=["#c6f6d5","#d4af37"], text="label",
                     labels={"daily_cost_bwp":"Annual Cost","role":""})
        fig.update_traces(textposition="outside")
        fig.update_layout(showlegend=False)
        st.plotly_chart(wchart(fig), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="ccard"><div class="ctitle">📊 Occupancy vs Staff Levels</div>', unsafe_allow_html=True)
        daily_staff = staffing.groupby("date").agg(
            rooms=("rooms_occupied","first"), total_staff=("actual_staff","sum")).reset_index()
        fig2 = px.scatter(daily_staff, x="rooms", y="total_staff", trendline="ols",
                          labels={"rooms":"Rooms Occupied","total_staff":"Total Staff on Duty"})
        st.plotly_chart(wchart(fig2), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

elif page == "📈  Pricing Strategy":
    st.markdown('<div class="topbar"><h1>📈 Dynamic Pricing Strategy</h1><p>Optimizing rates based on demand and events</p></div>', unsafe_allow_html=True)
    
    col1,col2 = st.columns(2)
    with col1:
        st.markdown('<div class="ccard"><div class="ctitle">📊 Price vs Occupancy</div>', unsafe_allow_html=True)
        fig = px.scatter(bookings, x="occupancy_rate_pct", y="avg_room_rate_bwp",
                         color="event_boost", color_continuous_scale=["#c6f6d5","#d4af37"],
                         labels={"occupancy_rate_pct":"Occupancy %","avg_room_rate_bwp":"Avg Rate","event_boost":"Event Boost"})
        st.plotly_chart(wchart(fig), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="ccard"><div class="ctitle">📊 Event Impact on Revenue</div>', unsafe_allow_html=True)
        bookings["Has Event"] = bookings["event_boost"].apply(lambda x: "Event Days" if x > 1.0 else "Normal Days")
        event_comp = bookings.groupby("Has Event")["daily_revenue_bwp"].mean().reset_index()
        fig2 = px.bar(event_comp, x="Has Event", y="daily_revenue_bwp", color="Has Event",
                      color_discrete_map={"Event Days":"#d4af37","Normal Days":"#6c757d"},
                      labels={"daily_revenue_bwp":"Avg Daily Revenue"})
        st.plotly_chart(wchart(fig2), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.markdown("<div style='text-align:center;color:#6c757d;font-size:.78rem'>Cresta Lodge Gaborone · Management Dashboard · Unaswi Leonard · 2026</div>", unsafe_allow_html=True)
