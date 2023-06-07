# SWEA_1217 거듭 제곱

# import sys
# sys.stdin = open("swea_1217.txt", "r")

def solution(base, index, answer, n):
    if n == index:
        return answer
    
    answer *= base
    return solution(base, index, answer, n+1)

for _ in range(10):
    TC = int(input())
    base, index = map(int,input().split())

    print(f'#{TC}', solution(base, index, 1, 0))

