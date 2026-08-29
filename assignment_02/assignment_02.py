import numpy as np
import subprocess
# Clear screen on Windows
subprocess.run("cls", shell=True)

# ============================================================
# 🏴‍☠️ GRAND LINE SAGA
# ============================================================
from assignment_02.databse_02 import CREW, DEVIL_FRUITS, ZORO_SWORDS
from assignment_02.functions_02 import build_crew_roster, get_fighters, reverse_roster
from assignment_02.functions_02 import lookup_fruit, find_fruits_by_type, fruit_users
from assignment_02.functions_02 import all_known_islands, island_overlap, unique_to_crew
from assignment_02.functions_02 import stretch_attack
from assignment_02.functions_02 import sword_combinations, best_combo_against
from assignment_02.functions_02 import sky_walk
# ============================================================
# 📌 Mission 1 — The Crew Roster
# ============================================================
# ── Tests (do NOT modify) ─────────────────────────────────────
r1 = build_crew_roster(["Luffy", "Zoro", "Nami"], "Jinbe", 2)
assert r1 == ["Luffy", "Zoro", "Jinbe", "Nami"], f"Got {r1}"

r2 = build_crew_roster(["Luffy", "Zoro"], "Sanji", 0)
assert r2 == ["Sanji", "Luffy", "Zoro"], f"Got {r2}"

fighters = get_fighters(CREW)
assert "Luffy" in fighters and "Zoro" in fighters and "Sanji" in fighters
assert "Nami" not in fighters

rev = reverse_roster(["Luffy", "Zoro", "Nami"])
assert rev == ["Nami", "Zoro", "Luffy"]

print("\u2705 Mission 1 COMPLETE — Crew roster ready!")
print(f"   Roster with Jinbe: {r1}")
print(f"   Fighters (power > 80): {fighters}")

# ============================================================
# ⚔️ Mission 2 — The Devil Fruit Encyclopedia
# ============================================================
# ── Tests (do NOT modify) ─────────────────────────────────────
r1 = lookup_fruit(DEVIL_FRUITS, "Gomu Gomu")
assert r1["user"] == "Luffy" and r1["type"] == "Paramecia"

r2 = lookup_fruit(DEVIL_FRUITS, "Fake Fruit")
assert r2 == "Unknown fruit"

logias = find_fruits_by_type(DEVIL_FRUITS, "Logia")
assert len(logias) == 2 and "Mera Mera" in logias

users = fruit_users(DEVIL_FRUITS)
assert users["Luffy"] == "Gomu Gomu" and users["Robin"] == "Hana Hana"

print("\u2705 Mission 2 COMPLETE — Devil Fruit Encyclopedia built!")
print(f"   Logia fruits: {list(logias.keys())}")
print(f"   Luffy ate: {users['Luffy']}")

# ============================================================
# ⚔️ Mission 3 — Island Intelligence
# ============================================================
# ── Tests (do NOT modify) ─────────────────────────────────────
straw_hat_islands = {"Alabasta", "Water 7", "Dressrosa", "Whole Cake", "Wano"}
heart_pirate_islands = {"Dressrosa", "Wano", "Zou", "Sabaody"}

overlap = island_overlap(straw_hat_islands, heart_pirate_islands)
assert overlap == {"Dressrosa", "Wano"}, f"Got {overlap}"

only_sh = unique_to_crew(straw_hat_islands, heart_pirate_islands)
assert only_sh == {"Alabasta", "Water 7", "Whole Cake"}, f"Got {only_sh}"

all_isl = all_known_islands(straw_hat_islands, heart_pirate_islands)
assert len(all_isl) == 7

print("\u2705 Mission 3 COMPLETE — Island intel gathered!")
print(f"   Both visited: {overlap}")
print(f"   Only Straw Hats: {only_sh}")
print(f"   Total unique islands: {len(all_isl)}")

# ============================================================
# 🏴‍☠️ Act II — Battle on the Grand Line
# ============================================================
# ============================================================
# ⚔️ Mission 4 — Luffy's Stretch Calculator
# ============================================================
# ── Tests (do NOT modify) ─────────────────────────────────────
r1 = stretch_attack(10)
assert r1["can_reach"] == True and r1["reach"] == 15 and r1["gap"] == 5 and r1["power"] == 100

r2 = stretch_attack(22)
assert r2["can_reach"] == False and r2["gap"] == -7

r3 = stretch_attack(22, gear="gear2")
assert r3["can_reach"] == True and r3["reach"] == 22.5 and r3["power"] == 120.0

r4 = stretch_attack(25, gear="gear3")
assert r4["can_reach"] == True and r4["reach"] == 30 and r4["power"] == 70.0

r5 = stretch_attack(35, gear="gear3")
assert r5["can_reach"] == False

print("\u2705 Mission 4 COMPLETE — Stretch calculator ready!")
print(f"   10m normal: reach={r1['reach']}m, can_reach={r1['can_reach']}")
print(f"   22m gear2:  reach={r3['reach']}m, power={r3['power']}")
print(f"   25m gear3:  reach={r4['reach']}m, power={r4['power']}")

# ============================================================
# ⚔️ Mission 5 — Zoro's Sword Combinations
# ============================================================
# ── Tests (do NOT modify) ─────────────────────────────────────
combos = sword_combinations(ZORO_SWORDS)
assert len(combos) == 3, f"3 swords = 3 combos, got {len(combos)}"

attacks = [c["combined_attack"] for c in combos]
assert 175 in attacks and 150 in attacks and 165 in attacks

best = best_combo_against(ZORO_SWORDS, 140)
assert best["attack"] == 175 and best["win_chance"] == 1.0

weak = best_combo_against(ZORO_SWORDS, 200)
assert weak["win_chance"] == 175 / 200

print("\u2705 Mission 5 COMPLETE — Sword combos calculated!")
print(f"   Combos: {[(c['sword_1'], c['sword_2'], c['combined_attack']) for c in combos]}")
print(f"   Best vs 140 def: {best['best_combo']}, win={best['win_chance']:.0%}")
print(f"   Best vs 200 def: win={weak['win_chance']:.1%}")

# ============================================================
# ⚔️ MISSION 6 — SANJI'S SKY WALK
# ============================================================
# ── Tests (do NOT modify) ─────────────────────────────────────
r1 = sky_walk(20)
assert r1["reached"] == True
assert r1["altitude"] == 22.5  # 5 kicks * 4.5m
assert r1["kicks_used"] == 5
assert r1["stamina_left"] == 40
assert r1["kick_power"] == 107.8  # 88 * (1 + 22.5/100)

r2 = sky_walk(100)
assert r2["reached"] == False  # can't reach 100m

r3 = sky_walk(10)
assert r3["reached"] == True
assert r3["kicks_used"] == 3  # 3 * 4.5 = 13.5 >= 10

r4 = sky_walk(50, stamina=36, stamina_per_kick=12)
assert r4["kicks_used"] == 3  # only enough stamina for 3 kicks
assert r4["reached"] == False  # 3 * 4.5 = 13.5 < 50

print("\u2705 Mission 6 COMPLETE — Sky Walk calculated!")
print(f"   20m enemy: reached={r1['reached']}, {r1['kicks_used']} kicks, power={r1['kick_power']}")
print(f"   100m enemy: reached={r2['reached']} (too high!)")
print(f"   Low stamina test: {r4['kicks_used']} kicks, reached={r4['reached']}")
