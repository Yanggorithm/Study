import sys
input = sys.stdin.readline
n, m = map(int, input().split())
numbers = list(map(int, input().split()))
sub_sum = 0
remainder = [0] * m
for i in range(n):
    sub_sum += numbers[i]
    remainder[sub_sum % m] += 1
result = remainder[0]
for rm in remainder:
    result += rm * (rm-1) // 2
print(result)