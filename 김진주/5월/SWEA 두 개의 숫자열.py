# SWEA 1959 두 개의 숫자열
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 짧은 길이를 항상 A로, 긴 길이를 항상 B로 할당
    if N > M:
        A, B = B, A
        N, M = M, N

    # 곱한 값의 합들을 넣을 리스트
    ls = []
    # (긴 길이)-(짧은 길이)+1 만큼
    for j in range(M-N+1):
        # 곱한 값 넣을 리스트
        tmp = []
        for i in range(N):
            # 긴 리스트는 짧은 길이 만큼 for문 돈 뒤에 인덱스 번호+1씩
            tmp.append(A[i]*B[i+j])

        # 곱한 값의 합 더하기
        ls.append(sum(tmp))

    # 곱한 값의 합 중 최대 값이 정답
    print(f"#{t} {max(ls)}")

