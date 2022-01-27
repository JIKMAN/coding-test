## source : https://leetcode.com/problems/sequential-digits/

low = 1000
high = 13000

s = len(str(low))
e = len(str(high))

output = []

while s <= e:
    for i in range(1, 11 - s):
        cnt = s
        tmp = ''
        now = i
        while cnt != 0:
            tmp += str(now)
            cnt -= 1
            now += 1
        if int(tmp) >= low and int(tmp) <= high:
            output.append(tmp)
    s += 1

print(output)
        