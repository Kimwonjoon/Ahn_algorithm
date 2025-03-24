# 1822
import sys

input = sys.stdin.readline

a,b = map(int, input().split())

set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

result = set_a - set_b

print(len(result))
print(*sorted(result))