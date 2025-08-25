import sys

input = sys.stdin.readline

ind = int(input())

for test_case in range(1, ind + 1):
    number = int(input())
    b = [[0] * number for _ in range(number)]

    start_x = 0
    start_y = 0
    # 우 하 좌 상 우 하 좌 상 우 하 좌 상 반복
    direction = "r" # "d" "l" "u"
    for i in range(1, number ** 2 + 1):
        if direction == "r":
            b[start_y][start_x] = i
            # 다음 위치가 큐브의 내부이면서 0이면 이동
            if start_x + 1 < number and b[start_y][start_x + 1] == 0:
                start_x += 1
            # 다음 위치가 큐브를 벗어나거나 이미 방문했다면 다음 방향으로 전환
            else:
                direction = "d"
                start_y += 1
        elif direction == "d":
            b[start_y][start_x] = i
            if start_y + 1 < number and b[start_y + 1][start_x] == 0:
                start_y += 1
            else:
                direction = "l"
                start_x -= 1
        elif direction == "l":
            b[start_y][start_x] = i
            if start_x - 1 >= 0 and b[start_y][start_x - 1] == 0:
                start_x -= 1
            else:
                direction = "u"
                start_y -= 1
        else:
            b[start_y][start_x] = i
            if start_y - 1 >= 0 and b[start_y - 1][start_x] == 0:
                start_y -= 1
            else:
                direction = "r"
                start_x += 1

    print(f"#{test_case}")
    for result in b:
        print(*result)