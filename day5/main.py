m = {}
cnt = 0

with open('input.txt') as f:
    for line in f:
        # print(line)
        start, end = line.split(" -> ")
        # print(start, end)
        if start == end:
            print("abc")
        sx, sy = [int(x) for x in start.split(",")]
        ex, ey = [int(x) for x in end.split(",")]
        if sx == ex:
            for y in range(min(ey, sy), max(ey, sy)+1):
                pos = (sx, y)
                m.setdefault(pos, 0)
                m[pos] += 1
                if m[pos] == 2:
                    cnt += 1
        elif ey == sy:
            for x in range(min(ex, sx), max(ex, sx)+1):
                pos = (x, sy)
                m.setdefault(pos, 0)
                m[pos] += 1
                if m[pos] == 2:
                    cnt += 1
        else:
            print("HERE: ", start, end)
            x = sx
            y = sy
            dx = (ex - sx)/abs(ex - sx)
            dy = (ey - sy)/abs(ey - sy)
            while (x, y) != (ex+dx, ey+dy):
                # print(x, y)
                pos = (x, y)
                m.setdefault(pos, 0)
                m[pos] += 1
                if m[pos] == 2:
                    cnt += 1
                x += dx
                y += dy
        
# 21624 - too high
# 21113 - too low
# 21134 - too low
print(cnt)