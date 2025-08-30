import sys
input = sys.stdin.readline
N, M = map(int, input().split())
li = []

def back():
    # 종료조건
    if len(li) == M:
        print(" ".join(map(str, li)))
        return
    # 1 ~ N
    # 1 -> 1 2 -> 1 2 3 -> 1 2 4 -> 1 2 -> 1 -> 1 3 ...
    for i in range(1, N+1):
        if i not in li:
            li.append(i)
            back()
            li.pop()

back()