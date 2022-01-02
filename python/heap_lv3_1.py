## source : https://programmers.co.kr/learn/courses/30/lessons/42627?language=python3

from collections import deque
import heapq

jobs = [[0, 3], [1, 9], [2, 6]]

def solution(jobs):
    answer = 0
    time = 0
    start = -1
    count = 0
    h = []
    while count < len(jobs):
        for job in jobs:
            if start < job[0] <= time:
                heapq.heappush(h, [job[1], job[0]])
                
        if h:
            cur = heapq.heappop(h)        
            start = time
            time += cur[0]
            answer += (time - cur[1])
            count += 1
        else:
            time += 1

    return int(answer / len(jobs))