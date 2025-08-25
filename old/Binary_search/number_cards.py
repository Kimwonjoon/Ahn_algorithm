# 10815
import sys

input = sys.stdin.readline

n = int(input())

own_cards = sorted(map(int, input().split()))

m = int(input())

compare_cards = list(map(int, input().split()))

result = []
# 홀수 중앙 : // 2 짝수 중앙 : // 2 -1
for card in compare_cards:
    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2

        if own_cards[mid] == card:
            result.append(1)
            break
        elif own_cards[mid] > card:
            end = mid - 1
        elif own_cards[mid] < card:
            start = mid + 1

    if start > end:
        result.append(0)

print(*result)