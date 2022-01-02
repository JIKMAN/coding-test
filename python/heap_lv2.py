## source : https://programmers.co.kr/learn/courses/30/lessons/42626?language=python3

scoville = [1, 2, 3, 9, 10, 12]
K = 7

import heapq

def solution(scoville, K):
    answer = 0
    scoville.sort()
    while scoville[0] < K:
        if len(scoville) <= 1:
            return -1
        else:
            small = heapq.heappop(scoville)
            small2 = heapq.heappop(scoville)
            heapq.heappush(scoville, (small + (small2 * 2)))
            answer += 1
    return answer