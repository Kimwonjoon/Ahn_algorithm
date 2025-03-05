# 1926
import sys
input = sys.stdin.readline

h,w = map(int,input().split())

picture = []
visited = [[False]*w for _ in range(h)]

for _ in range(h):
    line = list(map(int,input().split()))
    picture.append(line)

def dfs(x,y):
    pass



print(picture, visited)