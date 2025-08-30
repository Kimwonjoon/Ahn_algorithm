# 소수 구하기
import sys

input = sys.stdin.readline
a, b = map(int, input().split())

sieve = [True] * (b + 1) # True = 소수이다.
sieve[0] = sieve[1] = False # 0, 1 제외

# 에라토스테네스의 체 알고리즘
for i in range(2, int(b ** 0.5) + 1): # 2 ~ 제곱근으로 범위 축소
    if sieve[i]: # 만약 sieve i가 소수라면
        for j in range(i * i, b + 1, i): # i의 배수들을 False 처리 ex) i=2 -> 4, 6, 8, 10 ...
            sieve[j] = False

# start부터 end까지의 소수 출력
for i in range(a, b + 1):
    if sieve[i]:
        print(i)