# 2019 winter :https://programmers.co.kr/learn/courses/30/lessons/64062

def solution(stones, k):
    left = 1
    right = 200000000
    answer = 0

    while left <= right:
        cnt = 0
        mid = (left + right) // 2
        
        for s in stones:
            if s - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            
            if cnt >= k:
                break
        
        if cnt < k:
            left = mid + 1
        else:
            answer = mid
            right = mid - 1
    
    return answer