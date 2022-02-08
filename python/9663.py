## baekjoon 9663 : https://www.acmicpc.net/problem/9663



def check(x):
    for i in range(x):
        if col[x] == col[i] or abs(col[i] - col[x]) == x - i:
            return False
    return True


def dfs(x):
    global cnt
    if x == n:
        cnt += 1
        return
    for i in range(n):
        col[x] = i
        if check(x):
            dfs(x+1)

n = int(input())
col = [0] * n
cnt = 0

dfs(0)
print(cnt)