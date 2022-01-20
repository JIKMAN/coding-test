## source : https://programmers.co.kr/learn/courses/30/lessons/43165?language=python3

numbers	= [1, 1, 1, 1, 1]
target = 3

def solution(numbers, target):
    comb = []

    comb.append(numbers[0])
    comb.append(-numbers[0])

    for i in range(1, len(numbers)):
        tmp = []
        while comb:
            num = comb.pop()
            tmp.append(num + numbers[i])
            tmp.append(num - numbers[i])
        comb = tmp

    return comb.count(target)

## 다른풀이

from itertools import product

def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)