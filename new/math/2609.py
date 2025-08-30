import sys
input = sys.stdin.readline
a,b = map(int, input().split())
li = []
min_num = min(a,b)
for i in range(1, min_num // 2 + 1):
    if b % i == 0 and a % i == 0:
        li.append(i)

if max(a,b) % min_num == 0:
    li.append(min_num)

answer1 = max(li)
# 최소공배수 = 주어진 두수 / 최대공약수
answer2 = (a * b) // answer1

print(answer1)
print(answer2)