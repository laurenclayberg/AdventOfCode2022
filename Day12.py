import networkx as nx

# Parse Input
input = []
with open('input/day12.txt') as f:
    lines = f.readlines()
for line in lines:
    input.append(list(line.split()[0]))

# Setup
alpha = 'abcdefghijklmnopqrstuvwxyz'
alpha_dict = {}
for a in range(len(alpha)):
    alpha_dict[alpha[a]] = a
start = None
possible_starts = []
end = None
G = nx.DiGraph()
for i in range(len(input)):
    for j in range(len(input[0])):
        if input[i][j] == 'S':
            start = (i,j)
            possible_starts.append((i,j))
            input[i][j] = 'a'
        elif input[i][j] == 'a':
            possible_starts.append((i,j))
        elif input[i][j] == 'E':
            end = (i,j)
            input[i][j] = 'z'
for i in range(len(input)):
    for j in range(len(input[0])):
        cur = (i,j)
        cur_letter = input[i][j]
        for x in [-1,1]:
            if i + x >= 0 and i + x < len(input):
                next = (i+x,j)
                next_letter = input[i+x][j]
                if alpha_dict[next_letter] <= alpha_dict[cur_letter] + 1:
                    G.add_edge(cur,next)
            if j + x >= 0 and j + x < len(input[0]):
                next = (i,j+x)
                next_letter = input[i][j+x]
                if alpha_dict[next_letter] <= alpha_dict[cur_letter] + 1:
                    G.add_edge(cur,next)

# Solve part 1
print("Part 1: ", nx.shortest_path_length(G, start, end))

# Solve part 2
min_path = None
for start in possible_starts:
    try:
        cur_path = nx.shortest_path_length(G, start, end)
        if min_path == None or cur_path < min_path:
            min_path = cur_path
    except nx.NetworkXNoPath:
        continue
print("Part 2: ", min_path)
