## baekjoon 7576 : https://www.acmicpc.net/problem/7576

from collections import deque
from copy import deepcopy

m, n = map(int, input().split())

box = []
for i in range(n):
    box.append(list(map(int, input().split())))

def bfs(m, n, box):
    days = [[0] * m for _ in range(n)]
    tmp = deepcopy(box)

    q = deque()

    for i in range(n):
        for j in range(m):
            if box[i][j] == 1:
                q.append((i, j))

    dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if box[nx][ny] == 0:
                    box[nx][ny] = 1
                    days[nx][ny] = days[x][y] + 1
                    q.append((nx, ny))

    min_v = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == days[i][j]:
                return -1
            if days[i][j] > min_v:
                min_v = days[i][j]
    return min_v

print(bfs(m, n, box))
