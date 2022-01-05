## source : https://programmers.co.kr/learn/courses/30/lessons/42747?language=python3

citations = [3, 0, 6, 1, 5]

def solution(citations):
    citations.sort(reverse=True)
    for idx , citation in enumerate(citations):
        if idx >= citation:
            return idx
    return len(citations)