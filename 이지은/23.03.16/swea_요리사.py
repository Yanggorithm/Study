def solve(i, cnt):
    global minV
    if cnt == n//2:
        food1, food2 = 0, 0
        for k in range(n):
            for j in range(n):
                if k == j: continue
                elif selected[k] and selected[j]:
                    food1 += synergy[k][j]
                elif selected[k] == 0 and selected[j] == 0:
                    food2 += synergy[k][j]
        tmp = abs(food1-food2)
        if tmp < minV:
            minV = tmp

    for j in range(i, n):
        selected[j] = 1
        solve(j+1, cnt+1)
        selected[j] = 0


t = int(input())

for tc in range(1, t+1):
    n = int(input())
    synergy = [list(map(int, input().split())) for _ in range(n)]
    selected = [0] * n
    minV = 20000*2*n
    solve(0,0)
    print(f"#{tc} {minV}")

