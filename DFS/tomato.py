# 7576
import sys
from collections import deque

w, h = map(int, sys.stdin.readline().split())

t = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]

# 토마토가 있는 위치
q = deque()
for i in range(h):
    for j in range(w):
        if t[i][j] == 1:
            q.append([i,j])

# 토마토가 양쪽에 있는 경우 좌측 계산 끝나고 우측 계산이 끝나면 안되기 때문에
# bfs를 통해서 미리 저장된 토마토의 위치들부터 계산을 시작하면서 서로 맞물려짐
def bfs():
    while q:
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and t[nx][ny] == 0:
                t[nx][ny] = t[x][y] + 1
                q.append([nx,ny])

bfs()

result = 0
for i in range(h):
    for j in range(w):
        if t[i][j] == 0:
            print(-1)
            exit(0)
    result = max(result, max(t[i]))

print(result - 1)