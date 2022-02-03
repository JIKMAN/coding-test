## baekjoon 1254 : https://www.acmicpc.net/problem/1254

## pivot
def pivot(words):
    start = len(words) // 2

    for i in range(start, len(words)):
        p1 = words[:i]
        p2 = words[i+1:]
        if p1[::-1].startswith(p2):
            return len(p1) * 2 + 1
    return False


def fold(words):
    start = len(words) // 2

    for i in range(start, len(words)):
        p1 = words[:i]
        p2 = words[i:]
        if p1[::-1].startswith(p2):
            return len(p1) * 2
    return False

word = input()

if fold(word) == False:
    print(pivot(word))
else:
    print(min(pivot(word), fold(word)))