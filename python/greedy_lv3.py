## source : https://programmers.co.kr/learn/courses/30/lessons/42861?language=python3

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

def solution(n, costs):
    answer = 0
    costs.sort(key= lambda x: x[2])
    connect = set([costs[0][0]])

    while len(connect) != n:
        for cost in costs:
            if cost[0] in connect and  cost[1] in connect:
                continue
            if cost[0] in connect or cost[1] in connect:
                connect.update([cost[0], cost[1]])
                answer += cost[2]
                break
    return answer