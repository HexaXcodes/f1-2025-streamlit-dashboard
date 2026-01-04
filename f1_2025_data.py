"""
F1 2025 Season Complete Data
All 24 races, drivers, and race results
"""

class F1Data:
    def __init__(self):
        # All 24 races in 2025 season
        self.races = [
            {"race": "Australian Grand Prix", "date": "16 Mar", "location": "Melbourne"},
            {"race": "Chinese Grand Prix", "date": "23 Mar", "location": "Shanghai"},
            {"race": "Japanese Grand Prix", "date": "06 Apr", "location": "Suzuka"},
            {"race": "Bahrain Grand Prix", "date": "13 Apr", "location": "Manama"},
            {"race": "Saudi Arabian Grand Prix", "date": "20 Apr", "location": "Jeddah"},
            {"race": "Miami Grand Prix", "date": "04 May", "location": "Miami"},
            {"race": "Emilia Romagna Grand Prix", "date": "18 May", "location": "Imola"},
            {"race": "Monaco Grand Prix", "date": "25 May", "location": "Monte Carlo"},
            {"race": "Spanish Grand Prix", "date": "01 Jun", "location": "Barcelona"},
            {"race": "Canadian Grand Prix", "date": "15 Jun", "location": "Montreal"},
            {"race": "Austrian Grand Prix", "date": "29 Jun", "location": "Spielberg"},
            {"race": "British Grand Prix", "date": "06 Jul", "location": "Silverstone"},
            {"race": "Belgian Grand Prix", "date": "27 Jul", "location": "Spa"},
            {"race": "Hungarian Grand Prix", "date": "03 Aug", "location": "Budapest"},
            {"race": "Dutch Grand Prix", "date": "31 Aug", "location": "Zandvoort"},
            {"race": "Italian Grand Prix", "date": "07 Sep", "location": "Monza"},
            {"race": "Azerbaijan Grand Prix", "date": "21 Sep", "location": "Baku"},
            {"race": "Singapore Grand Prix", "date": "05 Oct", "location": "Marina Bay"},
            {"race": "United States Grand Prix", "date": "19 Oct", "location": "Austin"},
            {"race": "Mexico City Grand Prix", "date": "26 Oct", "location": "Mexico City"},
            {"race": "São Paulo Grand Prix", "date": "09 Nov", "location": "São Paulo"},
            {"race": "Las Vegas Grand Prix", "date": "22 Nov", "location": "Las Vegas"},
            {"race": "Qatar Grand Prix", "date": "30 Nov", "location": "Lusail"},
            {"race": "Abu Dhabi Grand Prix", "date": "07 Dec", "location": "Abu Dhabi"},
        ]
        
        # All 21 drivers in 2025 season
        self.drivers = [
            "Lando Norris", "Max Verstappen", "Oscar Piastri", "George Russell", 
            "Charles Leclerc", "Lewis Hamilton", "Kimi Antonelli", "Alex Albon", 
            "Carlos Sainz", "Fernando Alonso", "Nico Hulkenberg", "Isack Hadjar", 
            "Oliver Bearman", "Liam Lawson", "Esteban Ocon", "Lance Stroll", 
            "Yuki Tsunoda", "Pierre Gasly", "Gabriel Bortoleto", "Franco Colapinto", 
            "Jack Doohan"
        ]
        
        # Complete race results (top 10 finishers only, as only they score points)
        # Format: (driver, team, points) ordered by position
        self.race_results = [
            # Race 1: Australia
            {"race": 0, "results": [
                ("Lando Norris", "McLaren", 25), ("Max Verstappen", "Red Bull", 18), 
                ("Oscar Piastri", "McLaren", 15), ("George Russell", "Mercedes", 12), 
                ("Charles Leclerc", "Ferrari", 10), ("Lewis Hamilton", "Ferrari", 8),
                ("Nico Hulkenberg", "Sauber", 6), ("Alex Albon", "Williams", 4), 
                ("Fernando Alonso", "Aston Martin", 2), ("Lance Stroll", "Aston Martin", 1)
            ]},
            # Race 2: China
            {"race": 1, "results": [
                ("Oscar Piastri", "McLaren", 25), ("Lando Norris", "McLaren", 18), 
                ("Charles Leclerc", "Ferrari", 15), ("Lewis Hamilton", "Ferrari", 12), 
                ("Kimi Antonelli", "Mercedes", 10), ("Alex Albon", "Williams", 8),
                ("Carlos Sainz", "Williams", 6), ("Oliver Bearman", "Haas", 4), 
                ("Esteban Ocon", "Haas", 2), ("Lance Stroll", "Aston Martin", 1)
            ]},
            # Race 3: Japan
            {"race": 2, "results": [
                ("Max Verstappen", "Red Bull", 25), ("Oscar Piastri", "McLaren", 18), 
                ("Kimi Antonelli", "Mercedes", 15), ("Charles Leclerc", "Ferrari", 12), 
                ("Lewis Hamilton", "Ferrari", 10), ("Lando Norris", "McLaren", 8),
                ("Oliver Bearman", "Haas", 6), ("Fernando Alonso", "Aston Martin", 4), 
                ("Carlos Sainz", "Williams", 2), ("Lance Stroll", "Aston Martin", 1)
            ]},
            # Race 4: Bahrain
            {"race": 3, "results": [
                ("Oscar Piastri", "McLaren", 25), ("Max Verstappen", "Red Bull", 18), 
                ("Lando Norris", "McLaren", 15), ("Lewis Hamilton", "Ferrari", 12), 
                ("Charles Leclerc", "Ferrari", 10), ("Kimi Antonelli", "Mercedes", 8),
                ("George Russell", "Mercedes", 6), ("Oliver Bearman", "Haas", 4), 
                ("Esteban Ocon", "Haas", 2), ("Carlos Sainz", "Williams", 1)
            ]},
            # Race 5: Saudi Arabia
            {"race": 4, "results": [
                ("Oscar Piastri", "McLaren", 25), ("Lando Norris", "McLaren", 18), 
                ("Max Verstappen", "Red Bull", 15), ("Charles Leclerc", "Ferrari", 12), 
                ("George Russell", "Mercedes", 10), ("Lewis Hamilton", "Ferrari", 8),
                ("Kimi Antonelli", "Mercedes", 6), ("Nico Hulkenberg", "Sauber", 4), 
                ("Carlos Sainz", "Williams", 2), ("Lance Stroll", "Aston Martin", 1)
            ]},
            # Race 6: Miami
            {"race": 5, "results": [
                ("Oscar Piastri", "McLaren", 25), ("Lando Norris", "McLaren", 18), 
                ("Max Verstappen", "Red Bull", 15), ("Lewis Hamilton", "Ferrari", 12), 
                ("Charles Leclerc", "Ferrari", 10), ("George Russell", "Mercedes", 8),
                ("Kimi Antonelli", "Mercedes", 6), ("Carlos Sainz", "Williams", 4), 
                ("Alex Albon", "Williams", 2), ("Nico Hulkenberg", "Sauber", 1)
            ]},
            # Race 7: Emilia Romagna
            {"race": 6, "results": [
                ("Max Verstappen", "Red Bull", 25), ("Lando Norris", "McLaren", 18), 
                ("Charles Leclerc", "Ferrari", 15), ("Oscar Piastri", "McLaren", 12), 
                ("George Russell", "Mercedes", 10), ("Lewis Hamilton", "Ferrari", 8),
                ("Nico Hulkenberg", "Sauber", 6), ("Kimi Antonelli", "Mercedes", 4), 
                ("Carlos Sainz", "Williams", 2), ("Lance Stroll", "Aston Martin", 1)
            ]},
            # Race 8: Monaco
            {"race": 7, "results": [
                ("Lando Norris", "McLaren", 25), ("Oscar Piastri", "McLaren", 18), 
                ("Max Verstappen", "Red Bull", 15), ("George Russell", "Mercedes", 12), 
                ("Lewis Hamilton", "Ferrari", 10), ("Charles Leclerc", "Ferrari", 8),
                ("Carlos Sainz", "Williams", 6), ("Isack Hadjar", "Racing Bulls", 4), 
                ("Liam Lawson", "Racing Bulls", 2), ("Kimi Antonelli", "Mercedes", 1)
            ]},
            # Race 9: Spain
            {"race": 8, "results": [
                ("Oscar Piastri", "McLaren", 25), ("Lando Norris", "McLaren", 18), 
                ("Charles Leclerc", "Ferrari", 15), ("George Russell", "Mercedes", 12), 
                ("Lewis Hamilton", "Ferrari", 10), ("Max Verstappen", "Red Bull", 8),
                ("Kimi Antonelli", "Mercedes", 6), ("Fernando Alonso", "Aston Martin", 4), 
                ("Carlos Sainz", "Williams", 2), ("Nico Hulkenberg", "Sauber", 1)
            ]},
            # Race 10: Canada
            {"race": 9, "results": [
                ("George Russell", "Mercedes", 25), ("Carlos Sainz", "Williams", 18), 
                ("Lando Norris", "McLaren", 15), ("Lewis Hamilton", "Ferrari", 12), 
                ("Kimi Antonelli", "Mercedes", 10), ("Fernando Alonso", "Aston Martin", 8),
                ("Max Verstappen", "Red Bull", 6), ("Charles Leclerc", "Ferrari", 4), 
                ("Oscar Piastri", "McLaren", 2), ("Esteban Ocon", "Haas", 1)
            ]},
            # Race 11: Austria
            {"race": 10, "results": [
                ("Lando Norris", "McLaren", 25), ("Oscar Piastri", "McLaren", 18), 
                ("Max Verstappen", "Red Bull", 15), ("George Russell", "Mercedes", 12), 
                ("Lewis Hamilton", "Ferrari", 10), ("Charles Leclerc", "Ferrari", 8),
                ("Fernando Alonso", "Aston Martin", 6), ("Nico Hulkenberg", "Sauber", 4), 
                ("Kimi Antonelli", "Mercedes", 2), ("Lance Stroll", "Aston Martin", 1)
            ]},
            # Race 12: Great Britain
            {"race": 11, "results": [
                ("Lando Norris", "McLaren", 25), ("Oscar Piastri", "McLaren", 18), 
                ("Max Verstappen", "Red Bull", 15), ("Kimi Antonelli", "Mercedes", 12), 
                ("George Russell", "Mercedes", 10), ("Fernando Alonso", "Aston Martin", 8),
                ("Charles Leclerc", "Ferrari", 6), ("Lewis Hamilton", "Ferrari", 4), 
                ("Carlos Sainz", "Williams", 2), ("Nico Hulkenberg", "Sauber", 1)
            ]},
            # Race 13: Belgium
            {"race": 12, "results": [
                ("Oscar Piastri", "McLaren", 25), ("Lando Norris", "McLaren", 18), 
                ("Kimi Antonelli", "Mercedes", 15), ("George Russell", "Mercedes", 12), 
                ("Max Verstappen", "Red Bull", 10), ("Charles Leclerc", "Ferrari", 8),
                ("Lewis Hamilton", "Ferrari", 6), ("Oliver Bearman", "Haas", 4), 
                ("Carlos Sainz", "Williams", 2), ("Esteban Ocon", "Haas", 1)
            ]},
            # Race 14: Hungary
            {"race": 13, "results": [
                ("Lando Norris", "McLaren", 25), ("Oscar Piastri", "McLaren", 18), 
                ("George Russell", "Mercedes", 15), ("Charles Leclerc", "Ferrari", 12), 
                ("Lewis Hamilton", "Ferrari", 10), ("Kimi Antonelli", "Mercedes", 8),
                ("Fernando Alonso", "Aston Martin", 6), ("Alex Albon", "Williams", 4), 
                ("Liam Lawson", "Racing Bulls", 2), ("Gabriel Bortoleto", "Sauber", 1)
            ]},
            # Race 15: Netherlands
            {"race": 14, "results": [
                ("Oscar Piastri", "McLaren", 25), ("Lando Norris", "McLaren", 18), 
                ("Max Verstappen", "Red Bull", 15), ("Lewis Hamilton", "Ferrari", 12), 
                ("Charles Leclerc", "Ferrari", 10), ("George Russell", "Mercedes", 8),
                ("Nico Hulkenberg", "Sauber", 6), ("Carlos Sainz", "Williams", 4), 
                ("Fernando Alonso", "Aston Martin", 2), ("Isack Hadjar", "Racing Bulls", 1)
            ]},
            # Race 16: Italy
            {"race": 15, "results": [
                ("Max Verstappen", "Red Bull", 25), ("Lando Norris", "McLaren", 18), 
                ("Oscar Piastri", "McLaren", 15), ("Charles Leclerc", "Ferrari", 12), 
                ("Lewis Hamilton", "Ferrari", 10), ("George Russell", "Mercedes", 8),
                ("Carlos Sainz", "Williams", 6), ("Isack Hadjar", "Racing Bulls", 4), 
                ("Kimi Antonelli", "Mercedes", 2), ("Fernando Alonso", "Aston Martin", 1)
            ]},
            # Race 17: Azerbaijan
            {"race": 16, "results": [
                ("Max Verstappen", "Red Bull", 25), ("Oscar Piastri", "McLaren", 18), 
                ("George Russell", "Mercedes", 15), ("Lando Norris", "McLaren", 12), 
                ("Charles Leclerc", "Ferrari", 10), ("Lewis Hamilton", "Ferrari", 8),
                ("Isack Hadjar", "Racing Bulls", 6), ("Oliver Bearman", "Haas", 4), 
                ("Nico Hulkenberg", "Sauber", 2), ("Carlos Sainz", "Williams", 1)
            ]},
            # Race 18: Singapore
            {"race": 17, "results": [
                ("George Russell", "Mercedes", 25), ("Lewis Hamilton", "Ferrari", 18), 
                ("Lando Norris", "McLaren", 15), ("Oscar Piastri", "McLaren", 12), 
                ("Max Verstappen", "Red Bull", 10), ("Kimi Antonelli", "Mercedes", 8),
                ("Fernando Alonso", "Aston Martin", 6), ("Charles Leclerc", "Ferrari", 4), 
                ("Carlos Sainz", "Williams", 2), ("Esteban Ocon", "Haas", 1)
            ]},
            # Race 19: United States
            {"race": 18, "results": [
                ("Max Verstappen", "Red Bull", 25), ("Lando Norris", "McLaren", 18), 
                ("Oscar Piastri", "McLaren", 15), ("Kimi Antonelli", "Mercedes", 12), 
                ("George Russell", "Mercedes", 10), ("Oliver Bearman", "Haas", 8),
                ("Charles Leclerc", "Ferrari", 6), ("Lewis Hamilton", "Ferrari", 4), 
                ("Carlos Sainz", "Williams", 2), ("Fernando Alonso", "Aston Martin", 1)
            ]},
            # Race 20: Mexico
            {"race": 19, "results": [
                ("Lando Norris", "McLaren", 25), ("George Russell", "Mercedes", 18), 
                ("Oscar Piastri", "McLaren", 15), ("Carlos Sainz", "Williams", 12), 
                ("Lewis Hamilton", "Ferrari", 10), ("Max Verstappen", "Red Bull", 8),
                ("Charles Leclerc", "Ferrari", 6), ("Esteban Ocon", "Haas", 4), 
                ("Nico Hulkenberg", "Sauber", 2), ("Fernando Alonso", "Aston Martin", 1)
            ]},
            # Race 21: Brazil
            {"race": 20, "results": [
                ("Lando Norris", "McLaren", 25), ("Oscar Piastri", "McLaren", 18), 
                ("Alex Albon", "Williams", 15), ("Lewis Hamilton", "Ferrari", 12), 
                ("Charles Leclerc", "Ferrari", 10), ("Kimi Antonelli", "Mercedes", 8),
                ("George Russell", "Mercedes", 6), ("Fernando Alonso", "Aston Martin", 4), 
                ("Esteban Ocon", "Haas", 2), ("Carlos Sainz", "Williams", 1)
            ]},
            # Race 22: Las Vegas
            {"race": 21, "results": [
                ("Max Verstappen", "Red Bull", 25), ("Lando Norris", "McLaren", 18), 
                ("Oscar Piastri", "McLaren", 15), ("George Russell", "Mercedes", 12), 
                ("Charles Leclerc", "Ferrari", 10), ("Lewis Hamilton", "Ferrari", 8),
                ("Kimi Antonelli", "Mercedes", 6), ("Carlos Sainz", "Williams", 4), 
                ("Nico Hulkenberg", "Sauber", 2), ("Esteban Ocon", "Haas", 1)
            ]},
            # Race 23: Qatar
            {"race": 22, "results": [
                ("Max Verstappen", "Red Bull", 25), ("Oscar Piastri", "McLaren", 18), 
                ("Lando Norris", "McLaren", 15), ("George Russell", "Mercedes", 12), 
                ("Charles Leclerc", "Ferrari", 10), ("Lewis Hamilton", "Ferrari", 8),
                ("Fernando Alonso", "Aston Martin", 6), ("Kimi Antonelli", "Mercedes", 4), 
                ("Liam Lawson", "Racing Bulls", 2), ("Isack Hadjar", "Racing Bulls", 1)
            ]},
            # Race 24: Abu Dhabi (FINALE)
            {"race": 23, "results": [
                ("Max Verstappen", "Red Bull", 25), ("Charles Leclerc", "Ferrari", 18), 
                ("Oscar Piastri", "McLaren", 15), ("Lewis Hamilton", "Ferrari", 12), 
                ("Lando Norris", "McLaren", 10), ("George Russell", "Mercedes", 8),
                ("Carlos Sainz", "Williams", 6), ("Kimi Antonelli", "Mercedes", 4), 
                ("Esteban Ocon", "Haas", 2), ("Nico Hulkenberg", "Sauber", 1)
            ]},
        ]