"""
F1 2025 Season Interactive Dashboard
Main Streamlit Application
Author: DVP Lab Student
Created: January 2026
"""

import streamlit as st
import pandas as pd
from data_processor import DataProcessor
from visualizations import DashboardVisualizations
import plotly.graph_objects as go
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="F1 2025 Season Dashboard",
    page_icon="🏁",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
        .metric-card {
            background-color: #f0f2f6;
            padding: 20px;
            border-radius: 10px;
            margin: 10px 0;
        }
        .title-section {
            color: #FF1801;
            font-weight: bold;
        }
        .standings-table {
            background-color: white;
            padding: 15px;
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'data_processor' not in st.session_state:
    st.session_state.data_processor = DataProcessor()
    st.session_state.viz = DashboardVisualizations()

processor = st.session_state.data_processor
viz = st.session_state.viz

# Header
st.markdown("<h1 style='text-align: center; color: #FF1801;'>🏁 FORMULA 1 2025 SEASON DASHBOARD</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666;'>Interactive Championship Standings & Real-Time Analytics</p>", unsafe_allow_html=True)

# Sidebar configuration
with st.sidebar:
    st.markdown("## ⚙️ DASHBOARD CONTROLS")
    
    # Race selector
    race_num = st.slider(
        "Select Race Number",
        min_value=1,
        max_value=24,
        value=24,
        step=1,
        help="Move through the 2025 F1 season race-by-race"
    )
    
    # Toggle for different analysis views
    st.markdown("---")
    view_mode = st.radio(
        "Select View",
        ["📊 Championship Standings", "📈 Trends & Analytics", "🏆 Detailed Comparison"]
    )
    
    st.markdown("---")
    
    # Information panel
    st.markdown("### 📋 Quick Info")
    races_completed = race_num
    races_remaining = 24 - race_num
    st.info(f"**Races Completed**: {races_completed}/24\n\n**Races Remaining**: {races_remaining}")

# Get standings after selected race
driver_standings, constructor_standings = processor.get_standings(race_num)
race_info = processor.get_race_info(race_num - 1)

# Main content area
if view_mode == "📊 Championship Standings":
    # Current race information
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Current Race", f"Race {race_num}/24", f"{race_info['race']}")
    with col2:
        st.metric("Race Winner", race_info['winner'], race_info['team'])
    with col3:
        st.metric("Driver Leader", list(driver_standings.keys())[0], f"{list(driver_standings.values())[0]} pts")
    with col4:
        st.metric("Constructor Leader", list(constructor_standings.keys())[0], f"{list(constructor_standings.values())[0]} pts")
    
    st.markdown("---")
    
    # Driver standings
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🏎️ DRIVER CHAMPIONSHIP STANDINGS")
        
        # Create driver standings dataframe
        driver_df = pd.DataFrame(
            [(i+1, driver, points) for i, (driver, points) in enumerate(driver_standings.items())],
            columns=["Position", "Driver", "Points"]
        )
        
        # Highlight top 3
        def highlight_top3(row):
            if row['Position'] == 1:
                return ['background-color: #FFD700'] * len(row)  # Gold
            elif row['Position'] == 2:
                return ['background-color: #C0C0C0'] * len(row)  # Silver
            elif row['Position'] == 3:
                return ['background-color: #CD7F32'] * len(row)  # Bronze
            else:
                return [''] * len(row)
        
        st.dataframe(
            driver_df.style.apply(highlight_top3, axis=1).set_properties(**{'text-align': 'center'}),
            use_container_width=True,
            hide_index=True
        )
    
    with col2:
        st.subheader("🏭 CONSTRUCTOR CHAMPIONSHIP STANDINGS")
        
        # Create constructor standings dataframe
        constructor_df = pd.DataFrame(
            [(i+1, team, points) for i, (team, points) in enumerate(constructor_standings.items())],
            columns=["Position", "Team", "Points"]
        )
        
        st.dataframe(
            constructor_df.style.apply(highlight_top3, axis=1).set_properties(**{'text-align': 'center'}),
            use_container_width=True,
            hide_index=True
        )
    
    st.markdown("---")
    
    # Points distribution visualization
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Top 10 Drivers - Points Distribution")
        top_10_drivers = dict(list(driver_standings.items())[:10])
        
        fig_drivers = px.bar(
            x=list(top_10_drivers.values()),
            y=list(top_10_drivers.keys()),
            orientation='h',
            labels={'x': 'Points', 'y': 'Driver'},
            color=list(top_10_drivers.values()),
            color_continuous_scale='Reds'
        )
        fig_drivers.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig_drivers, use_container_width=True)
    
    with col2:
        st.subheader("🏭 Constructor Points Distribution")
        
        fig_constructors = px.pie(
            values=list(constructor_standings.values()),
            names=list(constructor_standings.keys()),
            hole=0.3
        )
        fig_constructors.update_layout(height=400)
        st.plotly_chart(fig_constructors, use_container_width=True)

