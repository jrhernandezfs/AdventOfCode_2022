from aoc_helper import open_input

# --- Day 4: Camp Cleanup ---
# Create list form input
input_list = open_input('AC4_Input.txt')

split_list = [i.split(',') for i in input_list]
for i in range(len(split_list)):
    split_list[i][0] = split_list[i][0].split('-')
    split_list[i][1] = split_list[i][1].split('-')


def question1(list):
    count = 0
    for i in range(len(list)):
        if ((int(list[i][0][0]) <= int(list[i][1][0])) and (int(list[i][0][1]) >= int(list[i][1][1]))) or \
                ((int(list[i][1][0]) <= int(list[i][0][0])) and (int(list[i][1][1]) >= int(list[i][0][1]))):
            count += 1
    return count


def question2(list):
    count = 0
    for i in range(len(list)):
        x = range(int(list[i][0][0]), int(list[i][0][1]) + 1)
        y = range(int(list[i][1][0]), int(list[i][1][1]) + 1)
        xs = set(x)
        xs = xs.intersection(y)
        if len(xs) != 0:
            count += 1
    return count


print("In how many assignment pairs does one range fully contain the other?")
print(question1(split_list))

print("In how many assignment pairs do the ranges overlap?")
print(question2(split_list))
