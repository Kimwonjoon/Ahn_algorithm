# 9375
import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    cnt = int(input())
    dic = {}

    for _ in range(cnt):
        wear_n, wear_t = input().strip().split()
        if wear_t in dic:
            dic[wear_t].append(wear_n)
        else:
            dic[wear_t] = [wear_n]

    result = 1

    for w in dic:
        result *= len(dic[w]) + 1
    print(result - 1)