## source : https://programmers.co.kr/learn/courses/30/lessons/42746?language=python3

numbers = [3, 30, 34, 5, 9]

def solution(numbers):
    answer = ""
    tmp = []
    sums = 0
    for num in numbers:
        c = (str(num) * 4)[:4]
        leng = len(str(num))
        tmp.append((c, leng))
    tmp.sort(reverse=True)
    for c, leng in tmp:
        sums += int(c)
        if sums == 0:
            return '0'
        answer += c[:leng]
    return answer
    
print(solution(numbers))

