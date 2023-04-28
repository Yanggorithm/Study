# [1] 백트래킹 시작
def dfs(idx, nowV):
    # [2] 종료조건
    if idx >= N - 1:
        global minV, maxV
        maxV = max(maxV, nowV)
        minV = min(minV, nowV)
        return

    # 해당 연산자가 있으면 계산해준다.
    for i in range(4):
        if calculator[i]:
            calculator[i] -= 1
            dfs(idx+1, cal(nowV, numbers[idx+1], i))
            calculator[i] += 1

# 해당 연산자가 +인지 -인지 * 인지 / 인지 확인하고 계산
def cal(nowV, number_i, i):
    if i == 0:
        return nowV + number_i
    elif i == 1:
        return nowV - number_i
    elif i == 2:
        return nowV * number_i
    else:
        return int(nowV/number_i)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    calculator = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    # [3] 실수 주의
    # 최대 값은 최대한 작게
    # 최소 값은 최대한 크게
    # 여기서 값의 범위를 -100000000 <= 값 <= 100000000 로 정해줬기 때문에
    # 그것에 맞게 값을 정해줘야됨
    minV = 10**9
    maxV = -(10**9)
    # 첫번째 숫자를 넣고 시작
    dfs(0, numbers[0])
    print(f"#{tc} {maxV-minV}")