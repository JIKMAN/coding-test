## source : https://programmers.co.kr/learn/courses/30/lessons/42628?language=python3

operations = ["I 7","I 5","I -5","D -1"]

import heapq

def solution(operations):
    h = []
    max_h = []

    for op in operations:
        if op[0] == 'I':
            num = int(op[2:])
            heapq.heappush(h, num)
            heapq.heappush(max_h, (-num, num))
        else:
            if len(h) == 0:
                continue
            elif op == 'D 1':
                max_v = heapq.heappop(max_h)[1]
                h.remove(max_v)
            elif op == 'D -1':
                min_v = heapq.heappop(h)
                max_h.remove((-min_v, min_v))
    
    if h:
        return [heapq.heappop(max_h)[1], heapq.heappop(h)]
    else:
        return [0, 0]



