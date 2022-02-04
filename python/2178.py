## backjun 2178 : https://www.acmicpc.net/problem/2178

from collections import deque

n, m = map(int, input().split())
INF = n * m

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

def shortcut():
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    q = deque([(0, 0)])
    while q:
        x, y = q.popleft()

        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == '0':
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
                
    return graph[n-1][m-1]

print(shortcut())