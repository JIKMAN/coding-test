## 큐브 최단경로
'''
가로 1칸, 세로 1칸의 크기를 갖는 정사각형으로 이루어진 가로 width칸, 세로 height칸의 격자가 있습니다. 일부 정사각형에는 "왼쪽 위의 점과 오른쪽 아래점을 잇는" 대각선이 있습니다. 이 격자에서 다음 조건을 만족하는 경로의 개수를 구하고자 합니다.

좌측 하단의 끝점에서 우측 상단의 끝점으로 가는 경로입니다.
대각선을 정확히 1번 이용해야 합니다.
1, 2번 조건을 만족하는 전제 하에서 최단거리 경로여야 합니다.
격자의 가로 길이 width, 세로 길이 height, 대각선이 위치한 정사각형의 정보 diagonals가 매개변수로 주어집니다. 주어진 조건을 모두 만족하는 경로의 개수를
10,000,019로 나눈 나머지를 return 하도록 solution 함수를 완성해주세요.
'''

def route(h, w):
    cube = [[0] * w for i in range(h)]
    cube[h-1] = [1] * w
    for i in range(h-1):
        cube[i][0] = 1

    for n in range(h-2, -1, -1):
        for m in range(1, w):
            cube[n][m] = cube[n+1][m] + cube[n][m-1]
    
    return cube[0][w-1]

def solution(width, height, diagonals):
    result = 0
    for x, y in diagonals:
        re1 = route(x+1, y) * route(height+1 - y, width+1 - (x-1))
        re2 = route(x, y+1) * route(height+1 - (y-1), width+1 - x)
        result += re1
        result += re2
    return result


width, height = 51, 37
diagonals = [[17,19]]
print(solution(width, height, diagonals) % 10000019)
print(solution(2,2,[[1,1],[2,2]]))