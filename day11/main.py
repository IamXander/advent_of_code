import itertools
import statistics
from typing import List

input: List[List[int]] = []


with open('input.txt') as f:
    for line in f.read().split('\n'):
        input.append([int(a) for a in line])

w = len(input[0])
h = len(input)
flashes = 0
i = 0
while True:
    inc = [(y,x) for y, x in itertools.product(range(h), range(w))]
    already_flashed = set()
    while inc:
        y,x = inc.pop()
        if (y,x) in already_flashed:
            continue
        input[y][x] += 1
        if input[y][x] > 9:
            already_flashed.add((y,x))
            input[y][x] = 0
            flashes += 1
            for yn, xn in itertools.product([y-1, y, y+1], [x-1, x, x+1]):
                if yn == y and xn == x:
                    continue
                if yn < 0 or yn >= h or xn < 0 or xn >= w:
                    continue
                inc.append((yn, xn))
    i += 1
    if len(already_flashed) == w*h:
        break
print(flashes)
print(i)
# 226 is too low

