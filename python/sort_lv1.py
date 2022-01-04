## source : https://programmers.co.kr/learn/courses/30/lessons/42748?language=python3

array = [1, 5, 2, 6, 3, 7, 4]
commands = 	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array, commands):
    answer = []
    
    for c in commands:
        start = c[0]
        end = c[1]
        pick = c[2]

        tmp = array[start-1:end]
        tmp.sort()
        answer.append(tmp[pick-1])
    return answer

print(solution(array,commands))