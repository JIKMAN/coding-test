## source : https://programmers.co.kr/learn/courses/30/lessons/42883?language=python3


number = "4177252841"
k = 4

def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    
    if k != 0:
        stack = stack[:-k]
    return "".join(stack)

print(solution(number, k))