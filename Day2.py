# Parse input
input_clean = []
with open('input/day2_1.txt') as f:
    lines = f.readlines()
for line in lines:
    input_clean.append(line.split())

# Solve Part 1
score = 0
for round in input_clean:
    if round[0] == 'A' and round[1] == 'X':
        score += 1 + 3
    elif round[0] == 'A' and round[1] == 'Y':
        score += 2 + 6
    elif round[0] == 'A' and round[1] == 'Z':
        score += 3 + 0
    elif round[0] == 'B' and round[1] == 'X':
        score += 1 + 0
    elif round[0] == 'B' and round[1] == 'Y':
        score += 2 + 3
    elif round[0] == 'B' and round[1] == 'Z':
        score += 3 + 6
    elif round[0] == 'C' and round[1] == 'X':
        score += 1 + 6
    elif round[0] == 'C' and round[1] == 'Y':
        score += 2 + 0
    elif round[0] == 'C' and round[1] == 'Z':
        score += 3 + 3

print(score)

# Solve Part 2
score = 0
for round in input_clean:
    # rock 1
    if round[0] == 'A' and round[1] == 'X': # lose
        score += 0 + 3
    elif round[0] == 'A' and round[1] == 'Y': # draw
        score += 3 + 1
    elif round[0] == 'A' and round[1] == 'Z': # win
        score += 6 + 2
    # paper 2
    elif round[0] == 'B' and round[1] == 'X': # lose
        score += 0 + 1
    elif round[0] == 'B' and round[1] == 'Y': # draw
        score += 3 + 2
    elif round[0] == 'B' and round[1] == 'Z': # win
        score += 6 + 3
    # scissors 3
    elif round[0] == 'C' and round[1] == 'X': # lose
        score += 0 + 2
    elif round[0] == 'C' and round[1] == 'Y': # draw
        score += 3 + 3
    elif round[0] == 'C' and round[1] == 'Z': # win
        score += 6 + 1

print(score)