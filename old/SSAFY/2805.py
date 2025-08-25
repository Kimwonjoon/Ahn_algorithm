import sys

input = sys.stdin.readline

T = int(input())

for test_case in range(1, T + 1):
    result = 0

    N = int(input())

    farm = [list(input().strip()) for _ in range(N)]
    num = 1
    reverse_farm = False
    left_ind = N // 2
    right_ind = N // 2

    # 만약 N이 3이면 1 3 1, 5면 1 3 5 3 1 이런식으로 중앙행에 올때까지 1부터 2씩 증가하는 방식으로 가면 됨
    for i in range(N):
        # 가운데에 도달했는지 확인
        if right_ind == N-1:
            reverse_farm = True

        result += sum(map(int, farm[i][left_ind:right_ind + 1]))

        # 가운데에 도달했다면 이제 거꾸로 서로 가까워져야함
        if reverse_farm:
            left_ind += 1
            right_ind -= 1
        else:
            left_ind -= 1
            right_ind += 1

    print(f"#{test_case} {result}")