# 2847

import sys

input = sys.stdin.readline

ind = int(input())
li = []
for i in range(ind):
    lv = int(input())
    li.append(lv)

cnt = -1
result = 0
for i in li[-2::-1]: # 난이도 제일 높은것부터 받기
    if i >= li[cnt]:
        while i >= li[cnt]:
            i -= 1
            result += 1
        li[cnt-1] = i
    cnt -= 1

print(result)