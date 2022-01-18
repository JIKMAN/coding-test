## source : https://programmers.co.kr/learn/courses/30/lessons/42839?language=python3

from itertools import permutations

def solution(numbers):
    lit = list(numbers)

    per = []

    for i in range(1, len(lit)+1):
        per += list(permutations(lit, i))

    combination = []
    for i in per:
        tmp = int("".join(i))
        if tmp not in combination:
            combination.append(tmp)

    def decimal(num):
        if num == 1 or num == 0:
            return False
        for i in range(2, int(num / 2) + 1):
            if num % i == 0:
                return False

        return True

    answer = 0
    for c in combination:
        if decimal(c) == True:
            answer += 1
    return answer

numbers = "011"

print(solution(numbers))