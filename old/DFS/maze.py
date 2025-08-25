# 2178
import sys
from collections import deque
input = sys.stdin.readline
h,w = map(int, input().split())

maze = []

for _ in range(h):
    a = list(map(int, input().strip()))
    maze.append(a)

def bfs(x,y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append([x,y])
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and maze[nx][ny] == 1:
                q.append([nx,ny])
                # 이전의 공간에 갈 수 있는 경우의 수 + 1을 하며 이동
                maze[nx][ny] = maze[x][y] + 1

bfs(0,0)

print(maze[h-1][w-1])