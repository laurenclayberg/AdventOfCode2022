# Parse Input
forest = []
with open('input/day8.txt') as f:
    lines = f.readlines()
for line in lines:
    forest.append(list(line.split()[0]));

forest_mark = []
scores = []
for i in range(len(forest)):
    forest_mark.append([])
    scores.append([])
    for j in range(len(forest[i])):
        forest[i][j] = int(forest[i][j])
        forest_mark[i].append(0)
        scores[i].append(0)

# Solve Part 1
# First check left to right and right to left
for i in range(len(forest)):
    row = forest[i]
    row_mark = forest_mark[i]
    row_mark[0] = 1
    row_mark[len(row)-1] = 1
    prev_max = row[0]
    for j in range(1, len(row)-1):
        if row[j] > prev_max:
            row_mark[j] = 1
            prev_max = row[j]
    prev_max = row[len(row)-1]
    for j in range(len(row)-2, 0, -1):
        if row[j] > prev_max:
            row_mark[j] = 1
            prev_max = row[j]

# Next top to bottom and bottom to top
for i in range(len(forest[0])): # which column
    forest_mark[0][i] = 1
    forest_mark[len(forest)-1][i] = 1
    prev_max = forest[0][i]
    for j in range(1, len(forest)-1): # which row
        if forest[j][i] > prev_max:
            forest_mark[j][i] = 1
            prev_max = forest[j][i]
    prev_max = forest[len(forest)-1][i]
    for j in range(len(forest)-2, 0, -1):
        if forest[j][i] > prev_max:
            forest_mark[j][i] = 1
            prev_max = forest[j][i]

answer = 0
for i in range(len(forest)):
    for j in range(len(forest[i])):
        answer += forest_mark[i][j]
print(answer)

# Solve Part 2
for i in range(len(forest)):
    for j in range(len(forest[0])):
        cur_tree = forest[i][j]
        # check left
        a_count = 0
        for a in range(j-1, -1, -1):
            if forest[i][a] < cur_tree:
                a_count += 1
            else:
                a_count += 1
                break
        # check right
        b_count = 0
        for b in range(j+1, len(forest[i])):
            if forest[i][b] < cur_tree:
                b_count += 1
            else:
                b_count += 1
                break
        # check up
        c_count = 0
        for c in range(i-1, -1, -1):
            if forest[c][j] < cur_tree:
                c_count += 1
            else:
                c_count += 1
                break
        # check down
        d_count = 0
        for d in range(i+1, len(forest)):
            if forest[d][j] < cur_tree:
                d_count += 1
            else:
                d_count += 1
                break
        scores[i][j] = a_count * b_count * c_count * d_count
answer = 0
for i in range(len(scores)):
    for j in range(len(scores[i])):
        answer = max(answer, scores[i][j])
print(answer)