import sys

input = sys.stdin.readline
n = int(input())
li = sorted(list(map(int, input().split())))
answer = 0
max_num = li[-1]

# True면 소수이다.
sieve = [True] * (max_num + 1)
# 0, 1은 기본적으로 제외한다.
sieve[0] = sieve[1] = False

for i in range(2, int(max_num ** 0.5) + 1):
    if sieve[i]:
        for j in range(i * i, max_num + 1, i):
            sieve[j] = False

for k in li:
    if sieve[k]:
        answer += 1

print(answer)