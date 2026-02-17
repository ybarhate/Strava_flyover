import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from engine import get_activity_data

st.set_page_config(page_title="Flyover Pro", layout="wide")
st.title("🚵 Strava Flyover Automation")

# Sidebar for credentials
with st.sidebar:
    st.header("Settings")
    token = st.text_input("Enter Access Token", value="d8a0e9e7389cd0e0d14b5900739e1b158d0578de", type="password")

# Main UI
url_input = st.text_input("Paste Strava Link:", placeholder="https://strava.app.link/...")

if st.button("Build 3D Flyover"):
    try:
        coords, alts = get_activity_data(url_input, token)
        df = pd.DataFrame(coords, columns=['lat', 'lon'])
        df['alt'] = alts
        
        # Build the Cinematic Map
        fig = go.Figure(data=[go.Scatter3d(
            x=df['lon'], y=df['lat'], z=df['alt'],
            mode='lines', line=dict(color='#FC4C02', width=6)
        )])
        
        fig.update_layout(
            template="plotly_dark",
            scene=dict(aspectratio=dict(x=1, y=1, z=0.5)),
            margin=dict(l=0, r=0, b=0, t=0)
        )
        
        st.plotly_chart(fig, use_container_width=True)
        st.success(f"Success! Analyzed {len(coords)} GPS points.")
        
    except Exception as e:
        st.error(f"Error: {e}")