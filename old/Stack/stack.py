# 10828

import sys

input = sys.stdin.readline

cnt = int(input())

s = []

for i in range(cnt):
    ind = list(map(str, input().strip().split()))
    if ind[0] == "push":
        s.append(int(ind[1]))
    elif ind[0] == "pop":
        if s:
            print(s.pop())
        else:
            print(-1)
    elif ind[0] == "size":
        print(len(s))
    elif ind[0] == "empty":
        if s:
            print(0)
        else:
            print(1)
    else:
        if s:
            print(s[-1])
        else:
            print(-1)