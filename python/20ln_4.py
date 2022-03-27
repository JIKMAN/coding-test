from collections import defaultdict

def check_nick(e1, n2):
    if e1 == n2:
        return True
    
    for n in range(1,3):
        for i in range(len(e1)-(n-1)):
            tmp = e1[:i] + e1[i+n:]
            if tmp == n2:
                return True
    for n in range(1,3):
        for i in range(len(n2)-(n-1)):
            tmp = n2[:i] + n2[i+n:]
            if tmp == e1:
                return True
    
    dic = defaultdict(list)
    for x in [e1, n2]:
        for i in range(len(x)):
            tmp = x[:i] + x[i+1:]
            dic[x].append(tmp)
    for a in dic[e1]:
        for b in dic[n2]:
            if a == b:
                return True
    return False



def check_email(e1, e2):
    e1, e1_addr = e1.split('@')[0], e1.split('@')[1]
    e2, e2_addr = e2.split('@')[0], e2.split('@')[1]

    if e1 == e2:
        return True

    if e1_addr == e2_addr:
        for i in range(len(e1)):
            tmp = e1[:i] + e1[i+1:]
            if tmp == e2:
                return True
        for i in range(len(e2)):
            tmp = e2[:i] + e2[i+1:]
            if tmp == e1:
                return True
    return False

def solution(nicks, emails):
    name = defaultdict(int)

    for i in range(len(nicks)-1):
        for j in range(i+1, len(nicks)):
            if check_nick(nicks[i], nicks[j]) and check_email(emails[i], emails[j]):
                name[i] += 1

    v_sum = sum(v for v in name.values())
    return len(nicks) - v_sum


nicks = ["imhero111", "moneyman", "hero111", "imher1111", "hro111", "mmoneyman", "moneymannnn"]
emails = ["superman5@abcd.com", "batman432@korea.co.kr", "superman@abcd.com", "supertman5@abcd.com", "superman@erty.net", "batman42@korea.co.kr", "batman432@usa.com"]
print(solution(nicks, emails))

nicks = ["99police", "99poli44"]
emails = ["687ufq687@aaa.xx.yyy", "87ufq687@aaa.xx.yyy"]
print(solution(nicks, emails))

nicks = ["99polico", "99policd"]
emails = ["687ufq687@aaa.xx.yyy", "587ufq687@aaa.xx.yyy"]
print(solution(nicks, emails))


