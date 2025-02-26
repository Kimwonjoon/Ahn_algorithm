# 18258
from collections import deque
import sys
input = sys.stdin.readline
cnt = int(input())
q = deque()
for _ in range(cnt):
    ind = list(map(str,input().strip().split()))
    if ind[0] == "push":
        q.append(int(ind[1]))
    elif ind[0] == "pop":
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif ind[0] == "size":
        print(len(q))
    elif ind[0] == "empty":
        if q:
            print(0)
        else:
            print(1)
    elif ind[0] == "front":
        if q:
            print(q[0])
        else:
            print(-1)
    else:
        if q:
            print(q[-1])
        else:
            print(-1)