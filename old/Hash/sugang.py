# 13414
import sys
input = sys.stdin.readline
s, n = map(int, input().split())

dic = {}
for i in range(n):
    school = input().strip()
    dic[school] = i

result = sorted(dic.items(), key = lambda x : x[1])

for j in range(s):
    if j == len(result):
        break
    print(result[j][0])