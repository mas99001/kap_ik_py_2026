# ============================================================
# 📌 Mission 1 — The Crew Roster
# ============================================================
def build_crew_roster(members, new_member, position):
    members_l = members.copy()
    members_l.insert(position, new_member)
    return members_l

def get_fighters(crew_data):
    fighters = []
    for x in crew_data.items():
        if (x[1]["power"] > 80):
            fighters.append(x[0])
    return fighters

def reverse_roster(roster):
    return (roster[::-1])

# ============================================================
# ⚔️ Mission 2 — The Devil Fruit Encyclopedia
# ============================================================
def lookup_fruit(fruits, fruit_name):
    return fruits.get(fruit_name,"Unknown fruit")
'''
    for x in fruits.items():
        if(x[0] == fruit_name ):
            return x[1]
    return "Unknown fruit"
'''
def find_fruits_by_type(fruits, fruit_type):
    f = {}
    for x in fruits.items():
        if(x[1]["type"] == fruit_type ):
            f = f | {x[0]:x[1]}
    return f
# use comprehension

def fruit_users(fruits):
    f = {}
    for x in fruits.items():
        f = f | {x[1]["user"] : x[0]}
    return f
# use comprehension

# ============================================================
# ⚔️ Mission 3 — Island Intelligence
# ============================================================
def island_overlap(crew_a_islands, crew_b_islands):
    return crew_a_islands.intersection(crew_b_islands)
    #S1 + S2 will also work here
def unique_to_crew(crew_islands, other_islands):
    return crew_islands.difference(other_islands)
    #S1 - S2 will also work here
def all_known_islands(crew_a_islands, crew_b_islands):
    return (crew_a_islands.difference(crew_b_islands) | crew_b_islands.difference(crew_a_islands) | crew_a_islands.intersection(crew_b_islands))
    #Try using union
# ============================================================
# ⚔️ Mission 4 — Luffy's Stretch Calculator
# ============================================================
def stretch_attack(enemy_distance, base_reach=15, gear="normal", base_power=100):
    can_reach = (base_reach >= enemy_distance)
    reach = base_reach
    gap = base_reach - enemy_distance
    power = base_power
    if(gear == "normal"):
        reach = base_reach
        power = base_power
        can_reach = (reach >= enemy_distance)
        gap = reach - enemy_distance
        return({"can_reach": can_reach, "reach":reach, "gap":gap, "power":power, "gear":gear})
    elif(gear == "gear2"):
        reach = base_reach * 1.5
        power = base_power * 1.2
        can_reach = (reach >= enemy_distance)
        gap = reach - enemy_distance
        return({"can_reach": can_reach, "reach":reach, "gap":gap, "power":power, "gear":gear})
    elif(gear == "gear3"):
        reach = base_reach * 2.0
        power = base_power * 0.7
        can_reach = (reach >= enemy_distance)
        gap = reach - enemy_distance
        return({"can_reach": can_reach, "reach":reach, "gap":gap, "power":power, "gear":gear})
    else:
        return({"can_reach": can_reach, "reach":reach, "gap":gap, "power":power, "gear":gear})

# ============================================================
# ⚔️ Mission 5 — Zoro's Sword Combinations
# ============================================================
def sword_combinations(swords):
    swords_list = [{"name": name, **stats} for name, stats in swords.items()]
    swords_list_n = []
    for x in range(0,len(swords_list)):
        for y in range(x+1, len(swords_list)):
            swords_list_n.append({"sword_1": swords_list[x]['name'], "sword_2": swords_list[y]['name'], 'combined_attack': swords_list[x]['attack']+swords_list[y]['attack'], 'combined_weight': swords_list[x]['weight']+swords_list[y]['weight']})
    return swords_list_n

def best_combo_against(swords, enemy_defense):
    combos = sword_combinations(swords)
    max_p = max(combos, key=lambda c: c["combined_attack"])
    attack = max_p["combined_attack"]
    win_chance = min(attack / enemy_defense, 1.0)
    return {"best_combo": (max_p["sword_1"], max_p["sword_1"]), "attack": max_p["combined_attack"], "enemy_defense": enemy_defense, "win_chance": win_chance}

# ============================================================
# ⚔️ MISSION 6 — SANJI'S SKY WALK
# ============================================================
def sky_walk(enemy_height, base_kick_power=88, kick_height=6, wind_resistance=1.5, max_altitude=60, stamina=100, stamina_per_kick=12):
    reached = False
    altitude = 0.0
    kicks_used = 0
    stamina_left = stamina
    kick_power = 0.0
    can_defeat = False
    enemy_defense = 100
    while((stamina_left >= stamina_per_kick) and (altitude < enemy_height) and (altitude < max_altitude)):
        stamina_left = stamina_left - stamina_per_kick
        altitude = altitude + kick_height - wind_resistance
        altitude = min(altitude, max_altitude)
        kicks_used += 1
    reached = (altitude >= enemy_height)
    kick_power = round(base_kick_power * (1 + altitude / 100.0),1)
    can_defeat = (kick_power > enemy_defense)
    return {"reached":reached, "altitude":altitude, "kicks_used":kicks_used, "stamina_left":stamina_left, "kick_power":kick_power, "can_defeat":can_defeat}