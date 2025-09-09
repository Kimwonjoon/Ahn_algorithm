import sys

input = sys.stdin.readline

cnt, result = map(int, input().split())

li = list(map(int, input().split()))

answer = 0

def subset_sum(idx, total):
    global answer

    if idx >= cnt:
        return

    total += li[idx]

    if total == result:
        answer += 1

    subset_sum(idx+1, total)
    subset_sum(idx+1, total - li[idx])

subset_sum(0,0)
print(answer)