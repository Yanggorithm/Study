import sys
input = sys.stdin.readline

"""
풀이 접근 방법
1. 배열의 각 자리와 이전 배열을 더한 값을 비교하여 더 큰 값을 배열의 해당 자리에 저장해주기
==> 이전 값과 더한 값이 더 크다면 연속해서 더해온 값에 현재 값을 더함
==> 아니라면 연속한 값이 아니라 현재 값부터 다시 시작
2. 반복이 끝나면 최대값을 반환

(시간초과)==> sum 사용하지 않고 배열에 저장해서 memoization 사용하기
풀이 접근 방법
1. 배열의 각 자리에서 배열의 끝으로 이동하면서 해당자리부터 끝까지 더했을때 큰 값을 저장한다.
2. 배열이 다 채워지면 배열에서 최대값을 찾는다.
"""

n = int(input().strip())
lst = list(map(int, input().strip().split()))

# 시작지점
for i in range(1, n):
    lst[i] = max(lst[i], lst[i-1] + lst[i])

print(max(lst))