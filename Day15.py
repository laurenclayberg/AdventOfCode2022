import re

pairs = []
beacons = set()
sensors = set()
with open('input/day15.txt') as f:
    lines = f.readlines()
for line in lines:
    line_split = line.strip().split()
    sensor_x = int(re.search(r'-?\d+', line_split[2])[0])
    sensor_y = int(re.search(r'-?\d+', line_split[3])[0])
    beacon_x = int(re.search(r'-?\d+', line_split[8])[0])
    beacon_y = int(re.search(r'-?\d+', line_split[9])[0])
    pairs.append(((sensor_x, sensor_y), (beacon_x, beacon_y)))
    beacons.add((beacon_x, beacon_y))
    sensors.add((sensor_x, sensor_y))

# Solve part 1
def manhattan_dist(coord_1, coord_2):
    dist = 0
    dist += abs(max(coord_1[0], coord_2[0]) - min(coord_1[0], coord_2[0]))
    dist += abs(max(coord_1[1], coord_2[1]) - min(coord_1[1], coord_2[1]))
    return dist
def is_pair_relevant(sensor, beacon, target_y):
    dist = manhattan_dist(sensor, beacon)
    if sensor[1] >= target_y and sensor[1] - dist <= target_y:
        return True
    elif sensor[1] <= target_y and sensor[1] + dist >= target_y:
        return True
    return False
def get_range_on_target_y(sensor, max_dist, target_y):
    # Note: this method gives an INCLUSIVE range
    max_horizontal_dist = max_dist - abs(target_y - sensor[1])
    return (sensor[0] - max_horizontal_dist, sensor[0] + max_horizontal_dist)
def condense_ranges(ranges):
    ranges_expand = []
    for r in ranges:
        ranges_expand.append((r[0], '0')) # 0 == '<'
        ranges_expand.append((r[1], '1')) # 1 == '>
    ranges_expand.sort()
    ranges_condensed = []
    count_open = 0
    cur_min = None
    for item in ranges_expand:
        if item[1] == '0': # '<'
            count_open += 1
            if cur_min == None:
                cur_min = item[0]
        elif item[1] == '1': # '>'
            count_open -= 1
        if count_open == 0:
            ranges_condensed.append((cur_min, item[0]))
            cur_min = None
    return ranges_condensed
def get_final_y_cover(minimal_ranges, beacons, target_y):
    relevant_beacons = set()
    for beacon in beacons:
        if beacon[1] == target_y:
            relevant_beacons.add(beacon[0])
    total_covered = 0
    for r in minimal_ranges:
        cur_covered = r[1] - r[0] + 1
        for b in relevant_beacons:
            if b >= r[0] and b <= r[1]:
                cur_covered -= 1
        total_covered += cur_covered
    return total_covered
def solve_y_covered(pairs, target_y):
    target_y_covered_ranges = []
    for pair in pairs:
        sensor = pair[0]
        beacon = pair[1]
        # Check if the sensor is relevant for this target y
        if is_pair_relevant(sensor, beacon, target_y) == False:
            continue
        # Find covered ranges
        target_y_covered_ranges.append(get_range_on_target_y(sensor, manhattan_dist(sensor, beacon), target_y))
    # Calculate covered ranges
    minimal_ranges = condense_ranges(target_y_covered_ranges)
    # Subtract out spots that are already beacons
    return get_final_y_cover(minimal_ranges, beacons, target_y)

print("Parts 1:", solve_y_covered(pairs, 2000000)) # 2000000 for my input, 10 for mini

# Solve part 2
# For this problem, don't subtract out the original beacons
# max coord values are for both x and y
max_beacon_coord = 4000000 # 20 for mini, 4000000 for my input

def get_tuning_freq(x_coord, y_coord):
    return 4000000 * x_coord + y_coord

def check_if_non_covered(minimal_ranges, min_x, max_x):
    # returns x value if one exists, else None
    min_x_covered = None
    max_x_covered = None
    for r in minimal_ranges:
        # min_x was covered and we can start the search
        if min_x >= r[0] and min_x <=r[1]:
            min_x_covered = min_x
            max_x_covered = r[1]
        # cover the case where the only spot is min_x
        elif min_x_covered == None and min_x+1 >= r[0] and min_x+1 <=r[1]: 
            return min_x
        # if the whole range of possible x values are covered return None
        if max_x_covered >= max_x:
            break
        # check if next part of range is covered by next min_range
        if max_x_covered+1 >= r[0] and max_x_covered+1 <= r[1]:
            max_x_covered = r[1] # extend the range
        else:
            return max_x_covered + 1

for y in range(0, max_beacon_coord + 1):
    target_y_covered_ranges = []
    for pair in pairs:
        sensor = pair[0]
        beacon = pair[1]
        # Check if the sensor is relevant for this target y
        if is_pair_relevant(sensor, beacon, y) == False:
            continue
        # Find covered ranges
        target_y_covered_ranges.append(get_range_on_target_y(sensor, manhattan_dist(sensor, beacon), y))
    # Calculate covered ranges
    minimal_ranges = condense_ranges(target_y_covered_ranges)
    # Check if any spots are available for the distress beacon
    result = check_if_non_covered(minimal_ranges, 0, max_beacon_coord)
    if result is not None:
        print("Part 2:", get_tuning_freq(result, y))
        break