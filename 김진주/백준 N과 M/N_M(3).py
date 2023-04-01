'''
1~N까지 자연수 중 M개 고른 수열
길이 M 수열 모두 출력 = 가능한 모든 경우
같은 수 여러번 가능
중복 수열 X
'''
# n : 선택한 숫자 개수
def dfs(n, now):
    if n == M:
        ans.append(now)
        return

    for i in range(1, N+1):
        dfs(n+1, now+[i]) # list 끼리 더하기

N, M = map(int, input().split())
ans = []
dfs(0, [])
for lst in ans:
    print(*lst) # 리스트 언패킹 & 공백 출력