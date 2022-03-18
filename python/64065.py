## https://programmers.co.kr/learn/courses/30/lessons/64065?language=python3

import re
from collections import Counter

s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"

def solution(s):
    exp = re.findall('\d+', s)
    orders = Counter(exp)
    result = list(map(int, [k for k, v in sorted(orders.items(), key= lambda x: x[1], reverse=True)]))
    return result

print(solution(s))