## source : https://programmers.co.kr/learn/courses/30/lessons/49191?language=python3

results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
n = 5

from collections import defaultdict

winner = defaultdict(set)
loser = defaultdict(set)

for w, l in results:
    winner[w].add(l)
    loser[l].add(w)


for i in range(1, n+1):
    for w in loser[i]:
        winner[w].update(winner[i])
    for l in winner[i]:
        loser[l].update(loser[i])

cnt = 0
for i in range(1, n+1):
    if len(winner[i]) + len(loser[i]) == n-1:
        cnt += 1
    
print(cnt)