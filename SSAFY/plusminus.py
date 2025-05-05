# 21425. +=
import sys

input = sys.stdin.readline

ind = int(input())

for _ in range(ind):
    result = 0
    a,b,n = map(int,input().split())

    while (a <= n) and (b <= n):
        if a > b:
            b += a
        else:
            a += b
        result += 1
    print(result)