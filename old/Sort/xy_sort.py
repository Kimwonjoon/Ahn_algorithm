# 11650, 11651
import sys
input = sys.stdin.readline
n = int(input())
li = []
for _ in range(n):
    xy = list(map(int, input().split()))
    li.append(xy)

li.sort(key=lambda x: (x[0], x[1]))
# 11651
# 11651에서는 y 좌표를 우선으로 오름차순 정렬
# li.sort(key=lambda x: (x[1], x[0]))

for i in li:
    print(' '.join(map(str, i)))