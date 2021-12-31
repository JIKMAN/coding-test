## source : https://programmers.co.kr/learn/courses/30/lessons/42586?language=python3

from collections import deque
from math import ceil

progresses = [93, 30, 55]
speeds = [1, 30, 5]

def solution(progresses, speeds):
    q = deque()
    for idx, p in enumerate(progresses):
        q.append((idx, p))

    cnt = 0
    work = ceil((100 - progresses[0]) / speeds[0])
    answer = []
    while q:
        idx, now = q.popleft()
        tmp = ceil((100 - now) / speeds[idx])
        if tmp > work:
            answer.append(cnt)
            work = tmp
            cnt = 1
        else:
            cnt += 1
        if not q:
            answer.append(cnt)

    return answer

print(solution(progresses, speeds))