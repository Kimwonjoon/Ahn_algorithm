import sys

input = sys.stdin.readline

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    li = list(map(int,input().split()))

    up = 0
    down = 0

    for i in range(1,N):
        if li[i] >= li[i-1]:
            up = max(up, li[i] - li[i-1])
        else:
            down = max(down, li[i-1] - li[i])

    print(f"#{test_case} {up} {down}")