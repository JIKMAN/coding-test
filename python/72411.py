## https://programmers.co.kr/learn/courses/30/lessons/72411?language=python3

from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    count = [defaultdict(int) for i in range(len(course))]

    for order in orders:
        for i, c in enumerate(course):
            comb = list(combinations(order, c))

            for j in comb:
                tmp = ''.join(sorted(j))
                count[i][tmp] += 1
    result = []
    for dic in count:
        if len(dic) == 0:
            continue
        if max(dic.values()) <= 1:
            continue 
        result += [k for k, v in dic.items() if max(dic.values()) == v]

    return sorted(result)

orders =["XYZ", "XWY", "WXA"]
course = [2,3,4]

print(solution(orders, course))