from functools import cmp_to_key
input = []
input2 = [[[2]],[[6]]]
with open('input/day13.txt') as f:
    lines = f.readlines()
first = None
second = None
i = 0
for line in lines:
    if i == 0:
        first = eval(line)
        input2.append(eval(line))
    elif i == 1:
        second = eval(line)
        input2.append(eval(line))
    elif i == 2:
        input.append((first, second))
    i = (i + 1) % 3
input.append((first,second))

# return -1 if left > right, 1 if right > left, 0 if equal
def compare(left, right):
    comp_val = 0
    if isinstance(left, int) and isinstance(right, int):
        comp_val = -1 if left > right else 1 if left < right else 0
    elif isinstance(left, int) and isinstance(right, list):
        left = [left]
        comp_val = compare(left, right)
    elif isinstance(left, list) and isinstance(right, int):
        right = [right]
        comp_val = compare(left, right)
    elif isinstance(left, list) and isinstance(right, list):
        for i in range(len(left)):
            if i < len(right): # there exist right vals for comparison
                comp_val = compare(left[i], right[i])
            else: 
                comp_val = -1 # right ran out of values first
            if comp_val != 0:
                break
        if comp_val == 0 and len(left) < len(right): # left ran out of values first
            comp_val = 1
    
    return comp_val
        
# Sanity checks
# print(compare(2,3), compare(3,2), compare(2,2)) # 1, -1, 0
# print(compare([1],2), compare([1],[2]), compare(1,[2])) # 1, 1, 1
# print(compare([0,1,2],2), compare(2,[0,1,2])) # 1, -1
# print(compare([],2), compare(2,[[],1,2])) # 1, -1
# print(compare([],[]), compare([],[[]]), compare([[]],[])) # 0, 1, -1
# print(compare([[1,2,3],[2,3]],[[1,2,[3]],[[2],[4]]]),compare([[1,2,3],[2,3]],[[1,2,[3]],[[2],[1]]])) # 1, -1
# print(compare([[1,4,3],[2,3]],[[1,2,[3]],[[2],[4]]]),compare([[1,1,3],[2,3]],[[1,2,[3]],[[2],[1]]])) # -1, 1
# print(compare([1],[1,2]), compare([1,2],[1])) # 1, -1
# print(compare([1],1), compare(1,[1])) # 0, 0
# print(compare([[5]],[[[[8,9],[5,10,8,1],2],[[2,6],6],5],[1],[],[6,[[],3,[8,9,0,1],7]]])) # 1
# print(compare(2,[[[[[[4]]]]]]), compare([[[[[[[[[[[4]]]]]]]]]]],1)) # 1 -1

# Solve part 1
answer = 0
for p in range(len(input)):
    pair = input[p]
    comp_val = compare(pair[0], pair[1])
    if comp_val == 1:
        answer += p + 1
    elif comp_val == 0:
        print("Error", p)
print("Part 1:", answer)

# Solve part 2
input2 = sorted(input2, key=cmp_to_key(compare), reverse=True)
index_1 = input2.index([[2]]) + 1
index_2 = input2.index([[6]]) + 1
print("Part 2:",  index_1 * index_2)