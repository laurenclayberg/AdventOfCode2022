class Monkey:
    def __init__(self, items, operation, test, true_monkey, false_monkey, max_val=None):
        self.items = items
        self.operation = operation
        self.test = test
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.count = 0
        self.max_val = max_val

    def inspect_items(self, monkey_list):
        for item in self.items:
            new_item = self.operation(item)
            if self.max_val != None:
                new_item = new_item % self.max_val
            if new_item % self.test == 0:
                monkey_list[self.true_monkey].items.append(new_item)
            else:
                monkey_list[self.false_monkey].items.append(new_item)
            self.count += 1
        self.items = []

    def inspect_item_individual(self, item):
        # returns index of new monkey when processing one item
        new_item = self.operation(item)
        if new_item % self.test == 0:
            return new_item, self.true_monkey
        return new_item, self.false_monkey

# Set up monkeys
monkeys_mini = []
monkeys_mini.append(Monkey([79,98], lambda x: int((x*19)/3), 23, 2, 3))
monkeys_mini.append(Monkey([54,65,75,74], lambda x: int((x+6)/3), 19, 2, 0))
monkeys_mini.append(Monkey([79,60,97], lambda x: int((x*x)/3), 13, 1, 3))
monkeys_mini.append(Monkey([74], lambda x: int((x+3)/3), 17, 0, 1))

monkeys_mini_2 = []
# 96577 = 23*19*13*17
monkeys_mini_2.append(Monkey([79,98], lambda x: (x*19), 23, 2, 3, 96577))
monkeys_mini_2.append(Monkey([54,65,75,74], lambda x: (x+6), 19, 2, 0, 96577))
monkeys_mini_2.append(Monkey([79,60,97], lambda x: (x*x), 13, 1, 3, 96577))
monkeys_mini_2.append(Monkey([74], lambda x: (x+3), 17, 0, 1, 96577))

monkeys_1 = []
monkeys_1.append(Monkey([80], lambda x: int((x*5)/3), 2, 4, 3))
monkeys_1.append(Monkey([75,83,74], lambda x: int((x+7)/3), 7, 5, 6))
monkeys_1.append(Monkey([86,67,61,96,52,63,73], lambda x: int((x+5)/3), 3, 7, 0))
monkeys_1.append(Monkey([85,83,55,85,57,70,85,52], lambda x: int((x+8)/3), 17, 1, 5))
monkeys_1.append(Monkey([67,75,91,72,89], lambda x: int((x+4)/3), 11, 3, 1))
monkeys_1.append(Monkey([66,64,68,92,68,77], lambda x: int((x*2)/3), 19, 6, 2))
monkeys_1.append(Monkey([97,94,79,88], lambda x: int((x*x)/3), 5, 2, 7))
monkeys_1.append(Monkey([77,85], lambda x: int((x+6)/3), 13, 4, 0))

monkeys_2 = []
# 9699690 = 2*7*3*17*11*29*5*13
monkeys_2.append(Monkey([80], lambda x: (x*5), 2, 4, 3, 9699690))
monkeys_2.append(Monkey([75,83,74], lambda x: (x+7), 7, 5, 6, 9699690))
monkeys_2.append(Monkey([86,67,61,96,52,63,73], lambda x: (x+5), 3, 7, 0, 9699690))
monkeys_2.append(Monkey([85,83,55,85,57,70,85,52], lambda x: (x+8), 17, 1, 5, 9699690))
monkeys_2.append(Monkey([67,75,91,72,89], lambda x: (x+4), 11, 3, 1, 9699690))
monkeys_2.append(Monkey([66,64,68,92,68,77], lambda x: (x*2), 19, 6, 2, 9699690))
monkeys_2.append(Monkey([97,94,79,88], lambda x: (x*x), 5, 2, 7, 9699690))
monkeys_2.append(Monkey([77,85], lambda x: (x+6), 13, 4, 0, 9699690))

# Solve part 1
print("Part 1")
monkeys = monkeys_1
for round in range(20):
    for monkey in monkeys:
        monkey.inspect_items(monkeys)
answer = []
for monkey in monkeys:
    answer.append(monkey.count)
answer.sort()
print("Part 1: ", answer[-1] * answer[-2])
    
# Solve part 2
print("Part 2")
monkeys = monkeys_2
for round in range(10000):
    for monkey in monkeys:
        monkey.inspect_items(monkeys)
answer = []
for monkey in monkeys:
    answer.append(monkey.count)
answer.sort()
print("Part 2: ", answer[-1] * answer[-2])
# monkey_items = []
# monkeys = monkeys_2
# for m in range(len(monkeys)):
#     monkey = monkeys[m]
#     for item in monkey.items:
#         # (cur_item, orig_item, cur_index, orig_index)
#         monkey_items.append((item, item, m, m))

# monkey_states = {}
# def get_state(monkey_items):
#     # sort first by orig monkey, then by orig value
#     monkey_items.sort(key=lambda x: (x[3], x[1]))
#     state_temp = []
#     # state includes original value, current index
#     for item in monkey_items:
#         state_temp.append(item[1])
#         state_temp.append(item[2])
#     state_final = tuple(state_temp)
#     return state_final

# for round in range(10000):
#     state = get_state(monkey_items)
#     if state in monkey_states:
#         print("State match: ", monkey_states[state], round)
#         break
#     else:
#         monkey_states[state] = round
#     for m in range(len(monkey_items)):
#         old_item = monkey_items[m]
#         monkey = monkeys[old_item[2]] # get the monkey
#         new_item, new_index = monkey.inspect_item_individual(old_item[0])
#         monkey_items[m] = (new_item, old_item[1], new_index, old_item[3])

