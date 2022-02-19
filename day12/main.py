import itertools
import statistics
from typing import DefaultDict, List

input = DefaultDict(list)


with open('input.txt') as f:
    for line in f.read().split('\n'):
        s, e = line.split("-")
        input[s].append(e)
        input[e].append(s)
input = dict(input)
print(input)

def find_paths(cnode, visited, visited_2):
    if cnode == "end":
        return 1
    cnt = 0
    for node in input[cnode]:
        if node.isupper():
            cnt += find_paths(node, visited, visited_2)
        elif not node in visited:
            visited.add(node)
            cnt += find_paths(node, visited, visited_2)
            visited.remove(node)
        elif visited_2 == False and node != "start" and node != "end":
            cnt += find_paths(node, visited, True)
    return cnt


# 9390 is too high
# 5958 is correct
# 153858 is too high
print(find_paths("start", set(["start"]), False))