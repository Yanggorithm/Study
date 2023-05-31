# SWEA_1959 두 개의 숫자열

T = int(input())
for TC in range(1,T+1):
    N, M = map(int,input().split())
    
    # 길이가 더 짧은 인풋을 A에 할당하기 위해!
    if N >= M :
        B = list(map(int,input().split()))
        A = list(map(int,input().split()))
    else :
        A = list(map(int,input().split()))
        B = list(map(int,input().split()))

    # 비교 횟수는 긴 배열의 길이 - 짧은 배열의 길이 + 1 
    dis = abs(N-M) + 1

    maxx = 0
    for i in range(dis):
        # 두 숫자열을 순서대로 순회하며 값을 곱하여 tmp에 더하고 이를 maxx와 비교하여 maxx 갱신
        tmp = 0 
        # tmp 한 번 계산할 때, 짧은 배열의 길이만큼 각각의 배열을 순회할 것
        for j in range(len(A)):
            # 이 때, B[i+j]의 값을 곱해줌으로써 tmp 갱신될 때마다 
            # 짧은 배열의 위치를 한 칸씩 우측으로 움직이는 것과 같은 효과 기대할 수 있음
            tmp += A[j] * B[i+j]
        if maxx < tmp:
            maxx = tmp
    
    print(f'#{TC}', maxx)