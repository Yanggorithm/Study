import sys
sys.stdin = open('input.txt', 'r')

def dfs(idx, sum_score, sum_kcal):
    global max_score

    # 제한 칼로리 넘어가면 리턴
    if sum_kcal > L:
        return

    # 점수 합이 최고 점수보다 높으면 갱신
    if sum_score > max_score:
        max_score = sum_score

    # 마지막 인덱스까지 다 돌았다면 리턴
    if idx == N:
        return

    # idx 파라미터를 통해 score, kcal 대입
    score, kcal = kcal_lst[idx]

    # 리스트에서 재료 사용 O
    dfs(idx + 1, sum_score + score, sum_kcal + kcal)
    # 리스트에서 재료 사용 X
    dfs(idx + 1, sum_score, sum_kcal)

T = int(input())
for TC in range(1, T+1):
    # N: 재료 수, L: 제한 칼로리
    N, L = map(int, input().split())

    # 재료 점수와 칼로리 리스트
    kcal_lst = [list(map(int, input().split())) for _ in range(N)]

    max_score = 0
    dfs(0, 0, 0)

    # 제한 칼로리 이하의 조합 중, 가장 높은 점수
    print(f'#{TC} {max_score}')