t = int(input())

for tc in range(1, t+1):
    n = int(input())
    time = []
    dock = [0]*25
    for i in range(n):
        s, e = map(int, input().split())
        time.append((e-s , s, e))

    # 0시부터 다음날 0시 이전까지 A도크의 사용 신청을 확인
    # 최대한 많은 화물차가 화물을 싣고 내를 수 있도록
    time.sort()

    work = 0
    for t, s, e in time:
        if 1 not in dock[s:e]:
            work += 1
            for j in range(s,e):
                dock[j] = 1
    
    print(f"#{tc} {work}")
    