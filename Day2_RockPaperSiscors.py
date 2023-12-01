from aoc_helper import open_input

# --- Day 2: Rock Paper Siscors ---
# Create list form input
input_list = open_input('AC2_Input.txt')

split_list = [i.split(' ') for i in input_list]


def question1(list):
    total = 0
    for i in range(len(split_list)):
        if split_list[i][1] == 'X':
            total += 1
        elif split_list[i][1] == 'Y':
            total += 2
        elif split_list[i][1] == 'Z':
            total += 3

        if (split_list[i][0] == 'A' and split_list[i][1] == 'Y') | (
                split_list[i][0] == 'B' and split_list[i][1] == 'Z') | (
                split_list[i][0] == 'C' and split_list[i][1] == 'X'):
            total += 6
        elif (split_list[i][0] == 'A' and split_list[i][1] == 'X') | (
                split_list[i][0] == 'B' and split_list[i][1] == 'Y') | (
                split_list[i][0] == 'C' and split_list[i][1] == 'Z'):
            total += 3
    return total


def question2(list):
    total = 0
    for i in range(len(split_list)):
        if split_list[i][1] == 'X':
            if split_list[i][0] == 'A':
                split_list[i][1] = 'Z'
            elif split_list[i][0] == 'B':
                split_list[i][1] = 'X'
            else:
                split_list[i][1] = 'Y'
        elif split_list[i][1] == 'Y':
            if split_list[i][0] == 'A':
                split_list[i][1] = 'X'
            elif split_list[i][0] == 'B':
                split_list[i][1] = 'Y'
            else:
                split_list[i][1] = 'Z'
        elif split_list[i][1] == 'Z':
            if split_list[i][0] == 'A':
                split_list[i][1] = 'Y'
            elif split_list[i][0] == 'B':
                split_list[i][1] = 'Z'
            else:
                split_list[i][1] = 'X'
    total = question1(list)
    return total


print("What would your total score be if everything goes exactly according to your strategy guide?")
print(question1(split_list))

print(
    "Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?")
print(question2(split_list))
