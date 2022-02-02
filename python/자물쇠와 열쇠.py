## source : https://programmers.co.kr/learn/courses/30/lessons/60059

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

map = [[0 for _ in range((len(lock) - 1) * 2 + len(key))] for _ in range((len(lock) - 1) * 2 + len(key))]

def turn(key): return list(zip(*key[::-1]))

def unlock(array):
    for i in range(len(lock) - 1, len(lock) + len(key) - 1):
        for j in range(len(lock) - 1, len(lock) + len(key) - 1):
            if array[i][j] == 0:
                return False
    return True

for i in range(len(lock) - 1, len(lock) + len(key) - 1):
    for j in range(len(lock) - 1, len(lock) + len(key) - 1):
        map[i][j] = lock[i-(len(lock) - 1)][j-(len(lock) - 1)]


for i in range(len(key) + len(lock)):
    for j in range(len(key) + len(lock)):
        for k in range(4):
            tmp = map
            for x in range(0, len(lock)):
                for y in range(0, len(lock)):
                    if tmp[i][j] == lock[x][y] == 1:
                        break
                    tmp[i][j] = lock[x][y]
            if unlock(tmp) == True:
                print(True)
            else:
                key = turn(key)
