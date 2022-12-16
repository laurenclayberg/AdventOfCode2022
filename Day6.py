# Parse Input
signals = []
with open('input/day6_1.txt') as f:
    lines = f.readlines()
for line in lines:
    signals.append(list(line));

# Solve Part 1
signal = signals[0]
buffer = signal[:4]
pointer = 0
answer = None
for i in range(4, len(signal)):
    # first check buffer
    if len(set(buffer)) == 4:
        answer = i
        break
    # then update the buffer
    buffer[pointer] = signal[i]
    pointer = (pointer + 1) % 4
if answer == None:
    anser = len(signal);
print(answer)

# Solve Part 2
signal = signals[0]
buffer = signal[:14]
pointer = 0
answer = None
for i in range(14, len(signal)):
    # first check buffer
    if len(set(buffer)) == 14:
        answer = i
        break
    # then update the buffer
    buffer[pointer] = signal[i]
    pointer = (pointer + 1) % 14
if answer == None:
    anser = len(signal);
print(answer)