import streamlit as st
import pickle
import pandas as pd
import plotly.graph_objects as go

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="IPL Match Center",
    page_icon="🏏",
    layout="wide"
)

# --- CUSTOM CSS FOR CLEAN, HUMAN UI ---
st.markdown("""
    <style>
    /* Clean Dark Theme */
    .stApp {
        background-color: #0E1117;
        color: #FAFAFA;
    }
    
    /* Clean up default streamlit UI */
    #MainMenu, footer, header {visibility: hidden; display: none !important;}
    
    /* Sleek Cards */
    div[data-testid="stContainer"] {
        background-color: #161B22;
        border-radius: 10px;
        border: 1px solid #30363D;
        padding: 15px;
    }
    
    /* Button Styling */
    div.stButton > button:first-child {
        background-color: #238636;
        color: white;
        font-weight: 600;
        border-radius: 6px;
        border: none;
        padding: 10px 20px;
        width: 100%;
        transition: 0.2s;
    }
    div.stButton > button:first-child:hover {
        background-color: #2EA043;
    }
    
    /* Metric styling */
    div[data-testid="stMetricValue"] {
        font-size: 2rem;
        font-weight: 700;
    }
    
    /* Custom Box for What-If Scenarios */
    .sim-box {
        background-color: #0D1117;
        border: 1px solid #30363D;
        border-radius: 8px;
        padding: 15px;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# --- LOAD MODEL ---
@st.cache_resource
def load_model():
    return pickle.load(open('pipe.pkl', 'rb'))

pipe = load_model()

# --- TEAM DATA & DYNAMIC COLORS ---
teams = [
    'Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore', 
    'Kolkata Knight Riders', 'Kings XI Punjab', 'Chennai Super Kings', 
    'Rajasthan Royals', 'Delhi Capitals'
]

cities = [
    'Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi', 
    'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth', 
    'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley', 
    'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala', 
    'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi', 'Sharjah', 
    'Mohali', 'Bengaluru'
]

team_colors = {
    'Chennai Super Kings': '#FACC15', # Yellow
    'Mumbai Indians': '#0284C7',      # Blue
    'Royal Challengers Bangalore': '#EF4444', # Red
    'Kolkata Knight Riders': '#7C3AED', # Purple
    'Kings XI Punjab': '#E11D48',     # Red/Pink
    'Sunrisers Hyderabad': '#F97316', # Orange
    'Rajasthan Royals': '#DB2777',    # Pink
    'Delhi Capitals': '#2563EB'       # Blue
}

# --- HEADER ---
st.title("🏏 IPL Match Center & Predictions")
st.markdown("Live win probability, tactical analysis, and momentum simulations.")

# --- MAIN SCREEN MATCH CONTROLS ---
with st.container(border=True):
    st.subheader("Match Setup")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        batting_team = st.selectbox('Chasing Team (Batting)', sorted(teams), index=teams.index('Chennai Super Kings') if 'Chennai Super Kings' in teams else 0)
    with col2:
        bowling_team = st.selectbox('Defending Team (Bowling)', sorted(teams), index=teams.index('Royal Challengers Bangalore') if 'Royal Challengers Bangalore' in teams else 1)
    with col3:
        selected_city = st.selectbox('Venue', sorted(cities))
        
    st.markdown("<hr style='border-color: #30363D; margin: 10px 0;'>", unsafe_allow_html=True)
    
    col4, col5, col6, col7 = st.columns(4)
    with col4:
        target = st.number_input('Target Score', min_value=1, value=185)
    with col5:
        score = st.number_input('Current Score', min_value=0, value=95)
    with col6:
        overs = st.number_input('Overs Bowled', min_value=0.1, max_value=19.5, value=11.2, step=0.1)
    with col7:
        wickets = st.number_input('Wickets Lost', min_value=0, max_value=9, value=3, step=1)
        
    predict_clicked = st.button("Analyze Match")

# --- MATCH ANALYSIS SECTION ---
if predict_clicked:
    # Calculations
    runs_left = max(0, target - score)
    balls_left = max(1, 120 - int(overs * 6))
    wickets_left = max(0, 10 - wickets)
    crr = score / overs if overs > 0 else 0
    rrr = (runs_left * 6) / balls_left if balls_left > 0 else 0
    
    input_df = pd.DataFrame({
        'batting_team': [batting_team], 'bowling_team': [bowling_team], 'city': [selected_city], 
        'runs_left': [runs_left], 'balls_left': [balls_left], 'wickets_left': [wickets_left], 
        'total_runs_x': [target], 'crr': [crr], 'rrr': [rrr]
    })
    
    # Model Prediction
    result = pipe.predict_proba(input_df)
    loss_prob = round(result[0][0] * 100)
    win_prob = round(result[0][1] * 100)
    
    st.markdown("### Match Overview")
    
    # 1. KPIs
    k_col1, k_col2, k_col3, k_col4 = st.columns(4)
    k_col1.metric("Runs Needed", f"{runs_left}", f"from {balls_left} balls", delta_color="off")
    k_col2.metric("Wickets in Hand", f"{wickets_left}", f"{wickets} down", delta_color="off")
    k_col3.metric("Current Run Rate", f"{crr:.2f}")
    k_col4.metric("Required Run Rate", f"{rrr:.2f}", f"{rrr-crr:.2f} difference", delta_color="inverse")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 2. Visualizations
    v_col1, v_col2 = st.columns([1, 1])
    
    with v_col1:
        with st.container(border=True):
            st.markdown(f"**Win Probability**")
            # Dynamic team colors based on selection
            bat_color = team_colors.get(batting_team, '#1f77b4')
            bowl_color = team_colors.get(bowling_team, '#ff7f0e')
            
            fig_donut = go.Figure(data=[go.Pie(
                labels=[batting_team, bowling_team],
                values=[win_prob, loss_prob],
                hole=0.6,
                marker=dict(colors=[bat_color, bowl_color], line=dict(color='#0E1117', width=2)),
                textinfo='label+percent',
                hoverinfo='label+percent'
            )])
            fig_donut.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                showlegend=False,
                margin=dict(t=20, b=20, l=20, r=20),
                height=280
            )
            st.plotly_chart(fig_donut, use_container_width=True)
        
    with v_col2:
        with st.container(border=True):
            st.markdown("**Tactical Pressure Index**")
            
            # Explainable AI Metrics for Radar
            radar_rrr = min(rrr / 15, 1) * 100
            radar_wickets = (wickets / 10) * 100
            radar_runs = (runs_left / target) * 100
            
            fig_radar = go.Figure(data=go.Scatterpolar(
                r=[radar_rrr, radar_wickets, radar_runs, radar_rrr],
                theta=['Run Rate Pressure', 'Wicket Strain', 'Target Load', 'Run Rate Pressure'],
                fill='toself',
                fillcolor='rgba(46, 160, 67, 0.2)',
                line=dict(color='#2EA043', width=2)
            ))
            fig_radar.update_layout(
                polar=dict(
                    bgcolor='rgba(0,0,0,0)',
                    radialaxis=dict(visible=False, range=[0, 100]),
                    angularaxis=dict(tickfont=dict(size=11, color='#FAFAFA'), linecolor='#30363D', gridcolor='#30363D')
                ),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                showlegend=False,
                margin=dict(t=30, b=20, l=30, r=30),
                height=280
            )
            st.plotly_chart(fig_radar, use_container_width=True)

    # 3. Text Analysis (Restored Analyst Note)
    st.markdown("### Match Analyst Note")
    if win_prob > 60:
        st.success(f"{batting_team} is in a commanding position. The required run rate is manageable ({rrr:.2f}), and with {wickets_left} wickets in hand, they should prioritize strike rotation over high-risk boundaries.")
    elif win_prob < 40:
        st.error(f"{batting_team} is falling behind. The pressure of the {rrr:.2f} required run rate means batters need to target boundaries immediately. Losing {wickets} wickets has put {bowling_team} in control.")
    else:
        st.info(f"The match is perfectly poised. The current run rate ({crr:.2f}) and required run rate ({rrr:.2f}) are highly competitive. The next two overs will dictate the momentum.")

    # 4. What-If Simulator (Restored)
    st.markdown("### Next-Ball Momentum Simulator")
    
    sim_col1, sim_col2 = st.columns(2)
    
    # Calculate Six Scenario
    b_left_6 = max(1, balls_left - 1)
    r_left_6 = max(0, runs_left - 6)
    input_df_6 = input_df.copy()
    input_df_6['runs_left'] = r_left_6
    input_df_6['balls_left'] = b_left_6
    input_df_6['rrr'] = (r_left_6 * 6) / b_left_6
    win_if_six = round(pipe.predict_proba(input_df_6)[0][1] * 100)
    
    # Calculate Wicket Scenario
    b_left_w = max(1, balls_left - 1)
    w_left_w = max(0, wickets_left - 1)
    input_df_w = input_df.copy()
    input_df_w['wickets_left'] = w_left_w
    input_df_w['balls_left'] = b_left_w
    input_df_w['rrr'] = (runs_left * 6) / b_left_w
    win_if_wicket = round(pipe.predict_proba(input_df_w)[0][1] * 100)
    
    with sim_col1:
        st.markdown(f"""
        <div class="sim-box">
            <h4 style="margin-top: 0; color: #2EA043;">Scenario: Six Hit (+6 Runs)</h4>
            <h1 style="margin: 0;">{win_if_six}% Win Probability</h1>
            <p style="color: #8B949E; margin-bottom: 0;">Momentum swing: <strong>+{win_if_six - win_prob}%</strong> to {batting_team}</p>
        </div>
        """, unsafe_allow_html=True)
        
    with sim_col2:
        st.markdown(f"""
        <div class="sim-box">
            <h4 style="margin-top: 0; color: #F85149;">Scenario: Wicket Falls</h4>
            <h1 style="margin: 0;">{win_if_wicket}% Win Probability</h1>
            <p style="color: #8B949E; margin-bottom: 0;">Momentum swing: <strong>{win_if_wicket - win_prob}%</strong> to {batting_team}</p>
        </div>
        """, unsafe_allow_html=True)