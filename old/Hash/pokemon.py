# 1620
import sys
input = sys.stdin.readline
doc, problem = map(int, input().split())

# 이름이 key
document1 = {}
# 도감 번호가 key
document2 = {}

for i in range(doc):
    name = input().strip()
    document1[name] = i + 1
    document2[i+1] = name

for _ in range(problem):
    question = input().strip()
    # 문제가 숫자라면 포켓몬 이름을 말해야함
    if question.isdigit():
        print(document2[int(question)])
    else:
        print(document1.get(question))