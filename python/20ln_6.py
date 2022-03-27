from collections import defaultdict

def date_cal(date1, date2):
    d1 = int(date1.split("-")[1]) * 30 + int(date1.split("-")[2])
    d2 = int(date2.split("-")[1]) * 30 + int(date2.split("-")[2])
    if 0 <= d1 - d2 < k:
        return True
    return False

def solution(records, k, date):
    order = defaultdict(dict)
    valid = []
    for r in records:
        tmp = r.split(" ")
        if date_cal(date, tmp[0]) == True:
            valid.append((tmp[1], tmp[2]))

    for uid, pid in valid:
        if uid not in order[pid]:
            order[pid][uid] = 1
        else:
            order[pid][uid] += 1

    result = []
    for p in order:
        sums = 0
        many = 0
        reor = 0
        for k, v in order[p].items():
            sums += v
            many += 1
            if v >= 2:
                reor += 1
        result.append((p, reor/many, sums))

    result.sort(key= lambda x: (-x[1], -x[2], int(x[0][3:])))

    if len(result) == 0:
        return ["no result"]
    else:
        return [r[0] for r in result]

records = ["2020-02-02 uid1 pid1", "2020-02-26 uid1 pid1", "2020-02-26 uid2 pid1", "2020-02-27 uid3 pid2", "2020-02-28 uid4 pid2", "2020-02-29 uid3 pid3", "2020-03-01 uid4 pid3", "2020-03-03 uid1 pid1", "2020-03-04 uid2 pid1", "2020-03-05 uid3 pid2", "2020-03-05 uid3 pid3", "2020-03-05 uid3 pid3", "2020-03-06 uid1 pid4"]
k = 10
date = "2020-03-05"
print(solution(records, k, date))

records = ["2020-02-02 uid141 pid141", "2020-02-03 uid141 pid32", "2020-02-04 uid32 pid32", "2020-02-05 uid32 pid141"]
k = 10
date = "2020-02-05"
print(solution(records, k, date))

records = records = ["2020-02-02 uid141 pid141", "2020-02-03 uid141 pid32", "2020-02-04 uid32 pid32", "2020-02-05 uid32 pid141"]
k = 10
date = "2020-01-11"
print(solution(records, k, date))