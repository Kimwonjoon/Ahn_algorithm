# 딕셔너리 정렬을 할 줄 아는가? sorted ~~ key = lambda x : ~~ 이걸 할 줄 아는가? 정도의 문제
import sys

input = sys.stdin.readline

T = int(input())

for test_case in range(T):
    # 문제 번호
    q_num = int(input())

    # 테스트 케이스
    li = list(map(int, input().split()))

    dic = {}

    for num in li:
        if num not in dic:
            dic[num] = 1
        else:
            dic[num] += 1

    sort_dic = sorted(dic.items(), key = lambda x: (x[1], x[0]), reverse=True)

    print(f"#{q_num} {sort_dic[0][0]}")