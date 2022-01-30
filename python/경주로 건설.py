from collections import deque
import math

def solution(board):
    
    def bfs(start):    

        table = [[math.inf for _ in range(len(board))] for _ in range(len(board))]
        table[0][0] = 0

        q = deque([start])

        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]

        while q:
            x, y, dir, cost = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                n_cost = cost + 600 if i != dir else cost + 100
                if 0 <= ny < len(board) and 0 <= nx < len(board) and board[nx][ny] == 0 and table[nx][ny] > n_cost:
                    table[nx][ny] = n_cost
                    q.append((nx, ny, i, n_cost)) 

        return table[-1][-1]
    
    return min(bfs((0,0,2,0)), bfs((0,0,3,0)))

board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
print(solution(board))