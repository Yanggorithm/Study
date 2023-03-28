t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    w = sorted(list(map(int, input().split())), reverse=True)
    t = sorted(list(map(int, input().split())), reverse=True)

    # w : 컨테이너 화물의 무게 n
    # t : 적재용량 m

    load = 0 
    i, j = 0, 0
    while True:
        if i == n or j == m:
            break

        if w[i] <= t[j]:
            load += w[i]
            i += 1
            j += 1
        else:
            i += 1
    
    print(f"#{tc} {load}")

