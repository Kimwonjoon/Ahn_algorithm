import sys
input = sys.stdin.readline
a, b = sorted(map(int, input().split()))

a_y = 4 if a % 4 == 0 else a % 4 # 33
b_y = 4 if b % 4 == 0 else b % 4 # 40

y_dist = b_y - a_y

a += y_dist

x_dist = (b - a) // 4

print(x_dist + abs(y_dist))