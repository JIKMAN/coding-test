## source : https://programmers.co.kr/learn/courses/30/lessons/43164?language=python3

from collections import defaultdict, deque

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
tickets.sort(key= lambda x: x[1])

depart = defaultdict(deque)

for t in tickets:
    depart[t[0]].append(t[1])

start = "ICN"

q = deque([start])

while q:
    cur = q.popleft()
    if depart[cur]:
        next = depart[cur].popleft()
    else:
        q.append(cur)
        continue
        

