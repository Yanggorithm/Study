'''
서류와 면접 성적 중 적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발
==> 둘 중 하나 점수가 같거나 큰 지원자가 합격
==> 둘 다 낮다면 탈락
==> 탈락자 세서 빼주기 (N-cnt)
'''
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(1, T+1):
    N = int(input())
    # 서류, 면접 등수 넣어줄 리스트
    rank = []
    for _ in range(N):
        # A:서류 / B:면접
        A, B = map(int, input().split())
        rank.append((A, B))

    # 서류 기준으로 정렬
    rank.sort(key=lambda x: x[0])

    cnt = 0
    # 첫 면접 등수를 최소로 설정
    min_v = rank[0][1]
    for i in range(1, N):
        if rank[i][1] > min_v:
            cnt += 1
        min_v = min(min_v, rank[i][1])
    print(N-cnt)