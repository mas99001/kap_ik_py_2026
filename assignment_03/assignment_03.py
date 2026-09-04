import subprocess as sp
import json
sp.run('cls', shell=True)
from c_cricketclub import CricketClub, InvalidDeliveryError, InvalidOversError
from c_players import Player, Batsman, Bowler, AllRounder
from c_scorecard import Scorecard, T20Scorecard, ODIScorecard
#
# SQUAD DATABASE — Run this cell FIRST
#
SQUAD = [
    {"name": "Virat Kohli",    "role": "Batsman",     "team": "RCB", "runs": 741,  "balls_faced": 578, "wickets": 0,  "overs_bowled": 0,   "runs_conceded": 0,   "matches": 15, "outs": 12},
    {"name": "Rohit Sharma",   "role": "Batsman",     "team": "MI",  "runs": 416,  "balls_faced": 310, "wickets": 0,  "overs_bowled": 0,   "runs_conceded": 0,   "matches": 14, "outs": 13},
    {"name": "Jasprit Bumrah", "role": "Bowler",      "team": "MI",  "runs": 8,    "balls_faced": 12,  "wickets": 20, "overs_bowled": 56,  "runs_conceded": 385, "matches": 14, "outs": 3},
    {"name": "Rashid Khan",    "role": "Bowler",      "team": "GT",  "runs": 122,  "balls_faced": 80,  "wickets": 18, "overs_bowled": 52,  "runs_conceded": 312, "matches": 15, "outs": 6},
    {"name": "Hardik Pandya",  "role": "AllRounder",  "team": "MI",  "runs": 487,  "balls_faced": 321, "wickets": 11, "overs_bowled": 38,  "runs_conceded": 310, "matches": 15, "outs": 10},
    {"name": "Ravindra Jadeja","role": "AllRounder",  "team": "CSK", "runs": 378,  "balls_faced": 250, "wickets": 14, "overs_bowled": 48,  "runs_conceded": 338, "matches": 14, "outs": 8},
    {"name": "Jos Buttler",    "role": "Batsman",     "team": "RR",  "runs": 863,  "balls_faced": 540, "wickets": 0,  "overs_bowled": 0,   "runs_conceded": 0,   "matches": 17, "outs": 14},
]
print("\u2705 Squad loaded!")
print(f"   Players: {len(SQUAD)}")
for p in SQUAD:
    print(f"   {p['name']:<18} | {p['role']:<12} | {p['team']}")
#
# ⚔️ Mission 1 — The Player Database
#
cc = CricketClub()
cc.save_players_csv(SQUAD, "cricket_playes.csv")
loaded = cc.load_players_csv("cricket_playes.csv")

assert len(loaded) == 7, f"Should load 7 players, got {len(loaded)}"
assert loaded[0]["name"] == "Virat Kohli"
assert loaded[0]["runs"] == 741 and type(loaded[0]["runs"]) == int, "runs must be int, not str"
assert loaded[2]["wickets"] == 20 and type(loaded[2]["wickets"]) == int
assert loaded[0]["role"] == "Batsman" and type(loaded[0]["role"]) == str

print("\u2705 Mission 1 COMPLETE — Player database ready!")
print(f"   Saved {len(SQUAD)} players to CSV")
print(f"   Loaded back: {loaded[0]['name']} — {loaded[0]['runs']} runs (type: {type(loaded[0]['runs']).__name__})")
#
#⚔️ Mission 2 — Crash-Proof Scoring
#
# ── Tests (do NOT modify) ─────────────────────────────────────
assert cc.calculate_strike_rate(741, 578) == 128.2
assert cc.calculate_strike_rate(0, 0) == 0.0

try:
    cc.calculate_strike_rate(-5, 10)
    assert False, "Should have raised ValueError"
except ValueError:
    pass  # Expected

assert cc.validate_delivery(4) == True
assert cc.validate_delivery(0) == True

try:
    cc.validate_delivery(-1)
    assert False, "Should have raised InvalidDeliveryError"
except InvalidDeliveryError:
    pass  # Expected

try:
    cc.validate_delivery(10)
    assert False, "Should have raised InvalidDeliveryError"
except InvalidDeliveryError:
    pass  # Expected

assert cc.safe_score_ball(4) == 4
assert cc.safe_score_ball(6) == 6
assert cc.safe_score_ball(-1) == -1
assert cc.safe_score_ball(99) == -1

print("\u2705 Mission 2 COMPLETE — Crash-proof scoring system ready!")
print("   Strike rate (741/578): 128.2")
print("   Invalid delivery (-1): caught and flagged")
print("   Safe scorer (99 runs): returned -1 (flagged)")
#
# ⚔️ Mission 3 — The Player Class
#
# ── Tests (do NOT modify) ─────────────────────────────────────
kohli = Player("Virat Kohli", "Batsman", "RCB", 741, 578, 0, 0, 0, 15, 12)
assert kohli.name == "Virat Kohli"
assert kohli.batting_avg() == 61.75
assert kohli.strike_rate() == 128.2
assert "Virat Kohli" in str(kohli) and "61.75" in str(kohli)

bumrah = Player("Jasprit Bumrah", "Bowler", "MI", 8, 12, 20, 56, 385, 14, 3)
assert bumrah.batting_avg() == 2.67
assert bumrah.strike_rate() == 66.67

