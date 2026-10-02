import subprocess as sb
import random

sb.run("cls", shell=True)
print("----------------------------------------")
print("Welcome to the Probability Assignment 05")

def coin_toss():
    if(random.randint(0, 1) == 0):
        return(1) #"Heads"
    else:
        return(0) #"Tails"

def coin_trial():
    heads = 0
    for i in range(100):
        if(coin_toss() == 1):
            heads += 1
    return heads

def simulate_coin_trials(num_trials):
    results = []
    for _ in range(num_trials):
        heads = coin_trial()
        results.append(heads)
    average_heads = sum(results)/num_trials
    return (average_heads) #Return the average number of heads obtained in the trials

print("\n--------------- Coin Toss --------------")
print("Testing coin_toss function:")
for i in range(5):
    print(f"Test {i+1}: {'head' if coin_toss() == 1 else 'tail'}")

print("\n--------------- Coin Trial --------------")
print("Testing coin_trial function:")
print("Number of heads in a trial of 100 flips:", coin_trial())

print("\n--------- Simulate Coin Trials ----------")
print("Testing simulate_coin_trials function:")
print("Average number-of-heads-out-of-100 flips in a simulation of 1000 trials:", simulate_coin_trials(1000))

# Betting offer: If you bet on heads, you will win $100 for each head and lose $10 for each tail. 
# Once you get a head and win $100, you will stop flipping the coin. If you get a tail, you will lose $10 and continue flipping until you get a head.
# One Trial ends when head is obtained. At this moment the player to choose to continue next trial or stop playing. 
# If the player chooses to continue, the next trial starts with a new series of coin tosses.

def simulate(n, receive, give):
    total_earnings = 0
    for _ in range(n):
        result = []
        print(f'Trial {_+1}')
        earnings = 0
        while True:
            if coin_toss() == 1:  # Head
                result.append('H')
                earnings += receive
                break
            else:  # Tail
                result.append('T')
                earnings -= give
        print(result)
        total_earnings += earnings
    return total_earnings

print("\n--------- Simulate Betting ----------")
# Example usage:
# profit = simulate(1, 15, 10)
# print(f"Profit after one simulation: ${profit}")
profit = simulate(10, 10, 10)
print(f"Profit after TEN simulations: ${profit}")