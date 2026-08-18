import subprocess
# Clear screen on Windows
subprocess.run("cls", shell=True)
# ═══════════════════════════════════════════════════════════════
# S.H.I.E.L.D. DATABASE — Run this cell FIRST
# ═══════════════════════════════════════════════════════════════
from database import HEROES, STONES, STONE_READINGS, FURY_TRANSMISSIONS, CHITAURI_WAVES
print("\u2705 S.H.I.E.L.D. database loaded.")
print(f" -> Heroes: {len(HEROES)} | Stones: {len(STONES)} | Waves: {len(CHITAURI_WAVES)}")
# ═══════════════════════════════════════════════════════════════
# Mission 1 — Hero Profile Decoder
# ═══════════════════════════════════════════════════════════════
from functions import decode_hero_profile
# ── Tests ─────────────────────────────────────────────────────
t1 = decode_hero_profile({"name": "Iron Man", "power": "92", "health": "85.5", "is_compromised": "0"})
assert t1["power"] == 92 and type(t1["power"]) == int
assert t1["health"] == 85.5 and type(t1["health"]) == float
assert t1["is_compromised"] == False and type(t1["is_compromised"]) == bool

t2 = decode_hero_profile({"name": "Cap", "power": "68", "health": "78.2", "is_compromised": "1"})
assert t2["is_compromised"] == True

print("\u2705 Mission 1 COMPLETE — Hero profiles decoded!")
# ═══════════════════════════════════════════════════════════════
# Mission 2 — Stone Power Calibrator
# ═══════════════════════════════════════════════════════════════
from functions import calibrate_stone 
ep, st = calibrate_stone(87.5, 0.92, 10)
assert ep == 90.5 and st == "OPTIMAL"
ep2, st2 = calibrate_stone(95.0, 0.45, 15)
assert ep2 == 57.75 and st2 == "STABLE"
ep3, st3 = calibrate_stone(72.0, 0.88, 8)
assert ep3 == 71.36 and st3 == "STABLE"
print("\u2705 Mission 2 COMPLETE — Stone calibration online!")
# ═══════════════════════════════════════════════════════════════
# Mission 3 — Decrypt Fury's Distress Signal
# ═══════════════════════════════════════════════════════════════
from functions import decrypt_caesar, parse_stone_signature

assert decrypt_caesar("EOXQW#DVVHPEOH#DW#VHFWRU#VHYHQ", 3) == "BLUNT ASSEMBLE AT SECTOR SEVEN"
assert decrypt_caesar("WKDQRV#LV#FRPLQJ", 3) == "THANOS IS COMING"
assert parse_stone_signature("PWR-0891-STARK") == ("PWR", 891, "Stark")
assert parse_stone_signature("TME-1942-ROGERS") == ("TME", 1942, "Rogers")

print("\u2705 Mission 3 COMPLETE — Messages decrypted!")
print("   -> BLUNT ASSEMBLE AT SECTOR SEVEN")
print("   -> THANOS IS COMING")

# ═══════════════════════════════════════════════════════════════
# Mission 4 — Battle Readiness Scanner
# ═══════════════════════════════════════════════════════════════
from functions import classify_hero
assert classify_hero("Iron Man", 85, 92, False) == "DEPLOY"
assert classify_hero("Thor", 45, 95, False) == "BACKUP"
assert classify_hero("Cap", 78, 68, True) == "BENCHED"
assert classify_hero("Test", 20, 30, False) == "BENCHED"

print("\u2705 Mission 4 COMPLETE — Battle Readiness online!")
print("\u2714   Iron Man: DEPLOY")
print("\u2714   Thor:     BACKUP")
print("\u2714   Cap:      BENCHED (compromised)")

# ═══════════════════════════════════════════════════════════════
# Mission 5 — Threat Wave Analyzer
# ═══════════════════════════════════════════════════════════════
from functions import analyze_waves
result = analyze_waves(CHITAURI_WAVES)
assert result["total_threat"] == 4150, f"total wrong: {result['total_threat']}"
assert result["wave_count"] == 2, f"count wrong: {result['wave_count']}"
assert result["deadliest_wave"] == 2, f"deadliest wrong: {result['deadliest_wave']}"

print("\u2705 Mission 5 COMPLETE — Threat analysis online!")
print(f"\u2714   Total threat: {result['total_threat']}")
print(f"\u2714   Deadliest: wave #{result['deadliest_wave']}")
###################################
# Mission 6 — Infinity Gauntlet Simulator
###################################
from functions import simulate_gauntlet

result = simulate_gauntlet(HEROES, 120)
assert result["stones_taken"][0] == "Time", f"First stone should be Time (Cap=68), got {result['stones_taken'][0]}"
assert result["outcome"] in ["SNAP", "BLOCKED"]
assert result["rounds"] >= 1

weak = simulate_gauntlet(HEROES, 10)
assert weak["outcome"] == "BLOCKED"
assert weak["stones_taken"] == []

print("\u2705 Mission 6 COMPLETE — Gauntlet simulator running!")
print(f"\u2714   Outcome: {result['outcome']}")
print(f"\u2714   Rounds: {result['rounds']}")
print(f"\u2714   Stones taken: {result['stones_taken']}")
if result["blocked_by"]:
    print(f"\u2714   BLOCKED BY: {result['blocked_by']}")
for log in result["battle_log"]:
    print(f"\u2713   {log}")
