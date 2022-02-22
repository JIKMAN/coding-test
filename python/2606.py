# 2606 : https://www.acmicpc.net/problem/2606

from collections import deque, defaultdict

n = int(input())
c = int(input())

connect = defaultdict(list)
for i in range(c):
    v, k = map(int, input().split())
    connect[v].append(k)
    connect[k].append(v)

visit = [False] * (n+1)
visit[1] = True

result = 0
q = deque([1])
while q:
    cur = q.popleft()
    for i in range(1, n + 1):
        if visit[i] == False and i in connect[cur]:
            q.append(i)
            result += 1
            visit[i] = True

print(result)
