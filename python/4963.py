## 4963 : https://www.acmicpc.net/problem/4963

from collections import deque


def bfs(i, j):
    global islands, cnt
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, -1, -1, -1, 0, 1, 1, 1]
    
    if islands[i][j] == 0:
        return
    else:
        islands[i][j] = 0
    q = deque([(i,j)])
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w or islands[nx][ny] == 0:
                continue
            islands[nx][ny] = 0
            q.append((nx, ny))
    cnt += 1

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    islands = []
    for i in range(h):
        islands.append(list(map(int, input().split())))

    cnt = 0
    for i in range(h):
        for j in range(w):
            bfs(i,j)
    print(cnt)