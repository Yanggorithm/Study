"""
풀이 접근 방법
1. 현재 위치의 좌, 우, 상 또는 하는 해당 위치 스티커를 선택하면 뜯을 수 없다.
2. 1번 열부터는, 이전 열까지 스티커 중에서 옆의 스티커 제외하고 다른 위치의 스티커 중에서 가장 큰값을 더한다.
- 1차 시도 실패 : 시간초과, 맨처음 자리부터 현재 위치까지 모두 돌았다.
- 2차 실패 : n이 1일 때, 2일 때를 고려해주지 않았다 => 인덱스에러
"""

import sys
input = sys.stdin.readline

t = int(input().strip())
for tc in range(t):
    n = int(input().strip())
    arr = [list(map(int, input().strip().split())) for _ in range(2)]
    if n == 1:
        print(max(arr[0][0], arr[1][0]))
    elif n == 2:
        arr[0][1] += arr[1][0]
        arr[1][1] += arr[0][0]
        print(max(arr[0][n-1], arr[1][n-1]))
    else:
        arr[0][1] += arr[1][0]
        arr[1][1] += arr[0][0]
        for i in range(2, n):
            # print('test', max(max(arr[0][0:i-1]), max(arr[1][0:i])))
            arr[0][i] += max(max(arr[0][i-2:i-1]), max(arr[1][i-2:i]))
            arr[1][i] += max(max(arr[0][i-2:i]), max(arr[1][i-2:i-1]))
        
        print(max(arr[0][n-1], arr[1][n-1]))