from aoc_helper import open_input
import string

# --- Day 3: Rucksack Reorganization ---
# Create list form input
input_list = open_input('AC3_Input.txt')

# Create a list with values of letters
values = dict()
for index, letter, in enumerate(string.ascii_letters):
    values[letter] = index + 1


def question1(list):
    letters = []
    for i in range(len(list)):
        first, second = list[i][:len(list[i]) // 2], list[i][len(list[i]) // 2:]
        letters.append(set(first).intersection(second))
    total = 0
    for i in range(len(letters)):
        s = ''.join(letters[i])
        total += values[s]
    return total


def question2(list):
    letters = []
    for i in range(0, len(list) - 2, 3):
        letters.append(set(list[i]) & set(list[i + 1]) & set(list[i + 2]))
    total = 0
    for i in range(len(letters)):
        s = ''.join(letters[i])
        total += values[s]
    return total


print("Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?")
print(question1(input_list))

print("Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?")
print(question2(input_list))
