## source : https://programmers.co.kr/learn/courses/30/lessons/43162?language=python3

n=3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

def solution(n, computers):
    visit = [False] * n
    answer = 0

    for i in range(len(computers)):
        q = []
        if visit[i] == 0:
            q.append(i)
        else:
            continue
        while q:
            tmp = q.pop()
            visit[tmp] = True
            for j in range(n):
                if computers[tmp][j] == 1 and visit[j] == False:
                    q.append(j)
                    visit[j] = True
        answer += 1

    return answer

print(solution(n, computers))