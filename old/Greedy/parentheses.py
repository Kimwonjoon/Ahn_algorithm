# 1541
# 55-50+40 이러한 경우에 괄호쳐서 최소를 만들기
# 55-(50+40) = -35
# 최소가 되려면 - 인경우 다시 - 나올때까지 계속 빼는게 당연히 나음
import sys

input = sys.stdin.readline
a = input().strip()

num = ""
now = "+"
result = 0
for i in a:
    if i in ['-','+']:
        if now == "+":
            result += int(num)
            num = ""
        else:
            result -= int(num)
            num = ""
    else:
        num = num + i

    if i == "-" and now == "+":
        now = "-"
    
if now == "-":
    result -= int(num)
else:
    result += int(num)
print(result)