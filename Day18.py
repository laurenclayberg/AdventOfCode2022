with open('input/day18.txt') as f:
    lines = f.readlines()
cubes = set()
max_index = 0
for line in lines:
    cube = eval('(' + line.strip() + ')')
    cube = list(cube)
    for i in range(3):
        cube[i] += 1
        max_index = max(max_index, cube[i])
    cube = tuple(cube)
    cubes.add(cube)

# Part 1
surface_area = 0
for cube in cubes:
    surface_area_to_add = 0
    for i in [-1,1]:
        for j in [0,1,2]:
            cube_ = list(cube)
            cube_[j] = cube[j] + i
            cube_ = tuple(cube_)
            if cube_ not in cubes:
                surface_area_to_add += 1
    surface_area += surface_area_to_add
print("Part 1:", surface_area)

# Part 2
full_cube = [[[False for _ in range(max_index+2)] for _ in range(max_index+2)] for _ in range(max_index+2)]

# go through each slice of the sube in each direction
cubes_to_explore = [(0,0,0)]
marked_cubes = set()
while len(cubes_to_explore) != 0:
    cube = cubes_to_explore.pop() # explore next cube
    if cube in marked_cubes: # ignore if previously explored
        continue
    marked_cubes.add(cube)
    for i in [-1,1]:
        for j in [0,1,2]:
            cube_ = list(cube)
            cube_[j] = cube_[j] + i
            cube_ = tuple(cube_)
            if cube_[j] >= 0 and cube_[j] < len(full_cube): # target cube in range
                if cube_ not in marked_cubes and cube_ not in cubes:
                    cubes_to_explore.append(cube_)


surface_area = 0
for cube in cubes:
    surface_area_to_add = 0
    for i in [-1,1]:
        for j in [0,1,2]:
            # cube_ is the surface area cube
            cube_ = list(cube)
            cube_[j] = cube_[j] + i
            cube_ = tuple(cube_)
            if cube_ not in cubes and cube_ in marked_cubes:
                surface_area_to_add += 1
    surface_area += surface_area_to_add
print("Part 2:", surface_area)



