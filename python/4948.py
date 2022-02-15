##  4948 : https://www.acmicpc.net/problem/4948

n = 123456 * 2 + 1

sosu = []

def prime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

for i in range(2, n):
    if prime(i) == True:
        sosu.append(i)

while True:
    r = int(input())
    if r == 0:
        break
    print(sum(map(lambda x: 1 if r < x <= 2 * r else 0, sosu)))