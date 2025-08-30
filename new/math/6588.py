# 4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다.
import sys
input = sys.stdin.readline

# 에라토스테네스의 체
def sieve(n):
    # True = 소수 False = 소수 아님
    prime = [True for _ in range(n+1)]
    # 0,1 제외
    prime[0] = prime[1] = False
    # 2부터 제곱근 +1 까지만 해도 됨
    for i in range(2, int(n**0.5)+1):
        if prime[i]:
            # i가 소수라면 i의 배수는 소수가 아님
            for j in range(i*i, n+1, i):
                prime[j] = False
    return prime
# 주어질 최대범위
n = 1000000
li = sieve(n)

while True:
    num = int(input())
    if num == 0:
        break
    # 홀수만 찾는거니까 3부터 2씩 올라가도 충분
    for k in range(3, num//2+1, 2):
        if li[k] and li[num-k]:
            print(f"{num} = {k} + {num-k}")
            break