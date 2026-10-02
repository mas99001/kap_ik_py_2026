import subprocess as sb
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli, binom, poisson, randint

sb.run('cls', shell=True)
# Case 1: Bernoulli Distribution
# Scenario: Patient appointment no-show rates (show=1, no-show=0)
p_bernoulli = 0.8  # Probability of showing up
## Generate 1000 random samples of patient show-up (1) or no-show (0) with a 80% show-up probability.
bernoulli_trials = bernoulli.rvs(p_bernoulli, size=1000) 

# Plot Bernoulli distribution
plt.figure(figsize=(8, 6))
plt.hist(bernoulli_trials, bins=2, density=True, alpha=0.6, color='g', edgecolor='black')
plt.title('Bernoulli Distribution (p=0.8)')
plt.xlabel('Outcome')
plt.ylabel('Probability Density')
plt.xticks([0, 1])
plt.show()
# Additional Analysis and Summary
print(f"Bernoulli Distribution: p={p_bernoulli}")
print(f"Mean of Bernoulli trials: {np.mean(bernoulli_trials)}")

print(bernoulli_trials)


# Case 2: Binomial Distribution
# Scenario: Number of successful surgeries out of 20 operations
n_binom = 20  # Number of trials (operations)
p_binom = 0.95  # Probability of success (successful surgery)
# Generate 1000 random samples representing the number of successful surgeries out of n_binom operations with a success probability of p_binom.
binom_trials = binom.rvs(n_binom, p_binom, size=1000) 
# Plot Binomial distribution
plt.figure(figsize=(8, 6))
plt.hist(binom_trials, bins=n_binom+1, density=True, alpha=0.6, color='b', edgecolor='black')
plt.title(f'Binomial Distribution (n={n_binom}, p={p_binom})')
plt.xlabel('Number of Successful Surgeries')
plt.ylabel('Probability Density')
plt.show()

# Additional Analysis and Summary
print(f"\nBinomial Distribution: n={n_binom}, p={p_binom}")
print(f"Mean of Binomial trials: {np.mean(binom_trials)}")

print(binom_trials)

# Case 3: Poisson Distribution
# Scenario: Number of emergency room visits per hour
lambda_poisson = 10  # Average rate of visits per hour
# Generate 1000 random samples representing the number of emergency room visits per hour with an average rate of lambda_poisson.
poisson_trials = poisson.rvs(lambda_poisson, size=1000) 
# Plot Poisson distribution
plt.figure(figsize=(8, 6))
plt.hist(poisson_trials, bins=max(poisson_trials)-min(poisson_trials), density=True, alpha=0.6, color='r', edgecolor='black')
plt.title(f'Poisson Distribution (λ={lambda_poisson})')
plt.xlabel('Number of Visits')
plt.ylabel('Probability')
plt.show()
# Additional Analysis and Summary
print(f"\nPoisson Distribution: λ={lambda_poisson}")
print(f"Mean of Poisson trials: {np.mean(poisson_trials)}")
print(poisson_trials)