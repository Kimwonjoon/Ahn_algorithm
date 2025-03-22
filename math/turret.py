# 1002 원의 거리 방정식, 내접 외접 사용하는 것
import sys
import math
input = sys.stdin.readline
n = int(input())

for _ in range(n):
    # x,y 좌표랑 r은 원의 반지름이라고 가정
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    # 두 원 중심 사이의 거리
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2)

    # 동심원인데 반지름이 같다면? -> 모든 것이 동일한거니까 무한대
    if d == 0 and r1 == r2:
        print(-1)
    # 만약 외접 or 내접이라면? -> 한 점에서 만나니까 1
    elif r1+r2 == d or abs(r1-r2) == d:
        print(1)
    # 원이 서로 다른 두 점에서 만난다면? -> 두 점이니까 2
    elif abs(r1-r2) < d < r1+r2:
        print(2)
    else:
        print(0)