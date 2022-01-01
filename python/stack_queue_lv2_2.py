## source : https://programmers.co.kr/learn/courses/30/lessons/42587?language=python3

from collections import deque

priorities = [2, 1, 3, 2]
location = 2

def solution(priorities, location):
    printer = deque()
    for idx, p in enumerate(priorities):
        printer.append((idx, p))

    cnt = 0

    while printer:
        max_v = max(i[1] for i in printer)
        tmp = printer.popleft()
        
        if tmp[1] == max_v:
            cnt += 1
            if tmp[0] == location:
                return cnt
        else:
            printer.append(tmp)
