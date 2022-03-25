jobs = [[0, 5, 1, 1], [2, 4, 3, 3], [3, 4, 4, 5], [5, 2, 3, 2]]
# 요청시간, 걸리는 시간, 분류 번호, 중요도

import heapq
from collections import defaultdict, deque

importancy = defaultdict(int)

finished = 0
process = deque()
order = []
pretime = -1
time = 0
# while finished < len(jobs):
result = []
most = 0
while finished < len(jobs):
    for job in jobs:
        if pretime < job[0] <= time:
            process.append(job)
            importancy[job[2]] += job[3]
            order.append(job[2])
    pretime = time
    flag = True
    if process and most in order:
        for i in range(len(process)):
            p = process.popleft()
            if p[2] == most:
                time += p[1]
                importancy[p[2]] -= p[3]
                finished += 1
                order.remove(p[2])
                flag = False
                result.append(p[2])
                break
            else:
                process.append(p)
    
    if process and flag == True:
        most = []
        for k,v in importancy.items():
            if v == max(importancy.values()):
                most.append(k)
        most.sort()
        most = most[0]
        t = 0
        for i in range(len(process)):
            p = process.popleft()
            if p[2] == most:
                time += p[1]
                importancy[p[2]] -= p[3]
                finished += 1
                order.remove(p[2])
                result.append(p[2])
            else:
                process.append(p)
    else:
        time += 1

answer = [result[0]]

for i in range(1, len(result)):
    if result[i] != result[i-1]:
        answer.append(result[i])

print(answer)
