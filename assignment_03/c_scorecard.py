# ═══════════════════════════════════════════════════════════════
# MISSION 6 — LIVE MATCH SCORECARD
# Concepts: OOP + inheritance + error handling + file I/O
# ═══════════════════════════════════════════════════════════════
from c_cricketclub import CricketClub, InvalidOversError
import json
cd = CricketClub()
class Scorecard:
    def __init__(self, team_name, max_overs):
        # Store team_name, max_overs
        # Initialize total_runs=0, wickets=0, balls=0, deliveries=[]
        self.team_name = team_name
        self.max_overs = max_overs
        self.total_runs=0
        self.wickets=0
        self.balls=0
        self.deliveries=[]

    def add_ball(self, runs):
        # Step 1: Check if innings is over (balls >= max_overs * 6 or wickets >= 10)
        #         If yes, raise InvalidOversError
        # Step 2: Validate runs using validate_delivery() from Mission 2
        # Step 3: Add runs to total_runs, increment balls, append to deliveries
        if((self.balls >= self.max_overs * 6) or (self.wickets >= 10)):
            raise InvalidOversError
        if(cd.validate_delivery(runs)):
            self.total_runs += runs
            self.balls += 1
            self.deliveries.append(runs)

    def add_wicket(self):
        # Step 1: If wickets >= 10, raise InvalidOversError
        # Step 2: Increment wickets and balls (wicket = legal delivery)
        if(self.wickets >= 10):
            raise InvalidOversError
        else:
            self.wickets += 1
            self.balls += 1

    def current_over(self):
        # overs = balls // 6, remaining = balls % 6
        # Return as string "overs.remaining"
        overs = self.balls // 6
        remaining = self.balls % 6
        return (f'{overs}.{remaining}')

    def run_rate(self):
        # total_runs / (balls / 6), handle 0 balls, round to 2
        if(self.balls == 0):
            return 0.00
        return round((self.total_runs / (self.balls / 6)),2)

    def save_json(self, filename):
        # Build a dict with team_name, total_runs, wickets, balls,
        # current_over, run_rate, deliveries
        # Use json.dump() with indent=2
        data = {"team_name": self.team_name, "total_runs": self.total_runs, "wickets": self.wickets, "balls":self.balls, "current_over": self.current_over(), "run_rate": self.run_rate(), "deliveries": self.deliveries }
        with open(filename, "w") as file:
            json.dump(data, file, indent=2)
        
    def __str__(self):
        # "TeamName: runs/wickets in current_over overs (RR: run_rate)"
        return (f"{self.team_name}: {self.total_runs}/{self.wickets} in {self.current_over()} {self.max_overs} (RR: {self.run_rate()})")

class T20Scorecard(Scorecard):
    # __init__ takes only team_name, passes max_overs=20 to super()
    def __init__(self, team_name, max_overs=20):
        super().__init__(team_name, max_overs)


class ODIScorecard(Scorecard):
    # __init__ takes only team_name, passes max_overs=50 to super()
    def __init__(self, team_name, max_overs=50):
        super().__init__(team_name, max_overs)