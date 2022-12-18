# Parse Input
input = []
with open('input/day10.txt') as f:
    lines = f.readlines()
for line in lines:
    line_split = line.split()
    if line_split[0] == 'noop':
        input.append(['noop', None])
    else:
        input.append(['addx', int(line_split[1])])

# Solve Part 1
x = 1
instruction = 0
if input[instruction][0] == 'noop':
    cycles_until_update = 1
else:
    cycles_until_update = 2
answer = 0
answer2 = [['.' for _ in range(40)] for _ in range(6)]
for i in range(250):
    # execute cycle
    cycles_until_update -= 1
    i_x = int(i / 40)
    i_y = i % 40
    if i_y == x-1 or i_y == x or i_y == x+1:
        answer2[i_x][i_y] = '#'
    if i in [19,59,99,139,179,219]:
        print("Cycle: " + str(i+1) + " X: " + str(x) + " Strength: " + str((i+1) * x))
        answer += (i+1) * x
    # check if we need to act on the instruction
    if cycles_until_update == 0:
        if input[instruction][0] == 'addx':
            x += input[instruction][1]
        instruction += 1
        if instruction >= len(input):
            break
        if input[instruction][0] == 'noop':
            cycles_until_update = 1
        else:
            cycles_until_update = 2
print(answer)

for i in range(len(answer2)):
    row = ''
    for j in range(len(answer2[0])):
        row += answer2[i][j]
    print(row)
