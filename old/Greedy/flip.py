# 1439

import sys

input = sys.stdin.readline

line = input().strip() + "9"

dic = {}

for i in range(len(line)-1):
    if line[i] != line[i+1]: # 다음꺼랑 다르다면 dic에 1 추가해야겠죠
        if line[i] in dic:
            dic[line[i]] += 1
        else:
            dic[line[i]] = 1

if len(dic) == 1:
    print(0)
else:
    print(min(dic.values()))