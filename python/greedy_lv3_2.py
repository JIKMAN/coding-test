## source : https://programmers.co.kr/learn/courses/30/lessons/42884?language=python3

routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3], [-2, 1], [-1, 5], [0, 3], [2, 4]]

def solution(routes):
    routes.sort(key= lambda x: x[0], reverse=True)

    answer = 1
    end = routes[0][0]

    for r in routes:
        if r[1] >= end:
            continue
        else:
            answer += 1
            end = r[0]

    return answer

print(solution(routes))
            