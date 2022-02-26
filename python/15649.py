# 15649 : https://www.acmicpc.net/problem/15649

from itertools import permutations

N, M = map(int, input().split())

num = []

for i in range(1, N + 1):
    num.append(i)

result = permutations(num, M)

for r in result:
    print(' '.join(map(str, r)))