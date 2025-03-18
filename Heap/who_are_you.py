# 1764
import sys

input = sys.stdin.readline
listen, see = map(int, input().split())

h = [input().strip() for _ in range(listen)]
s = [input().strip() for _ in range(see)]

result = sorted(set(h) & set(s))

print(len(result))
print(*result)