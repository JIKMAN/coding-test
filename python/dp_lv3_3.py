## source : https://programmers.co.kr/learn/courses/30/lessons/42898?language=python3

m, n = 4, 3
puddles = [[2,2]]


def solution(m, n, puddles):
    map = [[0 for _ in range(m+1)] for _ in range(n+1)]
    map[1][1] = 1

    for a, b in puddles:
        map[b][a] = -1

    for i in range(1, len(map)):
        for j in range(1, len(map[0])):
            if map[i][j] == -1:
                map[i][j] = 0
                continue
            map[i][j] += (map[i][j-1] + map[i-1][j])

    return map[n][m] % 1000000007

print(solution(4,3,puddles))