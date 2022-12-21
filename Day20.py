class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

input = []
input2 = []
with open('input/day20.txt') as f:
    lines = f.readlines()
for line in lines:
    input.append(Node(int(line)))
    input2.append(Node(int(line)*811589153))

# Connect the nodes
for i in range(len(input)):
    cur_node = input[i]
    next_node = input[(i+1)%len(input)]
    cur_node.next = next_node
    next_node.prev = cur_node

    cur_node = input2[i]
    next_node = input2[(i+1)%len(input2)]
    cur_node.next = next_node
    next_node.prev = cur_node

# Sub routine to handle node swaps
MOD_SIZE = len(input) - 1
def handle_swaps_pos(node):
    global MOD_SIZE
    for _ in range(node.value % MOD_SIZE):
        swap_node = node.next
        swap_node.prev = node.prev
        node.prev.next = swap_node
        node.next = swap_node.next
        swap_node.next.prev = node
        node.prev = swap_node
        swap_node.next = node
def handle_swaps_neg(node):
    global MOD_SIZE
    for _ in range(abs(node.value) % MOD_SIZE):
        swap_node = node.prev
        swap_node.next = node
        node.prev = swap_node.prev
        swap_node.prev.next = node
        swap_node.next = node.next
        node.next.prev = swap_node
        node.next = swap_node
        swap_node.prev = node
def handle_swaps(node):
    if node.value > 0:
        handle_swaps_pos(node)
    elif node.value < 0:
        handle_swaps_neg(node)

def handle_swaps_alt(node):
    if node.value != 0:
        handle_swaps_pos(node)

def print_node_order(nodes):
    result = ''
    count = 0
    node = nodes[0]
    while count < len(nodes):
        result += str(node.value) + ', '
        node = node.next
        count += 1
    print(result)

# Solve part 1
# -- Do the swaps
# print_node_order(input)
for node in input:
    handle_swaps(node)
    # print_node_order(input)

# -- Find the grove coordinates
print('Part 1 grove coordinates:')
index_zero = None
for n in range(len(input)):
    if input[n].value == 0:
        index_zero = n
        break 
next_node = input[index_zero]
for i in range(3000):
    next_node = next_node.next
    if i in [999, 1999, 2999]:
        print(i+1, next_node.value)

# Solve part 2
# -- Do the swaps
# print_node_order(input2)
for _ in range(10):
    for node in input2:
        handle_swaps(node)
        # print_node_order(input2)

# -- Find the grove coordinates
print('Part 2 grove coordinates:')
index_zero = None
for n in range(len(input2)):
    if input2[n].value == 0:
        index_zero = n
        break 
next_node = input2[index_zero]
answer = 0
for i in range(3000):
    next_node = next_node.next
    if i in [999, 1999, 2999]:
        answer += next_node.value
        print(i+1, next_node.value)
print(answer)