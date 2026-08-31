class Player:
    def __init__(self, name, role, team, runs, balls_faced, wickets, overs_bowled, runs_conceded, matches, outs):
        # Store all parameters as instance attributes using self.
        self.name = name
        self.role = role
        self.team = team
        self.runs = runs
        self.balls_faced = balls_faced
        self.wickets = wickets
        self.overs_bowled = overs_bowled
        self.runs_conceded = runs_conceded
        self.matches = matches
        self.outs = outs


    def batting_avg(self):
        # Return runs / outs (handle outs == 0 → return 0.0)
        if (self.outs == 0):
            return 0.0
        return round((self.runs / self.outs),2)
    
    def strike_rate(self):
        # Return (runs / balls_faced) * 100 (handle 0 balls → return 0.0)
        if (self.balls_faced == 0):
            return 0.0
        return round(((self.runs / self.balls_faced)*100), 2)

    def __str__(self):
        # Return: "Name | Role | Team | X runs | Avg: Y | SR: Z"
        stats = []
        stats.append(self.name)
        stats.append(self.role)
        stats.append(self.team)
        stats.append(f'{self.runs} runs')
        stats.append(f'Avg: {self.batting_avg()}')
        stats.append(f'SR: {self.strike_rate()}')
        return " | ".join(str(val) for val in stats)

class Batsman(Player):
    def __init__(self, name, role, team, runs, balls_faced, wickets, overs_bowled, runs_conceded, matches, outs):
        super().__init__(name, role, team, runs, balls_faced, wickets, overs_bowled, runs_conceded, matches, outs)
    def performance_rating(self):
        return round((self.batting_avg() * 0.6) + (self.strike_rate() * 0.4), 2)

class Bowler(Player):
    def __init__(self, name, role, team, runs, balls_faced, wickets, overs_bowled, runs_conceded, matches, outs):
        super().__init__(name, role, team, runs, balls_faced, wickets, overs_bowled, runs_conceded, matches, outs)
    def economy_rate(self):
        if(self.overs_bowled == 0):
            return 0.0
        return round((self.runs_conceded / self.overs_bowled),2)
    def performance_rating(self):
        return round((self.wickets * 3) - (self.economy_rate() * 5),2)

class AllRounder(Player):
    def __init__(self, name, role, team, runs, balls_faced, wickets, overs_bowled, runs_conceded, matches, outs):
        super().__init__(name, role, team, runs, balls_faced, wickets, overs_bowled, runs_conceded, matches, outs)
    def economy_rate(self):
        if(self.overs_bowled == 0):
            return 0.0
        return round((self.runs_conceded / self.overs_bowled),2)
    def performance_rating(self):
        return max (round((self.wickets * 2.5) - (self.economy_rate() * 4),2), round((self.batting_avg() * 0.5) + (self.strike_rate() * 0.3),2))