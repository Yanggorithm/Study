'''
n 개의 식재료
반씩 나누어 2개의 요리 (n은 짝수)
a, b 음식 맛차이가 최소가 되도록 배분

'''
# k : 재료 번호
def dfs(k, alst, blst):
    global ans
    if k == n:
        # a 음식에 선택된 재료 개수가 절반일 경우(b도 길이 같을테니 a만 써줘도 ok)
        if len(alst) == m:
            asum = bsum = 0
            for i in range(m):
                for j in range(m):
                    asum += arr[alst[i]][alst[j]]
                    bsum += arr[blst[i]][blst[j]]
            ans = min(ans, abs(asum-bsum))
        return

    dfs(k+1, alst+[k], blst) # a 음식 list에 추가
    dfs(k+1, alst, blst+[k]) # b 음식 list에 추가

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    m = n // 2
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = 20000 * n * n # 최악의 경우 가장 큰 max 값

    dfs(0, [], [])
    print(f'#{tc} {ans}')