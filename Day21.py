with open('input/day21.txt') as f:
    lines = f.readlines()
monkeys = {}
for line in lines:
    line_split = line.split()
    monkey = line_split[0][:-1]
    if len(line_split) == 2:
        monkeys[monkey] = int(line_split[1])
    else: 
        monkeys[monkey] = {}
        monkeys[monkey]['op'] = line_split[2]
        monkeys[monkey]['vals'] = [line_split[1], line_split[3]]

human_ref = 'humn'
def get_monkey_value(monkey):
    if isinstance(monkeys[monkey], int) or isinstance(monkeys[monkey], float):
        return monkeys[monkey], monkey == human_ref
    else:
        monkey1, req_human_1 = get_monkey_value(monkeys[monkey]['vals'][0])
        monkey2, req_human_2 = get_monkey_value(monkeys[monkey]['vals'][1])
        op = monkeys[monkey]['op']
        if op == '*':
            return monkey1 * monkey2, req_human_1 or req_human_2
        elif op == '/':
            return monkey1 / monkey2, req_human_1 or req_human_2
        elif op == '-':
            return monkey1 - monkey2, req_human_1 or req_human_2
        elif op == '+':
            return monkey1 + monkey2, req_human_1 or req_human_2

# Part 1
print("Part 1:", int(get_monkey_value('root')[0]))

# Part 2
# First check if both root sub problems require humn input
monkey1 = monkeys['root']['vals'][0]
monkey2 = monkeys['root']['vals'][1]

_, monkey1_req_human = get_monkey_value(monkey1)
monkey2_value, monkey2_req_human = get_monkey_value(monkey2)
print("Monkey 1 requires human:", monkey1_req_human)
print("Monkey 2 requires human:", monkey2_req_human)

# Only monkey 1 requires the human input
# Now work backwards for monkey 1 to get the correct human input

def get_new_req_value(orig_value_req, sub_val, op, sub_val_is_left):
    if op == '*': # a * b = orig_value_req
        return orig_value_req / sub_val
    elif op == '/': # a / b = orig_value_req
        if sub_val_is_left:
            return sub_val / orig_value_req
        else:
            return orig_value_req * sub_val
    elif op == '-': # a - b = orig_value_req
        if sub_val_is_left:
            return sub_val - orig_value_req
        else:
            return orig_value_req + sub_val
    elif op == '+': # a + b = orig_value_req
        return orig_value_req - sub_val

def get_human_value(monkey, value_req):
    if monkey == human_ref:
        return value_req
    else:
        monkey1 = monkeys[monkey]['vals'][0]
        monkey1_value, monkey1_req_human = get_monkey_value(monkey1)
        monkey2 = monkeys[monkey]['vals'][1]
        monkey2_value, monkey2_req_human = get_monkey_value(monkey2)
        op = monkeys[monkey]['op']
        if monkey1_req_human and not monkey2_req_human:
            return get_human_value(monkey1, get_new_req_value(value_req, monkey2_value, op, False))
        elif monkey2_req_human and not monkey1_req_human:
            return get_human_value(monkey2, get_new_req_value(value_req, monkey1_value, op, True))

answer = get_human_value(monkey1, monkey2_value)
print("Part 2:", int(answer))
monkeys[human_ref] = answer
# Verify answer
print("Verify part 2:")
print(get_monkey_value(monkey1)[0], get_monkey_value(monkey2)[0])

