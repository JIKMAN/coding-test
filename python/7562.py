# 7562 : https://www.acmicpc.net/problem/7562

from collections import deque
import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    
    n = int(input())
    start = tuple(map(int, input().split()))
    finish = tuple(map(int, input().split()))

    board = [[0] * n for i in range(n)]
    board[start[0]][start[1]] = 1

    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [-1, -2, -2, -1, 1, 2, 2, 1]


    q = deque([start])

    while q:
        x, y = q.popleft()
        if (x, y) == finish:
            print(board[x][y] -1)
            break
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                q.append((nx, ny))
                board[nx][ny] = board[x][y] + 1