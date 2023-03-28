# 두 명의 일꾼이 가로로 연속되게 벌꿀을 채취
# 일꾼이 채취할 수 있는 벌통의 수 : M
# 두 일꾼이 선택한 벌통이 겹치면 안된다.

# 두 일꾼이 채취할 수 있는 꿀의 최대 양 : C
# 최대 양을 초과할 경우, 최대 양에 맞추도록 몇개의 벌꿀 통 채취를 포기

# 수익은 각 용기의 벌꿀의 제곱만큼
# 수익이 최대가 되는 경우

# 가로로 m만큼씩 두개 선택

t = int(input())

def solve(cnt, tmp):
    if cnt == 3 and sum(tmp) >= c:
        sorted(tmp)
    
    for i in range(n):
        for j in range(n):
            if j+m-1 >= n:
                continue
            
            if visited[i][j] > 0:
                continue

            visited[i][j:j+m] = [cnt]*m
            solve(cnt+1, tmp+honey[i][j:j+m])
            visited[i][j:j+m] = [0]*m
            

for tc in range(1, t+1):
    n, m, c = map(int, input().split())
    honey = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    solve(0,[])