import sys
input = sys.stdin.readline

"""
풀이 접근 방법
포도주를 마시는 방법
1. 현재 포도주와 이전 포도주를 마시는 경우(전전 포도주는 마실 수 없다.)
2. 현재 포도주와 전전 포도주를 마시는 경우(이전 포도주는 마실 수 없다.)
3. 현재 포도주를 마시지 않는 경우(전전, 이전포도주를 마신다.)

풀이 접근 방법(오답)
1. 인접한 포도주 2잔을 마셨을 경우를 더해서 배열에 저장해준다.
ex ) 6 10 13 9 8 1
    => 16 23 22 17 9
2. 세칸씩 떨어진 값들의 합과 비교하여 최대값으로 갱신해준다. => 오답
    반례) 답 : 36
    10
    0
    0
    10
    0
    5
    10
    0
    0
    1
    10
"""
n = int(input().strip())
lst = [int(input().strip()) for _ in range(n)]

result = [0] * n
result[0] = lst[0]
if n > 1:
    result[1] = lst[0]+lst[1]
if n > 2:
    result[2] = max(lst[1] + lst[2], lst[0]+lst[2], result[1])

for i in range(3, n):
    result[i] = max(lst[i] + lst[i-1] + result[i-3], lst[i]+result[i-2], result[i-1])

print(max(result))