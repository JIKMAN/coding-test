## source : https://programmers.co.kr/learn/courses/30/lessons/49189?language=python3

n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

# graph = [[50001 for i in range(n)] for i in range(n)]

# for x,y in vertex:
#     graph[x-1][y-1] = 1
#     graph[y-1][x-1] = 1

# for k in range(n):
#     for i in range(n):
#         for j in range(n):
#             if graph[i][k] + graph[k][j] < graph[i][j]:
#                 graph[i][j] = graph[i][k] + graph[k][j]

# target = graph[0][1:]

# print(target.count(max(target)))

from collections import defaultdict, deque

distance = [50001] * (n+1)
distance[0] = 0
distance[1] = 0

graph = defaultdict(list)
for x,y in vertex:
    graph[x].append(y)
    graph[y].append(x)

visit = [False] * (n+1)
start = 1


q = deque([start])
while q:
    tmp = q.popleft()
    visit[tmp] = True
    for i in graph[tmp]:
        if visit[i] == False:
            q.append(i)
            distance[i] = min(distance[i], distance[tmp] + 1)
            visit[i] = True

max_v = max(distance)
print(distance.count(max_v))