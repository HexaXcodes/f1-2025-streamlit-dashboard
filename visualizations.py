"""
Visualization Module for F1 Dashboard
Contains all plotting and visualization functions
"""


import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

class DashboardVisualizations:
    def __init__(self):
        plt.rcParams['figure.figsize'] = (14, 8)
    
    def plot_driver_standings_bar(self, driver_standings, top_n=10):
        """Create bar chart of top N drivers"""
        fig, ax = plt.subplots(figsize=(12, 6))
        
        top_drivers = dict(list(driver_standings.items())[:top_n])
        drivers = list(top_drivers.keys())
        points = list(top_drivers.values())
        
        colors = ['#FFD700' if i == 0 else '#C0C0C0' if i == 1 else '#CD7F32' if i == 2 else '#FF1801' 
                 for i in range(len(drivers))]
        
        bars = ax.barh(drivers, points, color=colors, edgecolor='black', linewidth=1.5)
        
        # Add value labels
        for bar, point in zip(bars, points):
            ax.text(point + 5, bar.get_y() + bar.get_height()/2, 
                   f'{point}', va='center', fontweight='bold')
        
        ax.set_xlabel('Points', fontsize=12, fontweight='bold')
        ax.set_title('Driver Championship Standings', fontsize=14, fontweight='bold')
        ax.invert_yaxis()
        
        plt.tight_layout()
        return fig
    
    def plot_constructor_standings_pie(self, constructor_standings):
        """Create pie chart of constructor standings"""
        fig, ax = plt.subplots(figsize=(10, 8))
        
        teams = list(constructor_standings.keys())
        points = list(constructor_standings.values())
        
        colors = plt.cm.Set3(np.linspace(0, 1, len(teams)))
        
        wedges, texts, autotexts = ax.pie(points, labels=teams, autopct='%1.1f%%',
                                           colors=colors, startangle=90,
                                           textprops={'fontsize': 10})
        
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
        
        ax.set_title('Constructor Championship Distribution', fontsize=14, fontweight='bold')
        plt.tight_layout()
        return fig
    
    def plot_points_progression(self, progression_data, top_drivers=5):
        """Plot points progression over races"""
        fig, ax = plt.subplots(figsize=(14, 7))
        
        driver_df = progression_data['drivers']
        
        # Get top drivers
        top_cols = [col for col in driver_df.columns if col != 'Race'][:top_drivers]
        
        for driver in top_cols:
            ax.plot(driver_df['Race'], driver_df[driver], marker='o', linewidth=2, label=driver)
        
        ax.set_xlabel('Race Number', fontsize=12, fontweight='bold')
        ax.set_ylabel('Cumulative Points', fontsize=12, fontweight='bold')
        ax.set_title('Championship Points Progression - Top Drivers', fontsize=14, fontweight='bold')
        ax.legend(loc='upper left', fontsize=10)
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        return fig
    
    def plot_race_by_race_points(self, race_results, race_idx):
        """Plot points distribution for a specific race"""
        if race_idx >= len(race_results):
            return None
        
        race = race_results[race_idx]
        drivers = [result[0] for result in race['results']]
        points = [result[2] for result in race['results']]
        
        fig, ax = plt.subplots(figsize=(12, 6))
        
        colors_palette = ['#FFD700', '#C0C0C0', '#CD7F32'] + ['#FF1801'] * (len(drivers) - 3)
        
        bars = ax.bar(range(len(drivers)), points, color=colors_palette[:len(drivers)], 
                     edgecolor='black', linewidth=1.5)
        
        # Add value labels
        for bar, point in zip(bars, points):
            ax.text(bar.get_x() + bar.get_width()/2, point + 0.5,
                   f'{int(point)}', ha='center', va='bottom', fontweight='bold')
        
        ax.set_xticks(range(len(drivers)))
        ax.set_xticklabels(drivers, rotation=45, ha='right')
        ax.set_ylabel('Points', fontsize=12, fontweight='bold')
        ax.set_title(f'Race {race_idx + 1}: Points Distribution', fontsize=14, fontweight='bold')
        ax.set_ylim(0, max(points) + 5)
        
        plt.tight_layout()
        return fig
    
    def plot_head_to_head(self, comparison_data):
        """Plot head-to-head driver comparison"""
        fig, ax = plt.subplots(figsize=(12, 6))
        
        drivers = comparison_data.columns[:-1]  # Exclude 'Race' column
        races = comparison_data['Race'].values
        
        for driver in drivers:
            ax.plot(comparison_data['Race'], comparison_data[driver], 
                   marker='o', linewidth=2.5, label=driver, markersize=6)
        
        ax.set_xlabel('Race Number', fontsize=12, fontweight='bold')
        ax.set_ylabel('Cumulative Points', fontsize=12, fontweight='bold')
        ax.set_title('Head-to-Head Driver Comparison', fontsize=14, fontweight='bold')
        ax.legend(fontsize=11)
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        return fig
    
    @staticmethod
    def create_summary_stats_table(driver_standings, constructor_standings):
        """Create summary statistics table"""
        summary = {
            'Championship Leader': list(driver_standings.keys())[0],
            'Leader Points': list(driver_standings.values())[0],
            'Constructor Leader': list(constructor_standings.keys())[0],
            'Constructor Points': list(constructor_standings.values())[0],
            'Total Drivers': len(driver_standings),
            'Total Constructors': len(constructor_standings)
        }
        return summary