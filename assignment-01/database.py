HEROES = {
    "Iron Man": {"real_name": "Tony Stark", "power": 92, "health": 85, "stone": "Power", "is_compromised": False},
    "Thor": {"real_name": "Thor Odinson", "power": 95, "health": 45, "stone": "Space", "is_compromised": False},
    "Cap": {"real_name": "Steve Rogers", "power": 68, "health": 78, "stone": "Time", "is_compromised": True},
}

STONES = {
    "Power": {"signature": "PWR-0891-STARK", "guardian": "Iron Man"},
    "Space": {"signature": "SPC-0447-ODIN", "guardian": "Thor"},
    "Time": {"signature": "TME-1942-ROGERS", "guardian": "Cap"},
}

STONE_READINGS = {
    "Power": {"raw_power": 87.5, "stability": 0.92, "guardian_bonus": 10},
    "Space": {"raw_power": 95.0, "stability": 0.45, "guardian_bonus": 15},
    "Time": {"raw_power": 72.0, "stability": 0.88, "guardian_bonus": 8},
}

FURY_TRANSMISSIONS = [
    "EOXQW#DVVHPEOH#DW#VHFWRU#VHYHQ",
    "WKDQRV#LV#FRPLQJ",
]

CHITAURI_WAVES = [
    {"wave": 1, "sector": "A", "ships": 200, "power_each": 5},
    {"wave": 2, "sector": "B", "ships": 450, "power_each": 7},
    {"wave": 3, "sector": "A", "ships": 0, "power_each": 0},
]