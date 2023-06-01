

# N : 카드의 갯수, M :  특정 수
N, M = map(int, input().split())

# 카드
lst = list(map(int, input().split()))


ans = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if ans<lst[i]+lst[j]+lst[k] <= M:
                ans = lst[i] + lst[j] + lst[k]

print(ans)