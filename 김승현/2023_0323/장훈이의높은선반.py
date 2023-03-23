import sys
sys.stdin = open('장훈이의높은선반.txt', 'r')

T = int(input())

def combi(n, start):
    if n == k:
        result = sum(ans)
        if result >= B:
            res.append(result)
            return

    for i in range(start, N):
        ans.append(Height[i])
        combi(n + 1, i + 1)
        ans.pop()

for test_case in range(1, T + 1):
    N, B = map(int, input().split())
    Height = list(map(int, input().split()))
    Height.sort()
    ans = []
    res = []
    max_v = 100000000
    for i in range(1, N + 1):
        k = i
        combi(0, 0)
    print(f'#{test_case} {min(res) - B}')

