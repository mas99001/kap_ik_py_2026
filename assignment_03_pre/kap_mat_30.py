import subprocess as sb
sb.run("cls", shell=True)

'''
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
revenue = [2400, 3000, 2700, 3500, 4100]

plt.figure(figsize=(12, 6))
plt.plot(months, revenue, marker="o", color="#0f766e", linewidth=2)
plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue (USD)")
plt.grid(alpha=0.4)
plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt

cities = ["Mumbai", "Delhi", "Bangalore", "Chennai"]
revenue = [5400, 4050, 7600, 4550]

plt.figure(figsize=(6, 3.5))
plt.bar(cities, revenue, color=["#0f766e", "#14b8a6", "#2dd4bf", "#5eead4"])
plt.title("Revenue by City")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()


import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(42)
print("rng:\n", rng)
units   = rng.integers(50, 400, 40)
print("units:\n", units)
revenue = units * rng.uniform(15, 25, 40)
print("revenue:\n", revenue)

plt.figure(figsize=(6, 3.5))
plt.scatter(units, revenue, color="#0f766e", alpha=0.7)
plt.title("Units sold vs Revenue")
plt.xlabel("Units")
plt.ylabel("Revenue")
plt.grid(alpha=0.3)
plt.tight_layout()

import matplotlib.pyplot as plt
import numpy as np

scores = np.random.default_rng(0).normal(75, 12, 500)
print("scores:\n", scores)
plt.figure(figsize=(6, 3.5))
plt.hist(scores, bins=20, color="#14b8a6", edgecolor="white")
plt.title("Score distribution")
plt.xlabel("Score")
plt.ylabel("Count")
plt.tight_layout()
'''

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

fig, ax = plt.subplots(2, 2, figsize=(7, 4.5))
ax[0, 0].plot(x, np.sin(x), color="#0f766e");   ax[0, 0].set_title("sin")
ax[0, 1].plot(x, np.cos(x), color="#14b8a6");   ax[0, 1].set_title("cos")
ax[1, 0].plot(x, x**2,      color="#2dd4bf");   ax[1, 0].set_title("x²")
ax[1, 1].plot(x, np.log(x+1), color="#5eead4"); ax[1, 1].set_title("log")
plt.tight_layout()
plt.show()
