## 2156 : https://www.acmicpc.net/problem/2156

if __name__ == "__main__":
    n = int(input())

    wine = [0] + [int(input()) for _ in range(n)] + [0]

    dp = [0] * (n + 2)
    dp[1] = wine[1]
    dp[2] = dp[1] + wine[2]

    for i in range(3, n+1):
        dp[i] = max(dp[i-3] + wine[i-1] + wine[i], dp[i-2] + wine[i], dp[i-1])

    print(dp[n])