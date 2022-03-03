# 11399 : https://www.acmicpc.net/problem/11399

N = int(input())
people = list(map(int, input().split()))

people.sort()

result = 0
for i in range(N):
    result += (people[i] * (N - i))

print(result)