# %%
## CTRL-Enter will run the cell
### REMEMBER to create a Virtual Environment
### py -3 -m venv .\azpyenv\    <-- Directory to build the VENV
### .\azpyenv\scripts\activate  <-- Activates the environment
import os
import random
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path


# %%
## Shift-Enter will create a new cell
## Class Definition using default args
class Dice:
    def roll(self, low=1, high=6):
        die1 = random.randint(int(low), int(high))
        die2 = random.randint(int(low), int(high))
        return die1, die2


myDice = Dice()
print(f"Dice roll {myDice.roll()}")
print(f"On a d20 {myDice.roll(1, 20)}")


# %%
## File / IO example
path = Path("..\working")
print(path.exists())
for file in path.glob('*.*'):
    print(file)

# %%
## Loops for, while, if else
a, b = 3, 5
c = a
if a == b:
    pass
elif a == c:
    print("a = c")
else:
    print("wrong")

print(f"a: {a} b: {b} c:{c}")

## List - use
letters = [a, b, c]
## List supports append, insert, extend(add any iterable), sor 
for letter in letters:
    print(f"Letter: {letter}")

for nums in range(len(letters)):
    print(letters[nums])
else:
    print("Loop complete")

i = 0
while letters[i] != 5:
    print(f"Letters in while: {letters[i]}")
    if letters[i] == 3:
        break
    i += 1

## Tuple are immutable
## Has count and index functions
fruit = ("apple", "pear", "banana")
print(f"Tuple: {fruit}")

## Set - unordered, unindexed, and immutable NO Duplicates
## Has add, update, discard, clear, remove,  and subset / intersect functions
sports = {"baseball", "basketball", "football", "baseball"}
print(sports) #prints Baseball 1 time


## Dictionary - Ordered, change, add, remove NO Duplicates
## Has get, keys, remove etc.
car = {
    "brand": "Chrysler",
    "model": "Jeep",
    "year":  1982
}
print(f"Year: {car['year']}")

# %%
a = 9
b = 0 
try:
    print(f"a / b = {a / b}")
except ZeroDivisionError:
    print("Can't divide by zero")
except:
    print("Other error")
finally:
    print("Calc complete.")

val1 = os.cpu_count
txt = "CPU Count: {}"
print(txt.format(val1))
    # Also can use Raise with an error type

# %%
# Using Matplotlib
xpoints = np.array([0,6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()

# %%
import threading
import time

def delayer(caller):
    for i in range(5):
        print(f"Caller {caller} Counter {i}")
        time.sleep(2)
    
t1 = threading.Thread(target=delayer("t1"))
t2 = threading.Thread(target=delayer("t2"))

t1.daemon = False
t2.daemon = False

t1.start()
t2.start()

