'''
자연수 n과 시계/반시계 방향을 결정하는 boolean 값 clockwise가 주어집니다. 입출력 예 설명의 그림과 같이 소용돌이 모양(clockwise가 참이면 시계방향, 거짓이면 반시계방향)으로 n x n 정수 배열을 채워 return 하도록 solution 함수를 완성해주세요.
n은 1 이상 1,000 이하입니다.
'''

import copy

def solution(n, clockwise):
    answer = [[0] * n for i in range(n)]
    start = (0, 0)

    if clockwise == True:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
    else:
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

    step = n-1
    now = 1

    max_val = 0
    for i in range(n-1, 0, -2):
        max_val += i
        if i == 2:
            max_val += 1

    direction = 0

    cnt = 0
    x, y = start
    while now <= max_val:
        answer[x][y] = now
        now += 1
        cnt += 1
        if cnt == step:
            cnt = 0
            step -= 2
            direction += 1

        x += dx[direction % 4]
        y += dy[direction % 4]

    def rotate(m):
        N = len(m)
        ret = [[0] * N for _ in range(N)]

        for r in range(N):
            for c in range(N):
                ret[c][N-1-r] = m[r][c]
        return ret

    tmp = copy.copy(answer)
    for i in range(3):
        tmp = rotate(tmp)
        
        for j in range(n):
            for k in range(n):
                if answer[j][k] == 0:
                    answer[j][k] = tmp[j][k]

    if n % 2 != 0:
        answer[n//2][n//2] = max_val

    for a in answer:
        print(a)

solution(7, True)