## source : https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3

from collections import Counter

def solution(participant, completion):
    p = Counter(participant)
    c = Counter(completion)
    
    last = p - c
    
    return list(last.keys())[0]
