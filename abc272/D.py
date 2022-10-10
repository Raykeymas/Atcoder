from collections import deque

N, M = map(int, input().split(" "))
ground = [[-1 for _ in range(N)] for _ in range(N)]
ground[0][0] = 0
# 動ける範囲を計算する
move_set = set()
for i in range(-N, N):
    for k in range(-N, N):
        d = i**2 + k**2
        if d == M:
            move_set.add((i, k))

# BFSで最小経路を計算する
queue = deque()
queue.append((0, 0))
while queue:
    x, y = queue.popleft()
    for d_x, d_y in move_set:
        after_x, after_y = x+d_x, y+d_y
        if after_x < 0 or after_y < 0 or after_x >= N or after_y >= N:
            continue
        elif ground[after_x][after_y] != -1:
            continue
        else:
            queue.append((after_x, after_y))
            ground[after_x][after_y] = ground[x][y] + 1

for g in ground:
    print(*g)
