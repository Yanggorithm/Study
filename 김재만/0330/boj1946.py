# 백준 1946
# 양고리즘 스터디 문제 신입사원
# 풀이중

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    rank_list = [list(map(int, input().split())) for _ in range(n)]
    a_rank = sorted(rank_list, key=lambda x: x[0])
    b_rank = sorted(rank_list, key=lambda x: x[1])
    print(a_rank)
    print(b_rank)
