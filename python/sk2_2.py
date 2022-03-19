
from collections import deque


arr = ["1","2","4","3","3","4","1","5"]
processes = ["read 1 3 1 2",
"read 2 6 4 7",
"write 4 3 3 5 2",
"read 5 2 2 5",
"write 6 1 3 3 9",
"read 9 1 0 7"]

def solution(arr, processes):
    cnt = 0

    for i, p in enumerate(processes):
        t = p.split(" ")
        if len(t) == 5:
            processes[i] = [t[0], int(t[1]), int(t[2]), int(t[3]), int(t[4])]
            cnt += 1
        else:
            processes[i] = [t[0], int(t[1]), int(t[2]), int(t[3]), int(t[4]), t[5]]

    processes = deque(processes)
    active = []
    rq = deque()
    wq = deque()

    time = 1

    result = []

    while len(result) < cnt:
        deleter = []
        for p in processes:
            if p[1] <= time:
                if p[0] == "read":
                    rq.append(p)
                    deleter.append(processes.index(p))
                else:
                    wq.append(p)
                    deleter.append(processes.index(p))
        deleter.sort(reverse=False)
        for d in deleter:
            processes.remove(processes[d])
        time += 1

        if len(active) == 0:
            if wq:
                cur = wq.popleft()
                active.append(cur)
            else:
                while rq:
                    cur = rq.popleft()
                    active.append(cur)
        else:
            if active[0][0] == "read":
                if len(wq) == 0:
                    while rq:
                        cur = rq.popleft()
                        active.append(cur)

        flag = []
        for i in active:
            i[2] -= 1
            if i[2] == 0:
                if i[0] == "write":
                    for j in range(i[3], i[4]+1):
                        arr[j] = i[5]
                else:
                    tmp = ""
                    for k in range(i[3], i[4]+1):
                        tmp += arr[k]
                    result.append(tmp)
                flag.append(active.index(i))
        flag.sort(reverse=False)
        for f in flag:
            active.remove(active[f])

    result.append(time)

    return result

            

print(solution(arr, processes))