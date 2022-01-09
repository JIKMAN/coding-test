## source : https://programmers.co.kr/learn/courses/30/lessons/42840?language=python3

"""
1st_cheat : 1,2,3,4,5 ... (5)
2nd_cheat : 2,1,2,3,2,4,2,5, ... (8)
3rd_cheat : 3,3,1,1,2,2,4,4,5,5, ... (10)
"""

answer = [1,3,2,4,2]

def solution(answer):
    cheat_1st = [1,2,3,4,5]
    cheat_2nd = [2,1,2,3,2,4,2,5]
    cheat_3rd = [3,3,1,1,2,2,4,4,5,5]

    score = [0, 0, 0]
    for i in range(len(answer)):
        if answer[i] == cheat_1st[i % len(cheat_1st)]:
            score[0] += 1
        if answer[i] == cheat_2nd[i % len(cheat_2nd)]:
            score[1] += 1
        if answer[i] == cheat_3rd[i % len(cheat_3rd)]:
            score[2] += 1
    result = []
    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx + 1)
    result.sort()

    return result