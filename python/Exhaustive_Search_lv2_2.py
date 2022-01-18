## source : https://programmers.co.kr/learn/courses/30/lessons/42842?language=python3

brown = 24
yellow = 24

def solution(brown, yellow):
    for i in range(1, yellow + 1):
        if i * (yellow // i) == yellow:
            if i + (yellow // i) + 2 == brown // 2:
                return [yellow // i + 2, i + 2]
                

print(solution(brown, yellow))
