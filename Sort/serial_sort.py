# 1431
import sys
input = sys.stdin.readline
n = int(input())

li = [input().strip() for _ in range(n)]

for i in range(len(li)):
    num = 0
    for j in li[i]:
        if j.isdigit():
            num += int(j)
    li[i] = (num, li[i])
li.sort(key=lambda x: (len(x[1]), x[0], x[1]))

for k in li:
    print(k[1])