# 1927
import sys
import heapq

input = sys.stdin.readline
n = int(input())

h = []

for _ in range(n):
    num = int(input())

    if num == 0:
        if not h:
            print(0)
            continue
        else:
            min_num = heapq.heappop(h)
            print(min_num)
    else:
        heapq.heappush(h, num)