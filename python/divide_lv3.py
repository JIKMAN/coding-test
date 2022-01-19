## source : https://programmers.co.kr/learn/courses/30/lessons/43238?language=python3

n = 6
times = [7, 10]

def solution(n, times):
    right = max(times) * n
    left = 1
    
    while left < right:
        mid = (left + right) // 2
        total = 0
        for time in times:
            total += mid // time
        if total >= n:
            right = mid
        else:
            left = mid + 1
    return left
