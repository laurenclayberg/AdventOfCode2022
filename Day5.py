# Parse Input
stacks_input = []
instructions = [] # number, from, to
with open('input/day5_1.txt') as f:
    lines = f.readlines()
parse_stacks = True
for line in lines:
    if parse_stacks:
        if line == '\n':
            parse_stacks = False
            continue
    if parse_stacks:
        stack_line = []
        for l in range(1, len(line), 4):
            letter = line[l]
            stack_line.append(letter)
        stacks_input.append(stack_line)
    else:
        line_split = line.split()
        instructions.append([int(line_split[1]), int(line_split[3])-1, int(line_split[5])-1])

# Clean up the stacks
stacks = [[] for _ in range(len(stacks_input[0]))]
for i in range(len(stacks_input)-2, -1, -1):
    for j in range(len(stacks_input[i])):
        stack = stacks[j]
        letter = stacks_input[i][j]
        if letter != ' ':
            stack.append(letter)

# Solve part 1
for move in instructions:
    stack_from = stacks[move[1]]
    stack_to = stacks[move[2]]
    items_to_move = move[0]

    new_stack_from = stack_from[0:len(stack_from) - items_to_move]
    new_stack_to = stack_from[len(stack_from) - items_to_move:]
    new_stack_to.reverse()
    stack_to.extend(new_stack_to)
    stacks[move[1]] = new_stack_from
    stacks[move[2]] = stack_to

answer = ''
for stack in stacks:
    answer += stack.pop()
print(answer)

# Solve part 2
# remake the stacks
stacks = [[] for _ in range(len(stacks_input[0]))]
for i in range(len(stacks_input)-2, -1, -1):
    for j in range(len(stacks_input[i])):
        stack = stacks[j]
        letter = stacks_input[i][j]
        if letter != ' ':
            stack.append(letter)
# don't reverse this time
for move in instructions:
    stack_from = stacks[move[1]]
    stack_to = stacks[move[2]]
    items_to_move = move[0]

    new_stack_from = stack_from[0:len(stack_from) - items_to_move]
    stack_to.extend(stack_from[len(stack_from) - items_to_move:])
    stacks[move[1]] = new_stack_from
    stacks[move[2]] = stack_to

answer = ''
for stack in stacks:
    answer += stack.pop()
print(answer)