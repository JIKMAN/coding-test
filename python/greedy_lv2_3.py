## source : https://programmers.co.kr/learn/courses/30/lessons/42885?language=python3

people = [70, 50, 80, 50, 100, 10, 90]
limit = 100

def solution(people, limit):
    people.sort()
    cnt = 0
    i = 0
    j = len(people) - 1
    while i <= j:
        cnt += 1
        if people[j] + people[i] <= limit:
            i += 1
        j -=1
    return cnt
