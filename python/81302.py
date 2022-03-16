## kakao 2021 internship : https://programmers.co.kr/learn/courses/30/lessons/81302?language=python3

from collections import deque

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]



def bfs(place):
    start = []
    
    for i in range(5):
        for j in range(5):
            if place[i][j] == "P":
                start.append([i, j])
    
    for s in start:
        q = deque([s])
        visit = [[False] * 5 for i in range(5)]
        dist = [[0] * 5 for i in range(5)]
        visit[s[0]][s[1]] = True

        while q:
            x, y = q.popleft()

            dx = [-1, 0, 1, 0]
            dy = [0, -1, 0, 1]

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < 5 and 0 <= ny < 5 and visit[nx][ny] == False:
                    if place[nx][ny] == 'O':
                        q.append([nx, ny])
                        visit[nx][ny] = True
                        dist[nx][ny] = dist[x][y] + 1

                    if place[nx][ny] == 'P' and dist[x][y] <= 1:
                        return 0
    return 1

def solution(places):
    answer = []

    for i in places:
        answer.append(bfs(i))
    
    return answer

print(solution(places))