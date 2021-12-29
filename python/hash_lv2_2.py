## source : https://programmers.co.kr/learn/courses/30/lessons/42578?language=python3

from collections import Counter, defaultdict
from functools import reduce

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

## reduce 함수
def solution(clothes):
    dict = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x * (y+1), dict.values(), 1) - 1

    return answer

print(solution(clothes))

## 정석
def solution2(clothes):
    dict = defaultdict(int)
    for _, t in clothes:
        dict[t] += 1
    
    cnt = 1
    for v in dict.values():
        cnt *= (v+1)
    return cnt -1

print(solution2(clothes))