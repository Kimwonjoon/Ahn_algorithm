import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    end = 2 * n

    sieve = [1] * (end + 1)
    sieve[0] = sieve[1] = 0

    for i in range(2, int(end ** 0.5) + 1):
        if sieve[i]:
            for j in range(i*i, end+1, i):
                sieve[j] = 0

    print(sum(sieve[n+1:end+1]))