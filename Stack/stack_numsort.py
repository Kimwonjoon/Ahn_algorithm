# 1874

import sys
input = sys.stdin.readline
cnt = int(input())
stack = []
answer = []
now = 1
sign = True

for i in range(cnt):
    num = int(input())

    while now <= num: # 4면은 1 2 3 4
        stack.append(now)
        now += 1
        answer.append("+")

    if stack[-1] == num:
        stack.pop()
        answer.append("-")
    else:
        sign = False
        break

if not sign:
    print("NO")
else:
    for j in answer:
        print(j)