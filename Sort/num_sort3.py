# 10989
# 들어오는 수가 1천만건이지만 들어오는 수는 10000 이하의 자연수
# 메모리 제한의 크기가 작아서 배열에 모든 값을 쌓아두면 통과 못함
# 계수 정렬(메모리의 크기가 제한적일때 사용)
import sys
input = sys.stdin.readline
n = int(input())
li = [0] * (10000 + 1)

for _ in range(n):
    ind = int(input())
    li[ind] += 1

for i in range(len(li)):
    if li[i] != 0:
        for _ in range(li[i]):
            print(i)