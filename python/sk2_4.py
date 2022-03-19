from itertools import combinations
from collections import defaultdict

n = 8 # 패드 길이
m = 4 # 정수 범위 (1 ~ m)
k = 4 # 비밀번호 길이
records = [[1, 5, 1, 3], [5, 7, 5, 6]]

def solution(n, m, k, records):
    keys = defaultdict(int)
    num = [i for i in range(1, m+1)]
    for record in records:
        botton = len(set(record))

        # 누른 배열 길이
        leng = max(record) - min(record) + 1

        if leng < m:

            arr = []

            for i in range(1, m - leng + 2):
                tmp = []
                for j in range(i, i + leng):
                    tmp.append(j)
                arr.append(tmp)
            
            for a in arr:
                if 1 in record:
                    if 1 not in a:
                        continue
                    comb = list(combinations(a[1:], botton-1))
                    ordered = sorted(list(set(record)))
                    res = []
                    for c in comb:
                        result = ""
                        pad = [0 for j in range(n+1)]
                        pad[1]= 1
                        for i in range(len(c)):    
                            pad[ordered[i+1]] = c[i]

                        for r in record:
                            result += ("," + str(pad[r]))
                        res.append(result)
                    for r in res:
                        keys[r] += 1


                if n in record:
                    if n not in a:
                        continue
                    comb = list(combinations(a[:-1], botton-1))
                    ordered = sorted(list(set(record)))
                    res = []
                    for c in comb:
                        result = ""
                        pad = [0 for j in range(n+1)]
                        pad[n]= m
                        for i in range(len(c)):    
                            pad[ordered[i]] = c[i]

                        for r in record:
                            result += ("," + str(pad[r]))
                        res.append(result)
                    for r in res:
                        keys[r] += 1

                comb = list(combinations(a, botton))
                ordered = sorted(list(set(record)))
                res = []
                for c in comb:
                    result = ""
                    pad = [0 for j in range(n+1)]
                    for i in range(len(c)):
                        pad[ordered[i]] = c[i]
                    for r in record:
                        result += ("," + str(pad[r]))
                    res.append(result)
                for r in res:
                    keys[r] += 1

        else:
            if 1 in record:
                comb = list(combinations(num[1:], botton-1))
                ordered = sorted(list(set(record)))
                res = []
                for c in comb:
                    result = ""
                    pad = [0 for j in range(n+1)]
                    pad[1]= 1
                    for i in range(len(c)):    
                        pad[ordered[i+1]] = c[i]

                    for r in record:
                        result += ("," + str(pad[r]))
                    res.append(result)
                for r in res:
                    keys[r] += 1


            if n in record:
                comb = list(combinations(num[:-1], botton-1))
                ordered = sorted(list(set(record)))
                res = []
                for c in comb:
                    result = ""
                    pad = [0 for j in range(n+1)]
                    pad[n]= m
                    for i in range(len(c)):    
                        pad[ordered[i]] = c[i]
                    for r in record:
                        result += ("," + str(pad[r]))
                    res.append(result)
                for r in res:
                    keys[r] += 1
            
            comb = list(combinations(num, botton))
            ordered = sorted(list(set(record)))
            res = []
            for c in comb:
                result = ""
                pad = [0 for j in range(n+1)]
                for i in range(len(c)):
                    pad[ordered[i]] = c[i]
                for r in record:
                    result += ("," + str(pad[r]))
                res.append(result)
            
            for r in res:
                keys[r] += 1

    final = []
    for k, v in keys.items():
        if v == max(keys.values()):
            tmp = k[1:].split(",")
            final.append(''.join(tmp))
    final.sort()
    return list(map(int, list(final[-1])))

print(solution(n, m, k, records))

