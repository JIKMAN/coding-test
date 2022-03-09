## programmers 17678 : https://programmers.co.kr/learn/courses/30/lessons/17678

n, t, m = 1, 1, 5
timetable = ["00:01", "00:01", "00:01", "00:01", "00:01"]

def timeToNumber(time):
    num = int(time[0:2] + time[3:5])
    return num

def numberToTime(num):
    tmp = str(num)
    while len(tmp) < 4:
        tmp = "0" + tmp
    time = tmp[:-2] + ":" + tmp[-2:]
    return time
def solution(n, t, m, timetable):
    buses = {}
    start = 900
    for i in range(n):
        if i == 0:
            buses[start] = []
        else:
            if 60 <= (start % 100) + t < 100:
                start = start + t + 40
                buses[start] = []
            else:
                start = start + t
                buses[start] = []

    people = []
    for t in timetable:
        people.append(timeToNumber(t))

    for p in people:
        for k in buses.keys():
            if k < p:
                continue
            if len(buses[k]) < m:
                buses[k].append(p)
                break
            else:
                continue

    for k in buses.keys():
        buses[k].sort()

    bus_list = buses.keys()

    last_bus = list(buses.keys())

    if len(buses[last_bus[-1]]) == m:
        if buses[last_bus[-1]][-1] % 100 == 0:
            return numberToTime(buses[last_bus[-1]][-1] - 41)
        else:
            return numberToTime(buses[last_bus[-1]][-1] - 1)
    else:
        return numberToTime(last_bus[-1])