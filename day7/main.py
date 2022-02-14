import statistics

fish = []
cnt = 0

with open('input.txt') as f:
    fish = [int(x) for x in f.read().split(',')]

fish = sorted(fish)
m = statistics.median(fish)
print(sum([abs(d-m) for d in fish]))
