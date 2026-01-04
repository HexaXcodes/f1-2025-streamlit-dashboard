"""
Data Processor for F1 2025 Dashboard
Handles all data calculations and standings management
"""

from f1_2025_data import F1Data
import pandas as pd
from collections import defaultdict

class DataProcessor:
    def __init__(self):
        self.f1_data = F1Data()
        self.races = self.f1_data.races
        self.race_results = self.f1_data.race_results
        self.drivers = self.f1_data.drivers
    
    def get_standings(self, race_num):
        """
        Calculate cumulative driver and constructor standings after race_num
        
        Args:
            race_num: Race number (1-24)
        
        Returns:
            Tuple of (driver_standings_dict, constructor_standings_dict)
        """
        driver_points = {driver: 0 for driver in self.drivers}
        constructor_points = defaultdict(int)
        
        # Accumulate points from all races up to race_num
        for i in range(min(race_num, len(self.race_results))):
            race = self.race_results[i]
            for driver, team, points in race['results']:
                if driver in driver_points:
                    driver_points[driver] += points
                constructor_points[team] += points
        
        # Sort and return as ordered dicts
        sorted_drivers = dict(sorted(driver_points.items(), 
                                    key=lambda x: x[1], reverse=True))
        sorted_constructors = dict(sorted(constructor_points.items(), 
                                         key=lambda x: x[1], reverse=True))
        
        return sorted_drivers, sorted_constructors
    
    def get_race_info(self, race_idx):
        """Get information about a specific race"""
        if race_idx < 0 or race_idx >= len(self.races):
            return {'race': 'N/A', 'winner': 'N/A', 'team': 'N/A'}
        
        race = self.races[race_idx]
        race_result = self.race_results[race_idx]
        
        # First finisher is the winner
        winner_name, winner_team, _ = race_result['results'][0]
        
        return {
            'race': race['race'],
            'date': race['date'],
            'winner': winner_name,
            'team': winner_team
        }
    
    def get_progression_data(self, race_num):
        """
        Get point progression data for top drivers and constructors
        for use in trend charts
        """
        driver_progression = defaultdict(list)
        constructor_progression = defaultdict(list)
        
        # Track points after each race
        driver_totals = {driver: 0 for driver in self.drivers}
        constructor_totals = defaultdict(int)
        
        for race_idx in range(min(race_num, len(self.race_results))):
            race = self.race_results[race_idx]
            
            # Accumulate points
            for driver, team, points in race['results']:
                if driver in driver_totals:
                    driver_totals[driver] += points
                constructor_totals[team] += points
            
            # Record progression
            for driver, points in driver_totals.items():
                driver_progression[driver].append(points)
            
            for team, points in constructor_totals.items():
                constructor_progression[team].append(points)
        
        # Convert to dataframes for plotting
        driver_df = pd.DataFrame(driver_progression)
        driver_df['Race'] = range(1, len(driver_df) + 1)
        
        constructor_df = pd.DataFrame(constructor_progression)
        constructor_df['Race'] = range(1, len(constructor_df) + 1)
        
        return {
            'drivers': driver_df,
            'constructors': constructor_df
        }
    
    def get_comparison_data(self, race_num, driver_list):
        """Get comparison data for selected drivers"""
        driver_progression = {driver: [] for driver in driver_list}
        driver_totals = {driver: 0 for driver in driver_list}
        
        for race_idx in range(min(race_num, len(self.race_results))):
            race = self.race_results[race_idx]
            
            for driver, team, points in race['results']:
                if driver in driver_totals:
                    driver_totals[driver] += points
            
            for driver in driver_list:
                driver_progression[driver].append(driver_totals[driver])
        
        df = pd.DataFrame(driver_progression)
        df['Race'] = range(1, len(df) + 1)
        
        return df
    
    def get_driver_stats(self, driver_name, race_num):
        """Get detailed statistics for a specific driver"""
        wins = 0
        podiums = 0
        total_points = 0
        races_participated = 0
        
        for race_idx in range(min(race_num, len(self.race_results))):
            race = self.race_results[race_idx]
            
            for idx, (drv, team, points) in enumerate(race['results']):
                if drv == driver_name:
                    total_points += points
                    races_participated += 1
                    
                    if idx == 0:  # Winner
                        wins += 1
                    if idx < 3:  # Top 3
                        podiums += 1
                    break
        
        return {
            'driver': driver_name,
            'total_points': total_points,
            'wins': wins,
            'podiums': podiums,
            'races_participated': races_participated,
            'avg_points_per_race': total_points / races_participated if races_participated > 0 else 0
        }
    
    def get_constructor_stats(self, team_name, race_num):
        """Get detailed statistics for a specific constructor"""
        total_points = 0
        races_competed = 0
        wins = 0
        
        for race_idx in range(min(race_num, len(self.race_results))):
            race = self.race_results[race_idx]
            team_race_points = 0
            team_finished = False
            
            for idx, (drv, team, points) in enumerate(race['results']):
                if team == team_name:
                    total_points += points
                    team_race_points += points
                    team_finished = True
                    
                    if idx == 0:  # Winner
                        wins += 1
            
            if team_finished:
                races_competed += 1
        
        return {
            'team': team_name,
            'total_points': total_points,
            'wins': wins,
            'races_competed': races_competed,
            'avg_points_per_race': total_points / races_competed if races_competed > 0 else 0
        }
    
    def get_head_to_head(self, driver1, driver2, race_num):
        """Compare two drivers head-to-head"""
        stats1 = self.get_driver_stats(driver1, race_num)
        stats2 = self.get_driver_stats(driver2, race_num)
        
        return {
            'driver1': stats1,
            'driver2': stats2,
            'points_difference': stats1['total_points'] - stats2['total_points'],
            'wins_difference': stats1['wins'] - stats2['wins']
        }