elif view_mode == "📈 Trends & Analytics":
    st.subheader("📈 Championship Points Progression")
    
    # Get point progression data
    progression_data = processor.get_progression_data(race_num)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Top 5 Drivers - Points Trend")
        fig_trend = px.line(
            progression_data['drivers'],
            x='Race',
            y=['Lando Norris', 'Max Verstappen', 'Oscar Piastri', 'George Russell', 'Charles Leclerc'],
            markers=True,
            title="Points Progression Over Season"
        )
        fig_trend.update_layout(height=450, hovermode='x unified')
        st.plotly_chart(fig_trend, use_container_width=True)
    
    with col2:
        st.markdown("#### Top Constructors - Points Trend")
        fig_const_trend = px.line(
            progression_data['constructors'],
            x='Race',
            y=['McLaren', 'Red Bull', 'Mercedes', 'Ferrari'],
            markers=True,
            title="Constructor Points Progression"
        )
        fig_const_trend.update_layout(height=450, hovermode='x unified')
        st.plotly_chart(fig_const_trend, use_container_width=True)
    
    st.markdown("---")
    
    # Analytics metrics
    st.subheader("🎯 Key Statistics")
    
    col1, col2, col3, col4 = st.columns(4)
    
    leader_name = list(driver_standings.keys())[0]
    leader_points = list(driver_standings.values())[0]
    second_name = list(driver_standings.keys())[1]
    second_points = list(driver_standings.values())[1]
    gap = leader_points - second_points
    
    with col1:
        st.metric("Championship Lead", f"{leader_name}", f"+{gap} pts to {second_name}")
    
    with col2:
        st.metric("Average Points/Race", f"{leader_points/race_num:.1f}", f"(Top Driver)")
    
    with col3:
        avg_constructor_leader = list(constructor_standings.values())[0] / race_num
        st.metric("Constructor Avg/Race", f"{avg_constructor_leader:.1f}", f"({list(constructor_standings.keys())[0]})")
    
    with col4:
        st.metric("Total Points Awarded", f"{sum(driver_standings.values())}", f"Across {race_num} races")

else:  # Detailed Comparison
    st.subheader("🏆 Detailed Driver Comparison")
    
    col1, col2 = st.columns(2)
    
    with col1:
        drivers_to_compare = st.multiselect(
            "Select Drivers to Compare",
            list(driver_standings.keys())[:10],
            default=["Lando Norris", "Max Verstappen"]
        )
    
    with col2:
        st.info("💡 Tip: Select 2-5 drivers to compare their performance")
    
    if drivers_to_compare:
        comparison_data = processor.get_comparison_data(race_num, drivers_to_compare)
        
        st.markdown("#### Head-to-Head Comparison")
        fig_comparison = px.line(
            comparison_data,
            x='Race',
            y=drivers_to_compare,
            markers=True,
            title="Driver Performance Comparison"
        )
        fig_comparison.update_layout(height=500, hovermode='x unified')
        st.plotly_chart(fig_comparison, use_container_width=True)
        
        st.markdown("---")
        
        # Comparison statistics table
        st.markdown("#### Comparison Statistics")
        comparison_stats = []
        for driver in drivers_to_compare:
            # Find driver's position
            position = list(driver_standings.keys()).index(driver) + 1 if driver in driver_standings else 99
            points = driver_standings.get(driver, 0)
            avg_per_race = points / race_num
            
            comparison_stats.append({
                'Driver': driver,
                'Position': position,
                'Total Points': points,
                'Avg Points/Race': f"{avg_per_race:.1f}",
                'Points Gap to Leader': points - list(driver_standings.values())[0]
            })
        
        comparison_df = pd.DataFrame(comparison_stats)
        st.dataframe(comparison_df, use_container_width=True, hide_index=True)

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #999; font-size: 12px;'>
    <p>Formula 1 2025 Season Dashboard | DVP Lab Project | Data Source: Official F1 Results</p>
    <p>Last Updated: January 04, 2026</p>
    </div>
""", unsafe_allow_html=True)

# Export functionality
with st.expander("📥 Export Data"):
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Download Driver Standings (CSV)"):
            driver_df = pd.DataFrame(
                [(i+1, driver, points) for i, (driver, points) in enumerate(driver_standings.items())],
                columns=["Position", "Driver", "Points"]
            )
            st.download_button(
                label="Click to download",
                data=driver_df.to_csv(index=False),
                file_name=f"f1_2025_drivers_race_{race_num}.csv",
                mime="text/csv"
            )
    
    with col2:
        if st.button("Download Constructor Standings (CSV)"):
            constructor_df = pd.DataFrame(
                [(i+1, team, points) for i, (team, points) in enumerate(constructor_standings.items())],
                columns=["Position", "Team", "Points"]
            )
            st.download_button(
                label="Click to download",
                data=constructor_df.to_csv(index=False),
                file_name=f"f1_2025_constructors_race_{race_num}.csv",
                mime="text/csv"
            )
st.write("✅ App booted")            