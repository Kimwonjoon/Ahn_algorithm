# 7785
import sys

input = sys.stdin.readline

n = int(input())

dic = {}

for i in range(n):
    name, c = input().split()

    if name in dic:
        del dic[name]
    else:
        dic[name] = c

result = sorted(dic.keys(), reverse=True)
print(*result)