import sys

input = sys.stdin.readline

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    result = [0 for _ in range(N)]
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    num = 1

    for i in range(N):
        # 홀수 1,3,5 이때는 A의 시간
        if num % 2 != 0:
            player = a.pop(0)
            result[player - 1] = "A"
            b.pop(b.index(player))
            num += 1
        else:
            player = b.pop(0)
            result[player - 1] = "B"
            a.pop(a.index(player))
            num += 1
    print("".join(result))