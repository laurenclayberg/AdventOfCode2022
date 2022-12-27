with open('input/day17.txt') as f:
    lines = f.readlines()
moves = None
for line in lines:
    moves = list(line)

# ***************************** Solve Part 1 *****************************

def create_rock(current_height, rock_type):
    rock = []
    if rock_type == 0:
        rock.append((2, current_height+3))
        rock.append((3, current_height+3))
        rock.append((4, current_height+3))
        rock.append((5, current_height+3))
    elif rock_type == 1:
        rock.append((3, current_height+3))
        rock.append((2, current_height+4))
        rock.append((3, current_height+4))
        rock.append((4, current_height+4))
        rock.append((3, current_height+5))
    elif rock_type == 2:
        rock.append((2, current_height+3))
        rock.append((3, current_height+3))
        rock.append((4, current_height+3))
        rock.append((4, current_height+4))
        rock.append((4, current_height+5))
    elif rock_type == 3:
        rock.append((2, current_height+3))
        rock.append((2, current_height+4))
        rock.append((2, current_height+5))
        rock.append((2, current_height+6))
    elif rock_type == 4:
        rock.append((2, current_height+3))
        rock.append((3, current_height+3))
        rock.append((2, current_height+4))
        rock.append((3, current_height+4))
    return rock

def is_rock_config_valid(cur_rock, rock_locations):
    for coord in cur_rock:
        if coord[1] >= 0 and coord not in rock_locations and coord[0] < 7 and coord[0] >= 0:
            continue
        else:
            return False
    return True

def move_rock(cur_rock, rock_locations, move_index):
    ''' Returns cur_rock updated, rock locations and True/False if cur_rock settled
    '''
    next_rock = []
    for coord in cur_rock:
        if moves[move_index] == '<':
            next_rock.append((coord[0]-1, coord[1]))
        elif moves[move_index] == '>':
            next_rock.append((coord[0]+1, coord[1]))
    if is_rock_config_valid(next_rock, rock_locations):
        cur_rock = next_rock
    next_rock = []
    for coord in cur_rock:
        next_rock.append((coord[0], coord[1]-1))
    is_settled = False
    if is_rock_config_valid(next_rock, rock_locations):
        cur_rock = next_rock
    else: # rock has settled
        for coord in cur_rock:
            rock_locations.add(coord)
            is_settled = True
    return cur_rock, is_settled

def get_next_height(current_height, cur_rock):
    height = current_height
    for coord in cur_rock:
        height = max(height, coord[1]+1)
    return height

move_index = -1
current_height = 0
rock_locations = set()
for rock in range(2022):
    rock_type = (rock) % 5
    cur_rock = create_rock(current_height, rock_type)
    while True:
        move_index = (move_index + 1) % len(moves)
        cur_rock, is_settled = move_rock(cur_rock, rock_locations, move_index)
        if is_settled:
            current_height = get_next_height(current_height, cur_rock)
            break

print("Part 1:", current_height)

# for i in range(current_height, -1, -1):
#     row = ''
#     for j in range(7):
#         if (j,i) in rock_locations:
#             row += '#'
#         else:
#             row += '.'
#     print(row)

def get_current_state(rock_locations, current_height, move_idx, rock_type):
    rocks_on_level = []
    for i in range(7):
        if (i,current_height-1) in rock_locations:
            rocks_on_level.append(i)
    return (move_idx, rock_type, tuple(rocks_on_level))

answers = set()
for skip_states in range(5000):
    # print(skip_states)
    prev_states = {}
    move_index = -1
    current_height = 0
    rock_locations = set()
    num_rocks = 1000000000000
    offset_start = None
    offset_end = None
    offset_rock_start = None
    offset_rock_end = None
    skip_state = 0
    for rock in range(1000000000000):
        rock_type = (rock) % 5

        state = get_current_state(rock_locations, current_height, move_index, rock_type)
        if state in prev_states and skip_state == skip_states:
            offset_start = prev_states[state][0]
            offset_rock_start = prev_states[state][1]
            offset_end = current_height
            offset_rock_end = rock
            break # pause at current rock
        elif state in prev_states and skip_state != skip_states:
            skip_state += 1
            prev_states[state] = (current_height, rock)
        else:
            prev_states[state] = (current_height, rock)

        cur_rock = create_rock(current_height, rock_type)
        while True:
            move_index = (move_index + 1) % len(moves)
            cur_rock, is_settled = move_rock(cur_rock, rock_locations, move_index)
            if is_settled:
                current_height = get_next_height(current_height, cur_rock)
                break

    before_loop_height = offset_start
    loop_add = offset_end - offset_start
    loop_rocks = offset_rock_end - offset_rock_start
    num_loops = int((num_rocks - (offset_rock_start)) / loop_rocks)
    total_height_to_now = before_loop_height + (num_loops * loop_add)
    num_rocks_to_go = (num_rocks - (offset_rock_start)) % loop_rocks

    old_height = current_height
    for rock in range(offset_rock_end, offset_rock_end + num_rocks_to_go):
        rock_type = (rock) % 5
        cur_rock = create_rock(current_height, rock_type)
        while True:
            move_index = (move_index + 1) % len(moves)
            cur_rock, is_settled = move_rock(cur_rock, rock_locations, move_index)
            if is_settled:
                current_height = get_next_height(current_height, cur_rock)
                break
    if total_height_to_now + (current_height - old_height) not in answers:
        answers.add(total_height_to_now + (current_height - old_height))
        print(len(answers), answers)

    if len(answers) > 10:
        break
print("Part 2:", answers)
# Guessed
# 1551319648090, 1551319648091, 1555685131189, *1561739130391*
