# Notebook 3 — Data Analysis with Python
# https://python-lesson3.interviewkickstart.com/

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import subprocess
# Clear screen on Windows
subprocess.run("cls", shell=True)
# Consistent colours we'll use across all charts
BLUE   = "#4C72B0"
ORANGE = "#DD8452"
GREEN  = "#55A868"
RED    = "#C44E52"

# Cleaner chart style
plt.rcParams.update({"figure.dpi": 110, "axes.spines.top": False,
                     "axes.spines.right": False, "font.size": 10})
sns.set_theme(style="whitegrid", palette="muted")

def check(condition, ok="✅ Correct!", fail="❌ Not quite — re-read the step above."):
    print(ok if condition else fail)

np.random.seed(42)
print("Setup complete. Ready to go.")

# Messy names as they arrived from the registration form
raw_names = ["  arjun kumar  ", "PRIYA SHARMA", " ravi  ", "sneha PATEL", "  dev  "]

# The long way — 4 lines of code:
# clean = []
# for name in raw_names:
#     clean.append(name.strip().title())

# The Python way — 1 line that reads like English:
# [do_this  for each item  in  the_list]
clean_names = sorted([name.strip().title() for name in raw_names])

print(clean_names)
# strip()  → removes spaces at start and end
# title()  → capitalises First Letter Of Each Word

# Scores from the CSV — they're ALL strings, not numbers!
raw_scores = ["82", "91", "67", "45", "88", "34", "72"]

# ✏️ YOUR TURN
# Convert each string to an integer using a list comprehension
# Hint: int("82") → 82
scores = [int(x) for x in raw_scores]

print("Scores:", scores)
print("Type: ", type(scores[0]))  # should print <class 'int'>

scoref = [int(x) for x in raw_scores if int(x)<60]

print("Scoref:", scoref)
print("Type: ", type(scoref[0]))  # should print <class 'int'>

scoresi = [82, 91, 67, 45, 88, 34, 72]

# ✏️ YOUR TURN
# Get only scores between 50 and 80 (inclusive)
# Hint: use TWO conditions joined by 'and'
mid_scores = [s for s in scoresi if s>=50 and s<=80]

print("Mid-range scores:", mid_scores)

students = ["Arjun", "Priya", "Ravi", "Sneha"]
scores_2 = [82,      95,      67,     88]

# zip() locks two lists together like a zipper
# Each iteration gives you ONE item from each list — in sync
for student, score in zip(students, scores_2):
    result = "Pass" if score >= 40 else "Fail"
    print(f"  {student}: {score} → {result}")

# Without zip you'd need scores_2[i] inside range(len(...)) — messy!

students = ["Arjun", "Priya", "Ravi", "Sneha"]

# enumerate() gives you BOTH the position (rank) and the value
# start=1 → count from 1 instead of 0
print("Class rankings:")
for rank, student in enumerate(students, start=1):
    print(f"  {rank}. {student}")

# Old way:  for i in range(len(students)):  students[i]   ← ugly
# Python way: for rank, student in enumerate(...) ← clean

attendance = [91, 85, 78, 62, 95, 88]

# all() → True only if EVERY value passes the condition
print(all(a >= 60 for a in attendance))   # Is every student above 60%?

# any() → True if AT LEAST ONE value passes the condition
print(any(a < 75  for a in attendance))   # Is anyone below 75%?

# These scan the entire list in one call — no loop needed
# Power: works the same whether the list has 6 or 60,000 values

marks = [55, 72, 48, 89, 61, 77, 43]

# ✏️ YOUR TURN

# 1. Are ALL marks above 40? (i.e. everyone passed?)
all_passing = all(m > 40 for m in marks)

# 2. Is ANYONE scoring above 85?
has_top = any(m > 85 for m in marks)

print("All passing:  ", all_passing)
print("Has top scorer:", has_top)

students_data = [
    {"name": "Arjun", "score": 82},
    {"name": "Priya", "score": 95},
    {"name": "Ravi",  "score": 67},
    {"name": "Sneha", "score": 88},
]
# ==================================
# 1.5 — Sorted with a Key
# ==================================
# sorted() creates a NEW sorted list — doesn't change the original
# key= tells Python WHAT to sort by
# lambda s: s["score"]  →  "sort by the 'score' value in each dict"
# reverse=True          →  highest first
ranked = sorted(students_data, key=lambda s: s["score"], reverse=True)

for i, s in enumerate(ranked, start=1):
    print(f"  #{i}  {s['name']:8s}  {s['score']}")

# ==================================
#✏️ Exercise 1 — Put it all together
# ==================================
class_list = [
    ("  arjun  ", "82"), ("PRIYA", "95"), ("ravi kumar", "67"),
    ("Sneha", "88"),     ("  dev", "45"), ("Meena", "72"),
]
# Each tuple: (raw_name, score_as_string)

# ✏️ YOUR TURN

# 1. Clean names using a comprehension
#    Unpack each tuple: name, _ = ("  arjun  ", "82")
names_clean  = [name.strip().title() for name, marks in class_list]

# 2. Convert scores to int using a comprehension
scores_clean = [int(score) for name, score in class_list]

# 3. Names of students who scored >= 80
top_students = [name for name, score in zip(names_clean, scores_clean) if int(score)>=80]

# 4. Average score — sum all and divide by count
avg = round(sum(scores_clean) /len(scores_clean) , 1)

print("Clean names:  ", names_clean)
print("Top students: ", top_students)
print("Class average:", avg)