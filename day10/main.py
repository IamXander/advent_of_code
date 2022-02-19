import statistics
from typing import List

input: List[List[int]] = []

score = 0
scores = []
with open('input.txt') as f:
    for line in f.read().split('\n'):
        stack = ['a']
        for l in line:
            score_s = score
            if l in "([{<":
                stack.append(l)
            elif l == ')':
                if stack[-1] != '(':
                    score += 3
                    break
                stack.pop()
            elif l == ']':
                if stack[-1] != '[':
                    score += 57
                    break
                stack.pop()
            elif l == '}':
                if stack[-1] != '{':
                    score += 1197
                    break
                stack.pop()
            elif l == '>':
                if stack[-1] != '<':
                    score += 25137
                    break
                stack.pop()
        if score_s != score:
            continue
        ns = 0
        while stack != ['a']:
            ns *= 5
            c = stack.pop()
            if c == "(":
                ns += 1
            elif c == "[":
                ns += 2
            elif c == "{":
                ns += 3
            elif c == "<":
                ns += 4
        scores.append(ns)


print(score)
print(statistics.median(scores))