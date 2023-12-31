import sys
input = sys.stdin.readline
S = input().strip()
# S의 0번째 인덱스가 0인지 1인지
ans_one = 0
prev = cont = "0"
for oz in S:
    if oz != prev:
        prev = oz
        if prev != cont:
            ans_one += 1

ans_zero = 0
prev = cont = "1"
for oz in S:
    if oz != prev:
        prev = oz
        if prev != cont:
            ans_zero += 1

print(min(ans_one, ans_zero))