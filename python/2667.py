# 2667 : https://www.acmicpc.net/problem/2667

from collections import deque

N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))

result = 0
cnt_total = []

def bfs(i, j):
    if graph[i][j] == 0:
        return False
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    q = deque([(i, j)])
    graph[i][j] = 0
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
                cnt += 1
                graph[nx][ny] = 0
                q.append((nx, ny))
    cnt_total.append(cnt)
    return True

for i in range(N):
    for j in range(N):
        if bfs(i, j) == True:
            result += 1
cnt_total.sort()
print(result)
for i in range(len(cnt_total)):
    print(cnt_total[i])