# Edge case: player who never got out
newbie = Player("New Guy", "Batsman", "MI", 50, 30, 0, 0, 0, 1, 0)
assert newbie.batting_avg() == 0.0  # can't divide by 0 outs

print("\u2705 Mission 3 COMPLETE — Player class ready!")
print(f"   {kohli}")
print(f"   {bumrah}")
#
# ⚔️ Mission 4 — Specialized Players
#
# ── Tests (do NOT modify) ─────────────────────────────────────
kohli = Batsman("Virat Kohli", "Batsman", "RCB", 741, 578, 0, 0, 0, 15, 12)
assert kohli.batting_avg() == 61.75  # inherited from Player
assert kohli.performance_rating() == 88.33

bumrah = Bowler("Jasprit Bumrah", "Bowler", "MI", 8, 12, 20, 56, 385, 14, 3)
assert bumrah.economy_rate() == 6.88
assert bumrah.performance_rating() == 25.6

hardik = AllRounder("Hardik Pandya", "AllRounder", "MI", 487, 321, 11, 38, 310, 15, 10)
assert hardik.batting_avg() == 48.7
assert isinstance(hardik, Player)  # AllRounder IS a Player
assert hardik.performance_rating() > 0

print("\u2705 Mission 4 COMPLETE — Specialized player types ready!")
print(f"   Kohli (Batsman) rating: {kohli.performance_rating()}")
print(f"   Bumrah (Bowler) rating: {bumrah.performance_rating()}")
print(f"   Hardik (AllRounder) rating: {hardik.performance_rating()}")
#
# ⚔️ Mission 5 — Squad Analyzer
#
def analyze_squad(squad_list):
    result = {"ratings": [], "batsmen": [], "bowlers": [], "all_rounders": [], "mvp": ''}
    for player in squad_list:
        result["ratings"].append((player.name, player.role, player.performance_rating()))
        if(isinstance(player, Batsman)):
            result["batsmen"].append(player.name)
        if(isinstance(player, Bowler)):
            result["bowlers"].append(player.name)
        if(isinstance(player, AllRounder)):
            result["all_rounders"].append(player.name)
    result["ratings"].sort(key=lambda item:item[2], reverse=True)
    result["mvp"] = result["ratings"][0][0]
    return result

# ── Tests (do NOT modify) ─────────────────────────────────────
squad = [
    Batsman("Virat Kohli", "Batsman", "RCB", 741, 578, 0, 0, 0, 15, 12),
    Batsman("Jos Buttler", "Batsman", "RR", 863, 540, 0, 0, 0, 17, 14),
    Bowler("Jasprit Bumrah", "Bowler", "MI", 8, 12, 20, 56, 385, 14, 3),
    Bowler("Rashid Khan", "Bowler", "GT", 122, 80, 18, 52, 312, 15, 6),
    AllRounder("Hardik Pandya", "AllRounder", "MI", 487, 321, 11, 38, 310, 15, 10),
    AllRounder("Ravindra Jadeja", "AllRounder", "CSK", 378, 250, 14, 48, 338, 14, 8),
]

result = analyze_squad(squad)

assert len(result["ratings"]) == 6
assert result["ratings"][0][2] >= result["ratings"][1][2]  # sorted descending
assert len(result["batsmen"]) == 2
assert len(result["bowlers"]) == 2
assert len(result["all_rounders"]) == 2
assert result["mvp"] in ["Virat Kohli", "Jos Buttler"]  # batsmen likely have highest rating

print("\u2705 Mission 5 COMPLETE — Squad analyzed!")
print(f"   MVP: {result['mvp']}")
print(f"   Batsmen: {result['batsmen']}")
print(f"   Bowlers: {result['bowlers']}")
print(f"   AllRounders: {result['all_rounders']}")
print("\n   Ratings (sorted):")
for name, role, rating in result["ratings"]:
    print(f"   {name:<18} {role:<12} {rating:.2f}")

#
# ⚔️ Mission 6 — Live Match Scorecard
#
# ── Tests (do NOT modify) ─────────────────────────────────────

sc = T20Scorecard("Mumbai Indians")
sc.add_ball(4)
sc.add_ball(0)
sc.add_ball(6)
sc.add_ball(1)
sc.add_ball(2)
sc.add_wicket()

assert sc.total_runs == 13
assert sc.wickets == 1
assert sc.balls == 6
assert sc.current_over() == "1.0"
assert sc.run_rate() == 13.0

# Test invalid delivery
assert cc.safe_score_ball(-5) == -1  # uses Mission 2 function

# Test innings limit
try:
    sc_test = T20Scorecard("Test")
    for i in range(120):  # 20 overs = 120 balls
        sc_test.add_ball(1)
    try:
        sc_test.add_ball(1)  # 121st ball — should fail
        assert False, "Should have raised InvalidOversError"
    except InvalidOversError:
        pass
except Exception as e:
    print(f"Note: {e}")

# Test save
sc.save_json("test_scorecard.json")
with open("test_scorecard.json", "r") as f:
    saved = json.load(f)
assert saved["team_name"] == "Mumbai Indians"
assert saved["total_runs"] == 13

# Test isinstance
assert isinstance(sc, Scorecard)
assert isinstance(sc, T20Scorecard)

odi = ODIScorecard("India")
assert odi.max_overs == 50

print("\u2705 Mission 6 COMPLETE — Live scorecard system ready!")
print(f"   {sc}")
print(f"   Saved to test_scorecard.json")