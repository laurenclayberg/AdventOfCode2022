import re

# Parse Input
input_clean = []
with open('input/day4_1.txt') as f:
    lines = f.readlines()
for line in lines:
    line_clean = re.split('[,-]',line.split()[0])
    input_clean.append(line_clean)

# Solve Part 1
answer = 0
for pair in input_clean:
    p1_min = int(pair[0])
    p1_max = int(pair[1])
    p2_min = int(pair[2])
    p2_max = int(pair[3])
    if p1_min >= p2_min and p1_max <= p2_max:
        answer += 1
    elif p1_min <= p2_min and p1_max >= p2_max:
        answer += 1
print(answer)

# Solve Part 2
answer = 0
for pair in input_clean:
    p1_min = int(pair[0])
    p1_max = int(pair[1])
    p2_min = int(pair[2])
    p2_max = int(pair[3])
    if (p1_min >= p2_min and p1_min <= p2_max) or (p1_max >= p2_min and p1_max <= p2_max):
        answer += 1
    elif (p2_min >= p1_min and p2_min <= p1_max) or (p2_max >= p1_min and p2_max <= p1_max):
        answer += 1
print(answer)