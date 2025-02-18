# 6198

import sys

input = sys.stdin.readline
c = int(input())
buildings = [int(input()) for _ in range(c)] # 10 3 7 4 12 2

stack = []
result = 0
for i in buildings: # 10 / 3 / 7 / 4 / 12 / 2
    while stack and stack[-1] <= i: # / / 3 <= 7 / / 4 <= 12 / 7 <= 12 / 10 <= 12
        stack.pop() # / / 10 / / 10 7 / 10 / []
    stack.append(i) # 10 / 10 3 / 10 7 / 10 7 4 / 12 / 12 2
    result += len(stack) - 1 # 0 / 1 / 1 / 2 / 0 / 1 = 5
print(result)