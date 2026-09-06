# ============================================================
# 📘 PYTHON LEARNING SCRIPT — COMBINED Q&A + CODE EXAMPLES
# ============================================================
import numpy as np
import subprocess
# Clear screen on Windows
subprocess.run("cls", shell=True)

# ============================================================
# 📌 Lists — Q&A
# ============================================================

# Q1: How do you create a list?
my_list = [1, 2, 3, 4, 5, 6, 7, 9, 10]

# Q2: How do you add an item to a list?
my_list.append(4)

# Q3: How do you access list items?
first_item = my_list[0]
print(my_list)
print(my_list[-5:-1])

# ============================================================
# 📌 Tuples — Q&A
# ============================================================

# Q1: How do you create a tuple?
my_tuple = (10, 20, 30)

# Q2: Can you modify a tuple?
# No — tuples are immutable.

# Q3: How do you access tuple items?
second_item = my_tuple[1]


# ============================================================
# 📌 Sets — Q&A
# ============================================================

# Q1: How do you create a set?
my_set = {1, 2, 3}

# Q2: Do sets allow duplicates?
# No — duplicates are removed automatically.

# Q3: How do you add an item?
my_set.add(4)


# ============================================================
# 📌 Dictionaries — Q&A
# ============================================================

# Q1: How do you create a dictionary?
person = {"name": "Aditya", "city": "Plano"}

# Q2: How do you access a value?
name_value = person["name"]

# Q3: How do you add/update a key?
person["age"] = 30


# ============================================================
# 📌 Functions — Q&A
# ============================================================

# Q1: How do you define a function?
def greet():
    print("Hello, Aditya!")

# Q2: How do you pass arguments?
def add(a, b):
    return a + b

# Q3: What is a return value?
# The value a function gives back using 'return'.


# ============================================================
# 📌 For Loop — Q&A
# ============================================================

# Q1: Loop through a list
for item in [100, 200, 300]:
    print("Item:", item)

# Q2: Loop with range
for i in range(5):
    print("Index:", i)


# ============================================================
# 📌 Break Statement
# ============================================================

for num in range(10):
    if num == 5:
        break   # stops the loop
    print("Break example:", num)


# ============================================================
# 📌 Continue Statement
# ============================================================

for num in range(10):
    if num == 5:
        continue   # skips this iteration
    print("Continue example:", num)

# ============================================================
# 📌 Enumerate Statement
# ============================================================
'''
list1 = [10,20,30,45,56,67]
for index, value in enumerate(list1):
    print(index, value)

s = "Interview"
for i,j in enumerate(s):
    print(i, j)
'''
