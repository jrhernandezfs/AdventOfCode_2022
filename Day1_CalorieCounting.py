import pandas as pd

# --- Day 1: Calorie Counting ---
# Read xlsx of Elves
file = pd.read_excel('Input_AC1.xlsx', header=None)

# Group the Elves list
g = file[0].isna()
elves = file[~g].groupby(g.cumsum())[0].apply(list).tolist()

# Sort the Elves shopping list by sum
sortedElves = sorted(elves, key=sum)

# Answer 1: Highest sum:
print("Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?")
print(sum(sortedElves[len(sortedElves) - 1]))

# Answer 2: Total of three highest:
top3Total = sum(sortedElves[len(sortedElves) - 1]) + sum(sortedElves[len(sortedElves) - 2]) + sum(
    sortedElves[len(sortedElves) - 3])
print("Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?")
print(top3Total)
