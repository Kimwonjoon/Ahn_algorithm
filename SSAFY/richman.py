n = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
result = []
for test_case in range(1, n + 1):
    day = int(input())
    li = list(map(int, input().split()))
    result = 0
    max_price = 0
    for i in li[::-1]:
        if i >= max_price:
            max_price = i
        else:
            result += max_price - i
    print(f"#{test_case} {result}")