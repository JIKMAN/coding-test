## source : https://programmers.co.kr/learn/courses/30/lessons/42579?language=python3

from collections import defaultdict
import heapq

def solution2(genres, plays):
    count = defaultdict(int)

    type = defaultdict(list)

    for i in range(len(genres)):
        heapq.heappush(type[genres[i]], (-plays[i], i))
        count[genres[i]] += plays[i]

    items = list(count.items())
    items.sort(key= lambda x: x[1])

    answer = []
    while items:
        name = items.pop()[0]
        if type[name]:
            answer.append(heapq.heappop(type[name])[1])
        if type[name]:
            answer.append(heapq.heappop(type[name])[1])

    return answer

