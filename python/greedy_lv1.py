## source : https://programmers.co.kr/learn/courses/30/lessons/42862?language=python3

n = 5
lost = [1, 4]
reserve = [3, 5]

def solution(n, lost, reserve):
    student = [1 for i in range(n)]

    for i in lost:
        student[i-1] -= 1
    for i in reserve:
        student[i-1] += 1

    for i in range(1, n+1):
        if student[i-1] == 0:
            if i == 1:
                if student[i] >= 2:
                    student[i] -= 1
                    student[i-1] += 1
            elif i == n:
                if student[i-2] >= 2:
                    student[i-2] -= 1
                    student[i-1] += 1
            else:    
                if student[i-2] >= 2:
                    student[i-2] -= 1
                    student[i-1] += 1
                elif student[i] >= 2:
                    student[i] -= 1
                    student[i-1] += 1

    return sum(i > 0 for i in student)

print(solution(n, lost, reserve))