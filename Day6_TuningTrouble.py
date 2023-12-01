from aoc_helper import open_input

# --- Day 6: Tuning Trouble ---
# Create list form input
input_list = open_input('AC6_Input.txt')
split_list = [i for i in input_list[0]]


def question1(list):
    value = 0
    for i in range(len(list) - 3):
        start = list[i:i + 4]
        start_set = set(start)
        if len(start) == len(start_set):
            value = i + 4
            return value
    return value


def question2(list):
    value = 0
    for i in range(len(list) - 13):
        start = list[i:i + 14]
        start_set = set(start)
        if len(start) == len(start_set):
            value = i + 14
            return value
    return value


print("Question 1: How many characters need to be processed before the first start-of-packet marker is detected?")
print(question1(split_list))

print("Question 2: How many characters need to be processed before the first start-of-packet marker is detected?")
print(question2(split_list))
