'''
6종류(1원, 5원, 10원, 50원, 100원, 500원)의 동전을 생산하는 공장이 있습니다. 특정 금액만큼 동전을 생산해달라는 의뢰가 들어왔을 때, 최소 비용으로 그 금액만큼 동전을 생산하고자 합니다.
만약 각 동전의 생산 단가가 위의 표와 같고, 의뢰받은 금액이 4578원이라면, 최소의 비용으로 4578원어치의 동전을 생산하는 방법은 다음과 같습니다.
즉, 1원짜리 동전을 3개, 5원짜리 동전을 5개, 50원짜리 동전을 1개, 100원짜리 동전을 45개 생산하면 2308원이라는 최소 비용으로 4578원어치의 동전을 생산할 수 있습니다. 2308원보다 적은 비용으로 4578원어치의 동전을 생산할 수 있는 방법은 없습니다.

공장이 생산해야 하는 금액을 나타내는 정수 money, 6종류 동전의 생산 단가를 나타내는 1차원 정수 배열 costs가 매개변수로 주어집니다. money원만큼의 동전을 최소 비용으로 생산했을 때, 그 최소 비용을 return 하도록 solution 함수를 완성해주세요.
제한사항
1 ≤ money ≤ 1,000,000
costs의 길이 = 6
1 ≤ costs의 원소 ≤ 5,000
costs[0] ~ costs[5]은 차례대로 1원, 5원, 10원, 50원, 100원, 500원짜리 동전의 생산 단가를 담고 있습니다.
'''

'''
4578	[1, 4, 99, 35, 50, 1000]	2308
1999	[2, 11, 20, 100, 200, 600]	2798
'''

## 동전 종류를 담은 리스트 coins []
coins = [1, 5, 10, 50, 100, 500]

## 동전을 만드는데 드는 금액을 담은 리스트 costs []
costs = [1, 4, 99, 35, 50, 1000]

## 동전의 가치가 높은 순서를 담는 배열 value []
value = []
## 1. 모든 동전의 가치를 500원으로 환산
## 모든 동전을 500원으로 맞춰줌
# value [] = costs * [500, 100, 50, 10, 5, 1]
value = [500, 100, 50, 10, 5, 1]
for i in range(len(costs)):
    value[i] = (value[i] * costs[i], coins[i], costs[i])
value = [(i[1], i[2]) for i in sorted(value, key= lambda x: (x[0], -x[1]))]

## 만들어야하는 금액의 크기
money = 4578

def solution(money, costs):
    value = [500, 100, 50, 10, 5, 1]
    for i in range(len(costs)):
        value[i] = (value[i] * costs[i], coins[i], costs[i])
    value = [(i[1], i[2]) for i in sorted(value, key= lambda x: (x[0], -x[1]))]
    print(value)

    result = 0
    for i in range(len(value)):
        tmp = (money // value[i][0])
        money -= (value[i][0] * tmp)
        result += (value[i][1] * tmp)
        if money == 0:
            return result


money = 1999
costs =	[2, 11, 20, 100, 200, 600]
print(solution(money, costs))