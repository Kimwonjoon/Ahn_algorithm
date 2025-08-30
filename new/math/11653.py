import sys
input = sys.stdin.readline
num = int(input())

n = 2
while num != 1:
    if num % n == 0:
        print(n)
        num //= n
    else:
        n += 1