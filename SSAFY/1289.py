import sys

input = sys.stdin.readline
T = int(input())

for test_case in range(1, T+1):
    answer = 0
    meme = list(input().strip()) # 이걸로 변환할꺼
    first = ["0"] * len(meme)

    for i in range(len(meme)):
        if first[i] != meme[i]:
            answer += 1
            if meme[i] == "1":
                first[i:] = "1" * (len(meme) - i)
            else:
                first[i:] = "0" * (len(meme) - i)

    print(f"#{test_case} {answer}")
