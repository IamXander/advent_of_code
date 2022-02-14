fish = []
cnt = 0

with open('input.txt') as f:
    fish = [int(x) for x in f.read().split(',')]

# 0: 1 (0)
# 1: 2 (6, 8)
# 2: 2 (5, 7)
# 3: 2 (4, 6)
# 4: 2 (3, 5)
# 5: 2 (2, 4)
# 6: 2 (1, 3)
# 7: 2 (0, 2)
# 8: 2 (5, 1, 8)

t = [0]
cache = {}
for i in range(9):
    cache[(0,i)] = 1

for day in range(1, 257):
    cache[(day, 0)] = cache[(day-1, 6)] + cache[(day-1, 8)]
    for age in range(1, 9):
        cache[(day, age)] = cache[(day-1, age-1)]

# print(cache[])

# ^floor((days-s)/6)

# A = 1(1 + )


print(sum([cache[(256, f)] for f in fish]))
    

# for i in range(80):
#     l = len(t)
#     for f in range(l):
#         if t[f] == 0:
#             t[f] = 6
#             t.append(8)
#         else:
#             t[f] -= 1
#     # print(fish, len(fish), )
# print(len(t))