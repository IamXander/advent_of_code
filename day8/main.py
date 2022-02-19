import statistics
from typing import List

inputs: List[List[str]] = []
decode: List[List[str]] = []


with open('input.txt') as f:
    for line in f:
        data = line.split()
        # print(data)
        inputs.append([''.join(sorted(s)) for s in data[0:10]])
        decode.append([''.join(sorted(s)) for s in data[11:]])

# 5 = 2/3/5
# 6 = 0/6/9

cnt = 0
for idx, d in enumerate(decode):
    buildup = {}
    for num in inputs[idx]:
        print(inputs[idx])
        if len(num) == 2: # 1
            buildup[num] = 1
            buildup[1] = num
        elif len(num) == 3: # 7
            buildup[num] = 7
            buildup[7] = num
        elif len(num) == 4: # 4
            buildup[num] = 4
            buildup[4] = num
        elif len(num) == 7: # 8
            buildup[num] = 8
            buildup[8] = num
    # Figure out 2/3/6/9:
    for num in inputs[idx]:
        if len(num) == 5 and all([True if x in num else False for x in buildup[1]]):
            assert 3 not in buildup
            buildup[3] = num
            buildup[num] = 3
        if len(num) == 5 and sum([1 if x in num else 0 for x in buildup[4]]) == 2:
            assert 2 not in buildup
            buildup[2] = num
            buildup[num] = 2
        if len(num) == 6 and all([True if x in num else False for x in buildup[1]]) == False:
            assert 6 not in buildup
            buildup[6] = num
            buildup[num] = 6
        if len(num) == 6 and all([True if x in num else False for x in buildup[4]]):
            assert 9 not in buildup
            buildup[9] = num
            buildup[num] = 9
    for num in inputs[idx]:
        if num not in buildup:
            if len(num) == 5:
                buildup[5] = num
                buildup[num] = 5
            elif len(num) == 6:
                buildup[0] = num
                buildup[num] = 0

    print(buildup)
    decoded_num = 0
    for num in d:
        decoded_num *= 10
        decoded_num += buildup[num]
    cnt += decoded_num
print(cnt)

# 3668 = too low