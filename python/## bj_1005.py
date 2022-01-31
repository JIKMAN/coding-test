## bj_1005
## source : https://www.acmicpc.net/problem/1005

from collections import defaultdict, deque


# n, k = map(int, input().split())
n, k = 4, 4
# cost = list(map(int, input().split()))
cost = [10, 1, 100, 10]
# end = int(input())
end = 4
building = [(1,2), (1,3), (2,4), (3,4)]

dp = [0] * (n + 1)
ingreed = [0] * (n + 1)

con = defaultdict(list)
# for _ in k:
#     tmp = tuple(map(int, input().split()))
#     con[tmp[0]].append(tmp[1])
#     ingreed[tmp[1]] += 1

for i in building:
    con[i[0]].append(i[1])
    ingreed[i[1]] += 1

q = deque()
for i in range(1, n + 1):
    if ingreed[i] == 0:
        q.append(i)
        dp[i] = cost[i-1]

while q:
    cur = q.popleft()
    for i in con[cur]:
        ingreed[i] -= 1
        dp[i] = max(dp[i], dp[cur] + cost[i-1])
        if ingreed[i] == 0:
            q.append(i)

print(dp[end])