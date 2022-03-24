research = ["yxxy","xxyyy"]
n = 2
k = 1

from collections import Counter

mini = 2 * n * k

name = {}
for i in range(len(research)):
    for j in list(research[i]):
        if j not in name:
            name[j] = [0 for _ in range(len(research))]
            name[j][i] += 1
        else:
            name[j][i] += 1



answer = []
for a in name:
    total = []
    for i in range(len(name[a]) - n+1):
        if sum(name[a][i:i+n]) < 2 * n * k:
            continue
        tmp = 0
        for j in range(i, len(name[a])):
            if name[a][j] >= k:
                tmp += 1
            else:
                break
        total.append(tmp)
    if total:
        answer.append((a, max(total)-1))
answer.sort(key= lambda x: (-x[1], x[0]))

print(name)
if answer:
    print(answer[0][0])
else:
    print('None')
