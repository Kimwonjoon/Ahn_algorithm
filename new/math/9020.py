import sys
input = sys.stdin.readline
n = int(input())

for test_case in range(n):
    num = int(input())
    answer = []
    min_num = num

    li = [True] * (num + 1)
    li[0] = li[1] = False

    for i in range(2, int(num**0.5)+1):
        if li[i]:
            for j in range(i*i, num+1, i):
                li[j] = False

    for k in range(len(li)):
        if li[k] and li[num-k]:
            if min(min_num, abs(num-(k*2))) == abs(num-(k*2)):
                min_num = abs(num-(k*2))
                answer = [k,num-k]

    answer.sort()
    print(" ".join(map(str, answer)))