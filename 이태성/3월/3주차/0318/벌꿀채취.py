def counting(r, c, M, stack):
    for i in range(M):
        stack.append(barrel[r][c+i])
        visited[r][c+i] = 1
# 순열 * 순열
def cal_A(idx, sub_sum, length, stack):
    global A_honey
    if idx == M:
        if sub_sum <= C and length > 0:
            A_honey = max(A_honey, cal(stack))
        return
    if idx < M:
        cal_A(idx+1, sub_sum+A[idx], length+1, stack+[A[idx]])
        cal_A(idx+1, sub_sum, length, stack)

def cal_B(idx, sub_sum, length, stack):
    global B_honey
    if idx == M:
        if sub_sum <= C and length > 0:
            B_honey = max(B_honey, cal(stack))
        return
    if idx < M:
        cal_B(idx+1, sub_sum+B[idx], length+1, stack+[B[idx]])
        cal_B(idx+1, sub_sum, length, stack)

def reset(r, c, M):
    for i in range(M):
        visited[r][c+i] = 0

def cal(stack):
    tot = 0
    for num in stack:
        tot += num ** 2
    return tot

T = int(input())
for tc in range(1, T+1):
    max_honey = 0
    # 범위, 연속된 벌통, 벌통 최대 용량
    N, M, C = map(int, input().split())
    visited = [[0] * N for _ in range(N)]
    barrel = [list(map(int, input().split())) for _ in range(N)]
    for r in range(N):
        for c in range(N-M+1):
            A_honey = 0
            A = list()
            A.sort()
            counting(r, c, M, A)
            cal_A(0, 0, 0, [])
            for p in range(r, N):
                for q in range(N-M+1):
                    if visited[p][q] == 0:
                        B_honey = 0
                        B = list()
                        B.sort()
                        counting(p, q, M, B)
                        cal_B(0, 0, 0, [])
                        sub_honey = A_honey + B_honey
                        max_honey = max(max_honey, sub_honey)
                        reset(p, q, M)
    print(f"#{tc}", max_honey)