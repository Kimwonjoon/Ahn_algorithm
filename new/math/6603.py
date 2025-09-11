import sys
input = sys.stdin.readline

def dfs(depth, idx): # depth : 뽑은 개수, idx : 시작 인덱스
    if depth == 6: # 6자리 뽑았으면 중지
        print(*result)
        return

    for i in range(idx, l):
        result.append(li[i])
        dfs(depth + 1, i + 1)
        result.pop()
while 1:
    array = list(map(int, input().split()))

    l = array[0]
    li = array[1:]
    result = []

    if l == 0:
        break

    dfs(0,0)
    print()