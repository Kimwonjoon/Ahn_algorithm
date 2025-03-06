# 1926
import sys
# BFS = 큐
# DFS = 스택
def dfs(x,y):
    # 방문한 곳은 0으로 변경
    picture[x][y] = 0
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    # 넓이
    ww = 1
    # 방문할 곳의 좌표 저장될 배열
    li = list()
    li.append([x,y])
    while li:
        x,y = li.pop()
        # x,y = li.popleft() # bfs 방식
        for i in range(4):
            # 위아래 이동 좌표
            nx = x + dx[i]
            ny = y + dy[i]
            # 그림의 밖으로 나가지 않는 경우와 아직 방문하지 않은 곳인 경우
            if 0 <= nx < h and 0 <= ny < w and picture[nx][ny] == 1:
                li.append([nx,ny])
                picture[nx][ny] = 0
                ww += 1
    return ww

input = sys.stdin.readline

h,w = map(int,input().split())

picture = []

for _ in range(h):
    line = list(map(int,input().split()))
    picture.append(line)

cnt = 0 # 1의 개수
ans = 0 # 그림의 넓이 중 최대값

for i in range(h):
    for j in range(w):
        if picture[i][j] == 1:
            cnt += 1
            ans = max(dfs(i,j), ans)

print(cnt)
print(ans)