# Parse Input
input = []
with open('input/day9.txt') as f:
    lines = f.readlines()
for line in lines:
    line_split = line.split()
    input.append((line_split[0], int(line_split[1])))

# Solve Part 1
states = set()
def update_tail_loc(t_loc, h_loc):
    global states
    if abs(t_loc[0] - h_loc[0]) == 2:
        t_loc[0] = int((t_loc[0] + h_loc[0]) / 2)
        t_loc[1] = h_loc[1]
    elif abs(t_loc[1] - h_loc[1]) == 2:
        t_loc[1] = int((t_loc[1] + h_loc[1]) / 2)
        t_loc[0] = h_loc[0]
    states.add(tuple(t_loc))
def update_head_loc(t_loc, h_loc, direction, distance):
    for i in range(distance):
        if direction == 'U':
            h_loc[0] += 1
        elif direction == 'D':
            h_loc[0] -= 1
        elif direction == 'L':
            h_loc[1] -= 1
        elif direction == 'R':
            h_loc[1] += 1
        update_tail_loc(t_loc, h_loc)
T_loc = [0,0]
H_loc = [0,0]
states.add(tuple([0,0]))
for move in input:
    direction = move[0]
    distance = move[1]
    update_head_loc(T_loc, H_loc, direction, distance)
print(len(states))

# Solve Part 2
states = set()
def update_tail_loc(t_loc, h_loc, is_final):
    global states
    if abs(t_loc[0] - h_loc[0]) == 2 and abs(t_loc[1] - h_loc[1]) == 2:
        t_loc[0] = int((t_loc[0] + h_loc[0]) / 2)
        t_loc[1] = int((t_loc[1] + h_loc[1]) / 2)
    elif abs(t_loc[0] - h_loc[0]) == 2:
        t_loc[0] = int((t_loc[0] + h_loc[0]) / 2)
        t_loc[1] = h_loc[1]
    elif abs(t_loc[1] - h_loc[1]) == 2:
        t_loc[1] = int((t_loc[1] + h_loc[1]) / 2)
        t_loc[0] = h_loc[0]
    if is_final: # only save location for 9th piece of tail
        states.add(tuple(t_loc))
def coordinate_tail_update(t_loc, h_loc):
    update_tail_loc(t_loc[0], h_loc, False)
    for i in range(1, len(t_loc)):
        update_tail_loc(t_loc[i], t_loc[i-1], i == len(t_loc) - 1)
def update_head_loc(t_loc, h_loc, direction, distance):
    for i in range(distance):
        if direction == 'U':
            h_loc[0] += 1
        elif direction == 'D':
            h_loc[0] -= 1
        elif direction == 'L':
            h_loc[1] -= 1
        elif direction == 'R':
            h_loc[1] += 1
        coordinate_tail_update(t_loc, h_loc)
T_loc = [[0,0] for _ in range(9)]
H_loc = [0,0]
states.add(tuple([0,0]))
for move in input:
    direction = move[0]
    distance = move[1]
    update_head_loc(T_loc, H_loc, direction, distance)
print(len(states))