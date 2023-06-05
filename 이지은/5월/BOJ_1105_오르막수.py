import sys
input = sys.stdin.readline

"""
풀이 접근 방법
길이가 n인 오르막 수 : 뒤로 갈수록 증가해야 한다.

1번째에 0~9까지 들어갈 수 있음.
2번째에 0일때는 1번째에는 0만, 1일때는 0~1만, 2일때는 0~2만 ...
...
i번째에는 0일때는 

"""
def solve():
    N = int(input().strip())
    if N == 1:
        print(10)
        return
    else:
        arr = [[1] * 10 for _ in range(N)]
        for i in range(1, N):
            for j in range(1, 10):
                arr[i][j] = arr[i-1][j] + arr[i][j-1]
        print(sum(arr[N-1])%10007)

solve()