# 10773

import sys

input = sys.stdin.readline
n = int(input())
li = []
for i in range(n):
    num = int(input())
    if num == 0:
        li.pop()
    else:
        li.append(num)

print(sum(li))