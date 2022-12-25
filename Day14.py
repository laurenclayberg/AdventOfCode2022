def get_range(start, end):
    min_x = min(start[0], end[0])
    max_x = max(start[0], end[0])
    min_y = min(start[1], end[1])
    max_y = max(start[1], end[1])
    return min_x, max_x, min_y, max_y

blocked_1 = set()
blocked_2 = set()
overall_max_y = 0
with open('input/day14.txt') as f:
    lines = f.readlines()
for line in lines:
    line_split = line.strip().split(" -> ")
    for i in range(len(line_split) - 1):
        start = line_split[i]
        end = line_split[i+1]
        min_x, max_x, min_y, max_y = get_range(eval(start), eval(end))
        overall_max_y = max(max_y, overall_max_y)
        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                blocked_1.add((x,y))
                blocked_2.add((x,y))

# Part 1 solution
sand_past_end = False
sand_count = 0
while sand_past_end == False:
    sand = (500,0)
    sand_is_blocked = False
    while sand_is_blocked == False:
        if (sand[1] > overall_max_y):
            sand_past_end = True
            break
        elif (sand[0], sand[1]+1) not in blocked_1:
            sand = (sand[0], sand[1]+1)
        elif (sand[0]-1, sand[1]+1) not in blocked_1:
            sand = (sand[0]-1, sand[1]+1)
        elif (sand[0]+1, sand[1]+1) not in blocked_1:
            sand = (sand[0]+1, sand[1]+1)
        else:
            sand_is_blocked = True
            sand_count += 1
            blocked_1.add(sand)
            break
print(sand_count)

# Part 2 solution
sand_count = 0
floor = overall_max_y + 2
while True:
    sand = (500,0)
    sand_is_blocked = False
    while sand_is_blocked == False:
        if (sand[1] == floor - 1): # check hit the floor
            sand_is_blocked = True
            sand_count += 1
            blocked_2.add(sand)
        elif (sand[0], sand[1]+1) not in blocked_2:
            sand = (sand[0], sand[1]+1)
        elif (sand[0]-1, sand[1]+1) not in blocked_2:
            sand = (sand[0]-1, sand[1]+1)
        elif (sand[0]+1, sand[1]+1) not in blocked_2:
            sand = (sand[0]+1, sand[1]+1)
        else:
            sand_is_blocked = True
            sand_count += 1
            blocked_2.add(sand)
    if sand_is_blocked and sand[0] == 500 and sand[1] == 0:
        break
print(sand_count)