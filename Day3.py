import string 

# Parse input
input_clean = []
input_2_clean = []
with open('input/day3_1.txt') as f:
    lines = f.readlines()
for line in lines:
    line_clean = line.split()[0]
    input_2_clean.append(line_clean)
    line_length = int(len(line_clean)/2)
    input_clean.append([line_clean[:line_length], line_clean[line_length:]])

# Solve Part 1
priorities = {}
i = 1
for letter in string.ascii_lowercase:
    priorities[letter] = i
    i += 1
for letter in string.ascii_uppercase:
    priorities[letter] = i
    i += 1

answer = 0
for sack in input_clean:
    sack1 = set(list(sack[0]))
    sack2 = set(list(sack[1]))
    intersection = list(sack1.intersection(sack2))
    for item in intersection:
        answer += priorities[item]

print(answer)

# Solve Part 2
answer = 0
for i in range(0, len(input_2_clean), 3):
    sack1 = set(list(input_2_clean[i]))
    sack2 = set(list(input_2_clean[i+1]))
    sack3 = set(list(input_2_clean[i+2]))
    intersection = list(sack1.intersection(sack2).intersection(sack3))
    for item in intersection:
        answer += priorities[item]

print(answer)
