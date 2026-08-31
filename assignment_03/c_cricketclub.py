import csv
#
# Exceptions
#   
class InvalidDeliveryError(Exception):
    def __init__(self, *args):
        super().__init__(*args)
        self.message = args[0]
class InvalidOversError(Exception):
    def __init__(self, *args):
        super().__init__(*args)
        self.message = args[0]
#
# Cricket Club
#   
class CricketClub:
    def __init__(self):
        pass
    # Save players to csv
    def save_players_csv(self, players, filename):
        try:
            with open(filename, "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=players[0].keys(), extrasaction="ignore")
                writer.writeheader()
                writer.writerows(players)
        except:
            print("Some error inside save_players_csv()")
        finally:
            print("I am done with save_players_csv()")
    # Load players from csv
    def load_players_csv(self, filename):
        result = []
        try:
            with open(filename, "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    next_item = {}
                    next_item["name"] = row["name"]
                    next_item["role"] = row["role"]
                    next_item["team"] = row["team"]
                    next_item["runs"] = int(row["runs"])
                    next_item["balls_faced"] = int(row["balls_faced"])
                    next_item["wickets"] = int(row["wickets"])
                    next_item["overs_bowled"] = int(row["overs_bowled"])
                    next_item["runs_conceded"] = int(row["runs_conceded"])
                    next_item["matches"] = int(row["matches"])
                    next_item["outs"] = int(row["outs"])
                    result.append(next_item)
        except:
            print("Some error inside load_players_csv()")
        finally:
            print("I am done with load_players_csv()")
        return result
    def calculate_strike_rate(self, runs, balls_faced):
        if(balls_faced == 0):
            return 0.0
        elif(runs < 0):
            raise ValueError("Runs cannot be negative")
        else:
            return round((float(runs)/float(balls_faced))*(100.0),1)
    def validate_delivery(self, runs_scored):
        if runs_scored in range(0,8):
            return True
        else:
            raise InvalidDeliveryError("Runs are not valid")
    def safe_score_ball(self, runs_scored):
        try:
            if(self.validate_delivery(runs_scored)):
                return runs_scored
        except:
            return -1
        