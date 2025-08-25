# 11399

import sys

input = sys.stdin.readline

cnt = int(input())

line = sorted(list(map(int,input().split())))

result = 0

for i in range(cnt):
    result += sum(line[:i+1])

print(result)