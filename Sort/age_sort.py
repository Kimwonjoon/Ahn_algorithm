# 10814
import sys
input = sys.stdin.readline
n = int(input())

dic = {}
for _ in range(n):
    age, name = list(map(str, input().strip().split()))

    if age not in dic:
        dic[age] = [name]
    else:
        dic[age].append(name)

# 나이가 같다면 먼저 가입한 사람이 우선이기 때문에 정렬의 기준은 나이로만
sort_dic = sorted(dic.items(), key=lambda x: int(x[0]))

for ages, names in sort_dic:
    for n in names:
        print(ages, n)