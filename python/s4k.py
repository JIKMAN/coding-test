'''
문제 설명
n개의 노드로 이루어진 트리가 있습니다. 각 노드에는 0번부터 n-1번까지 번호가 매겨져 있습니다. 이때, 당신은 다음 조건을 모두 만족하는 정수 순서쌍 (i,j,k)의 개수를 구하고자 합니다.

0 ≤ i, j, k < n
i, j, k는 서로 다릅니다.
distance(a, b)를 a번 노드와 b번 노드를 잇는 경로 상의 간선의 개수라고 할 때, distance(i, j) + distance(j, k) = distance(i, k)입니다.
트리의 노드 개수를 의미하는 n과 간선 정보가 담긴 2차원 정수 배열 edges가 매개변수로 주어집니다. 주어진 조건을 모두 만족하는 순서쌍 (i,j,k)의 개수를 return 하도록 solution 함수를 완성해주세요.

제한사항
3 ≤ n ≤ 300,000
edges의 행의 개수 = n - 1
edges의 각 행은 [v1,v2] 2개의 정수로 이루어져 있으며, 이는 v1번 노드와 v2번 노드 사이에 간선이 있음을 의미합니다.
0 ≤ v1 < n
0 ≤ v2 < n
v1 ≠ v2
edges가 의미하는 그래프가 항상 트리인 경우만 입력으로 주어집니다.
'''
from collections import defaultdict

def dijkstra(start, end, con, n):
    distance = [300001] * (n+1)
    h = [start]
    distance[start] = 0
    visit = [False] * (n+1)
    visit[start] = True

    while h:
        cur = h.pop()
        if cur in con:
            for v in con[cur]:
                if visit[v[0]] == False:
                    h.append(v[0])
                    visit[v[0]] = True
                    distance[v[0]] = min(distance[v[0]], distance[cur]+v[1])

    return distance[end]

def solution(n, edges):

    con = defaultdict(list)

    for a, b in edges:
        con[a].append((b,1))
        con[b].append((a,1))

    result = 0
    for i in range(n):
        for j in range(n):
            tmp = dijkstra(i, j, con, n)
            if tmp >= 2:
                result += (tmp - 1)

    return result

n = 5
edges = [[2,3],[0,1],[1,2]]
print(solution(5, [[0,1],[0,2],[1,3],[1,4]]))