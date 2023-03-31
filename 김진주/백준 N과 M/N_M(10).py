'''
중복 수열 x, 오름차순 출력
'''
# 풀이 1)
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(map(int, input().split()))
    v = [0] * N
    temp = []
    
    def dfs(start):
        if len(temp) == M:
            print(*temp)
            return

        pre = 0
        for i in range(start, N):
            if not v[i] and pre != A[i]:
                v[i] = 1
                temp.append(A[i])
                pre = A[i]
                dfs(i+1)
                v[i] = 0
                temp.pop()
    dfs(0)

# 풀이 2)
def dfs(n, start, now):
    if n == M:
        ans.append(now)
        return

    prev = 0
    for i in range(start, N):
        if v[i] == 0 and prev != lst[i]:
            prev = lst[i]
            v[i] = 1
            dfs(n+1, i+1, now + [lst[i]])
            v[i] = 0

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = sorted(map(int, input().split()))

    ans = []
    v = [0] * N
    dfs(0, 0, [])
    print(ans)
    for lst in ans:
        print(*lst)