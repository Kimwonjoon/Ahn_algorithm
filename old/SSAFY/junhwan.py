import sys

input = sys.stdin.readline

ind = int(input())

for test_case in range(1,ind+1):
    l,u,x = map(int,input().split())

    if l <= x and u >= x:
        print(f"#{test_case} {0}")
    elif l > x:
        print(f"#{test_case} {l - x}")
    else:
        print(f"#{test_case} {-1}")