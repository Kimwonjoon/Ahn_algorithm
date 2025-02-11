# 준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.

# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

import sys

input = sys.stdin.readline

ind, money = list(map(int, input().split()))
coins = []

for i in range(ind):
    coin = int(input())
    if coin <= money:
        coins.append(coin)
coins.sort(reverse=True)

result = 0

for j in coins:
    if money % j == 0: # 돈이 딱 맞는다면
        result += money // j
        break
    else:
        result += money // j
        money = money % j

print(result)