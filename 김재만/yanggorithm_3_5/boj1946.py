# 백준 1946
# 양고리즘 스터디 문제 신입사원
# 풀이중
import sys
input = sys.stdin.readline


T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    rank_list = [list(map(int, input().split())) for _ in range(n)]
    # 여기서 한 성적을 기준으로 정렬을 먼저 하자
    a_rank = sorted(rank_list, key=lambda x: x[0])
    # 처음 한명은 통과
    ans = 1
    check_rank = a_rank[0][1]
    for i in range(1,n):
        if check_rank > a_rank[i][1]:
            ans += 1
            check_rank = a_rank[i][1]
    
    print(ans)

