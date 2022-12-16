# Parse Input
commands = []
with open('input/day7_1.txt') as f:
    lines = f.readlines()
for line in lines:
    commands.append(line.split());

MAX_DIR_SIZE = 100000

# Solve Part 1
top_dir = {}
top_dir['top'] = True
top_dir['parent'] = top_dir
top_dir['size'] = 0
cur_dir = top_dir
# Format: dir['size'] = total file size for immediate dir
# Format: dir['parent'] = dir that represents the parent directory
# Format: dir['top'] = True if top, else False
# Format: dir[other char] = {another directory}
for command in commands:
    if command[1] == 'cd':
        if command[2] == '/':
            cur_dir = top_dir
        elif command[2] == '..':
            cur_dir = cur_dir['parent']
        else:
            if command[2] not in cur_dir:
                cur_dir[command[2]] = {}
                cur_dir[command[2]]['top'] = False
                cur_dir[command[2]]['parent'] = cur_dir
                cur_dir[command[2]]['size'] = 0
            cur_dir = cur_dir[command[2]]
    elif command[1] == 'ls':
        cur_dir['size'] = 0 # because we are about to reread the sizes
    elif command[0] != 'dir':
        cur_dir['size'] += int(command[0])

global_total = 0
def sum_directories(dir):
    global global_total
    total = 0
    for key in dir.keys():
        if key == 'size':
            total += dir[key]
        elif key == 'parent' or key == 'top':
            continue
        else:
            total += sum_directories(dir[key])
    if total < MAX_DIR_SIZE:
        global_total += total
    return total

sum_directories(top_dir)
print(global_total)

# Solve Part 2
def get_filesystem_size(dir):
    total = 0
    for key in dir.keys():
        if key == 'size':
            total += dir[key]
        elif key == 'parent' or key == 'top':
            continue
        else:
            total += get_filesystem_size(dir[key])
    return total
filesystem_size = get_filesystem_size(top_dir)
free_space = 70000000 - filesystem_size
extra_space_req = 30000000 - free_space
print('Total filesystem size: ' + str(filesystem_size))
print('Current free space: ' + str(free_space))
print('Need to free up at least ' + str(extra_space_req) + ' space')

min_dir_size = 70000000
def get_min_dir(dir):
    global min_dir_size
    global extra_space_req
    total = 0
    for key in dir.keys():
        if key == 'size':
            total += dir[key]
        elif key == 'parent' or key == 'top':
            continue
        else:
            total += get_min_dir(dir[key])
    if total >= extra_space_req and total < min_dir_size:
        min_dir_size = total
    return total

get_min_dir(top_dir)
print(min_dir_size)