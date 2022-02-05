## 1629 :  https://www.acmicpc.net/problem/1629

def power(a, b):
    global C
    if b == 1:
        return a % C
    else:
        tmp = power(a, b // 2)
        if b % 2 == 0:
            return tmp * tmp % C
        else:
            return tmp * tmp * a % C

if __name__ == "__main__":
    A, B, C = map(int, input().split())

    res = power(A, B)
    print(res)
