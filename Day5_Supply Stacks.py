import re

# --- Day 5: Supply Stacks ---
# Create list form input
stacks = []
with open('AC5_Input.txt') as file:
    input = file.readlines()
    for col in range(0, len(input[0])):
        stacks.append("")
        for line in range(0, 8):
            if input[line][col] not in ["[", "]", " "]:
                stacks[col] += input[line][col]

# remove empty lists and list of trailing newlines
stacks = [stack for stack in stacks if stack != ''][:-1]
# remove stack diagram from input, reduce to only integers
# instructions are now [Digit, Digit, Digit]: move n from x1 to x2
input = [[int(d) for d in re.findall(r"\d+", line.strip())] for line in input[10:]]


def question1(stack_list, input_list):
    for i in range(len(input_list)):
        for j in range(input_list[i][0]):
            stack_list[input_list[i][2] - 1] = stack_list[input_list[i][1] - 1][0] + stack_list[input_list[i][2] - 1]
            stack_list[input_list[i][1] - 1] = stack_list[input_list[i][1] - 1][1:]
    last = ''
    for i in range(len(stack_list)):
        last += stack_list[i][0]
    return last


def question2(stack_list, input_list):
    print(stack_list)
    for i in range(len(input_list)):
        print(stack_list)
        stack_list[input_list[i][2] - 1] = stack_list[input_list[i][1] - 1][0:input_list[i][0]] + stack_list[
            input_list[i][2] - 1]
        stack_list[input_list[i][1] - 1] = stack_list[input_list[i][1] - 1][input[i][0]:]
        print(stack_list)
    last = ''
    for i in range(len(stack_list)):
        if len(stack_list[i]) != 0:
            last += stack_list[i][0]
        else:
            last += ' '
    return last


print("After the rearrangement procedure completes, what crate ends up on top of each stack?")
print(question2(stacks, input))
