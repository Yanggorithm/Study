"""
풀이접근 방법
1. 배열의 길이만큼의 1로 채운 배열 arr를 만든다.
2. 앞에서부터 자신보다 앞선 수보다 클 경우 arr의 자리에다가
    이전 앞선 수의 arr 수를 더한다.
"""

import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().strip().split()))

arr = [1] * N
for i in range(1, N):
    for j in range(i):
        if A[j] < A[i] and arr[j]+1 > arr[i]:
            arr[i] = arr[j] + 1

print(max(arr))