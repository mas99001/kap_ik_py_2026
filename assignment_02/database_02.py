# ═══════════════════════════════════════════════════════════════
# CREW DATABASE — Run this cell FIRST
# ═══════════════════════════════════════════════════════════════

CREW = {
    "Luffy": {"role": "Captain",       "bounty": 3_000_000_000, "has_devil_fruit": True,  "power": 95},
    "Zoro":  {"role": "Swordsman",     "bounty": 1_111_000_000, "has_devil_fruit": False, "power": 90},
    "Nami":  {"role": "Navigator",     "bounty":   366_000_000, "has_devil_fruit": False, "power": 55},
    "Sanji": {"role": "Cook",          "bounty": 1_032_000_000, "has_devil_fruit": False, "power": 88},
    "Robin": {"role": "Archaeologist", "bounty":   930_000_000, "has_devil_fruit": True,  "power": 70},
}

DEVIL_FRUITS = {
    "Gomu Gomu": {"type": "Paramecia", "ability": "Rubber body",        "user": "Luffy"},
    "Hana Hana": {"type": "Paramecia", "ability": "Sprout extra limbs", "user": "Robin"},
    "Mera Mera": {"type": "Logia",     "ability": "Control fire",       "user": "Sabo"},
    "Hie Hie":   {"type": "Logia",     "ability": "Control ice",        "user": "Aokiji"},
    "Gura Gura": {"type": "Paramecia", "ability": "Create earthquakes", "user": "Whitebeard"},
}

ZORO_SWORDS = {
    "Wado Ichimonji": {"attack": 80, "weight": 5},
    "Sandai Kitetsu": {"attack": 70, "weight": 4},
    "Enma":           {"attack": 95, "weight": 7},
}

print("\u2705 Crew data loaded!")
print(f"   Crew members: {list(CREW.keys())}")
print(f"   Devil Fruits known: {len(DEVIL_FRUITS)}")
print(f"   Zoro\'s swords: {list(ZORO_SWORDS.keys())}")