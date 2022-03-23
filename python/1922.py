# https://www.acmicpc.net/problem/1922

n = int(input())
m = int(input())
network = []
for i in range(m):
    network.append(list(map(int, input().split())))

network.sort(key=lambda x: x[2])

group = set()

group.add(network[0][0])
group.add(network[0][1])

result = network[0][2]

while len(group) < n:
    for a, b, cost in network:
        if (a in group) and (b in group):
            continue
        elif (a in group) or (b in group):
            group.add(a)
            group.add(b)
            result += cost
            break

print(result)
        