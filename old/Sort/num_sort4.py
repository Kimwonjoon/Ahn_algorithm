# 11931
import sys
input = sys.stdin.readline
n = int(input())
li = sorted([int(input()) for _ in range(n)], reverse=True)
print(*li)