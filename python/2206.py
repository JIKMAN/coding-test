from collections import deque
from copy import deepcopy

n , m = map(int, input().split())

graph = [list(map(int,input())) for _ in range(n)]


def bfs():
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    map = deepcopy(graph)
    map[0][0] = 1

    q = deque([(0,0)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if map[nx][ny] == 0:
                    map[nx][ny] = map[x][y] + 1
                    q.append((nx, ny))
    if map[n-1][m-1] == 0:
        return -1
    else:
        return map[n-1][m-1]

min_val = 1000000

if bfs() != -1:
    min_val = bfs()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            graph[i][j] = 0
            if bfs() != -1 and bfs() < min_val:
                min_val = bfs()
            graph[i][j] = 1

if min_val == 1000000:
    print(-1)
else:
    print(min_val)