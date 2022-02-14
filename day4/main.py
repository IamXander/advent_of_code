boards = []
content = ""

with open('input.txt') as f:
    content = f.read().split('\n')
nums = [int(x) for x in content[0].split(",")]
print(nums)
slow_win = 0
m = 0
for i in range(2, len(content), 6):
    board = []
    board.append([int(c) for c in content[i].strip().split()])
    board.append([int(c) for c in content[i+1].strip().split()])
    board.append([int(c) for c in content[i+2].strip().split()])
    board.append([int(c) for c in content[i+3].strip().split()])
    board.append([int(c) for c in content[i+4].strip().split()])
    rows = [0, 0, 0, 0, 0]
    cols = [0, 0, 0, 0, 0]
    lookup = {}
    for y in range(5):
        for x in range(5):
            lookup[board[y][x]] = (y, x)
    for i, num in enumerate(nums):
        if num in lookup:
            y, x = lookup[num]
            rows[y] += 1
            cols[x] += 1
            board[y][x] = 0
            if rows[y] >= 5 or cols[x] >= 5:
                if i > slow_win:
                    slow_win = i
                    m = num * sum([sum(x) for x in board])
                break
    # boards.append(board)

print(m)