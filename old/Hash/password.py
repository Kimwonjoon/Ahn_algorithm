# 17219
import sys
input = sys.stdin.readline
n, p = map(int, input().split())

dic = {}

for _ in range(n):
    url, password = input().split()
    dic[url] = password

for _ in range(p):
    question = input().strip()
    print(dic[question])