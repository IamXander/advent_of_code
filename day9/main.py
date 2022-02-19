import statistics
from typing import List

input: List[List[int]] = []


with open('input.txt') as f:
    for line in f.read().split('\n'):
        input.append(list([int(l) for l in line]))

cnt = 0
basin_t = []
# print(input)
for y in range(len(input)):
    for x in range(len(input[y])):
        v = input[y][x]
        if v == 9:
            continue
        basin_s = [(y, x)]
        basin = 1
        input[y][x] = 9
        while basin_s:
            yn, xn = basin_s.pop()
            if yn > 0 and input[yn-1][xn] < 9:
                basin_s.append((yn-1, xn))
                basin += 1
                input[yn-1][xn] = 9
            if xn > 0 and input[yn][xn-1] < 9:
                basin_s.append((yn, xn-1))
                basin += 1
                input[yn][xn-1] = 9
            if yn+1 < len(input) and input[yn+1][xn] < 9:
                basin_s.append((yn+1, xn))
                basin += 1
                input[yn+1][xn] = 9
            if xn+1 < len(input[yn]) and input[yn][xn+1] < 9:
                basin_s.append((yn, xn+1))
                basin += 1
                input[yn][xn+1] = 9
        basin_t.append(basin)
print(sorted(basin_t))
# 221 is too low
# 223 is too low