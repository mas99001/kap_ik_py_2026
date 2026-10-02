import subprocess as sb
import random
sb.run('cls', shell=True)
print('Demonstation of a Casino')
def simulate_casino_games(num_games, fee_per_game):
    total_profit = 0 #This is for the casino for the day
    win_amount = 10#0

    for _ in range(num_games):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        if((die1 == 6) and (die2 == 6)):
            print(f'{_+1}th PLAYER: HURRAY')
            total_profit -= (win_amount - fee_per_game)
        else:
            total_profit += fee_per_game
        #if((_ % 100) == 0):
            #print(f'TOTAL PROFIT at GAME {_+1} {total_profit:.2f}')
    return total_profit
    #average_profit = total_profit / num_games
    #return average_profit

num_games = 10000 #1000000  # Number of games to simulate
fee_per_game = 0.5  # Casino fee per game in dollars

# Running the simulation
total_profit = simulate_casino_games(num_games, fee_per_game)
average_profit = total_profit / num_games
# Print the average profit per game
print(f"Total profit: ${total_profit:.2f}")
print(f"Average profit per game: ${average_profit:.2f}")