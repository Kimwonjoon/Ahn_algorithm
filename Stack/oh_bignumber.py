# 17298

import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int,input().split()))

stack = [0]
result = [-1] * n

for i in range(1,n):
    while stack and nums[stack[-1]] < nums[i]:
        result[stack.pop()] = nums[i]
    stack.append(i)
print(*result)