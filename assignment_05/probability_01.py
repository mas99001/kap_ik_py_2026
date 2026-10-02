import subprocess as sb
sb.run("cls", shell=True)
#Import the required modules
import math
# Parameters
lambda_ = 5  # Average number of calls per hour
k = 3  # Number of calls we are interested in

# Probability of exactly 3 calls in the next hour
prob_3_calls = math.exp(0-lambda_)*lambda_**k / math.factorial(k)

# Plot the PMF
# Hint: Use poisson.pmf()


# Plot the CDF
# Hint: Use poisson.cdf()


# Print resultant probability
print(f"Probability of exactly 3 calls in the next hour: {prob_3_calls:.4f}")

# Parameters
n = 10  # Number of trials (visitors)
p = 0.1  # Probability of success (visitor making a purchase)
k = 2  # Number of successes we are interested in

# Probability of exactly 2 visitors making a purchase
prob_2_purchases = math.comb(10, 2) * (p**2) * ((1 - p)**8)

# Plot the PMF
# Hint: Use binom.pmf()


# Plot the CDF
# Hint: Use binom.cdf()


# Print the resultant probability
print(f"Probability of exactly 2 visitors making a purchase: {prob_2_purchases:.4f}")

# Parameters
n = 8  # Number of trials (students)
p = 0.7  # Probability of success (student passing the exam)
k = 5  # Minimum number of successes we are interested in

# Probability of at least 5 students passing the exam
p5 = math.comb(8, 5) * (p**5) * ((1 - p)**3)
p6 = math.comb(8, 6) * (p**6) * ((1 - p)**2)
p7 = math.comb(8, 7) * (p**7) * ((1 - p)**1)
p8 = math.comb(8, 8) * (p**8) * ((1 - p)**0)

prob_at_least_5_pass = p5 + p6 +p7 +p8

# Plot the PMF
# Hint: Use binom.pmf()


# Plot the CDF
# Hint: Use binom.cdf()


# Print the resultant probability
print(f"Probability of at least 5 students passing the exam: {prob_at_least_5_pass:.4f}")