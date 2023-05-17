t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    
    arr = [list(map(int, input().split())) for _ in range(n)]

    ans = 0
    for k in range(2*n):
        expense = (k+1)*(k+1)+k*k

        for i in range(n):
            for j in range(n):

                cnt = 0
                for ti in range(i-k, i+k+1):
                    for tj in range(j - k + abs(i-ti), j + k - abs(i-ti)+1):
                        if 0 <= ti < n and 0 <= tj < n and arr[ti][tj] == 1:
                            cnt += 1

                profit = cnt * m

                if profit >= expense:
                    if ans < cnt:
                        ans = cnt
        
    print(f"#{tc} {ans}")