## sourece : https://programmers.co.kr/learn/courses/30/lessons/42584?language=python3

from collections import deque

prices = [1, 2, 3, 2, 3]

def solution(prices):
    queue = deque(prices)
    answer = []

    while queue:
        tmp = queue.popleft()
        time = 0
        for i in queue:
            time += 1
            if tmp > i:
                break
        answer.append(time)

    return answer

print(solution(prices))