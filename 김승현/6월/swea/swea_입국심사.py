import sys
sys.stdin = open('입국심사.txt', 'r')
T = int(input())

for test_case in range(1, T + 1):
    answer = 0
    n, m = map(int, input().split())

    times = [int(input()) for _ in range(n)]
    left, right = 1, max(times) * m

    while left <= right:
        mid = (left + right) // 2
        people = sum([mid // time for time in times])

        if people >= m:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    print('#' + str(test_case), answer)