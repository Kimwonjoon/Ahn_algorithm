import sys

input = sys.stdin.readline

for ind in range(1,2):
    num = int(input())
    li = list(map(int, input().split()))

    result = 0

    for i in range(2,num-2):
        now = li[i]
        tmp = [li[i] - li[i-2], li[i] - li[i-1], li[i] - li[i+1], li[i] - li[i+2]]

        if min(tmp) > 0:
            result += min(tmp)
    print(f"#{ind} {result}")