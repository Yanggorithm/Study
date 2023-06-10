import sys
sys.stdin = open('input.txt', 'r')
# 문어박사님 코드
T = int(input())
for TC in range(1, T+1):
    pipe = list(input())

    answer = cnt = 0
    for i in range(len(pipe)):
        if pipe[i] == "(":
            cnt += 1
        else:
            cnt -= 1
            # 레이저
            if pipe[i-1] == "(":
                answer += cnt
            # 끝부분
            else:
                answer += 1

    print(f"#{TC} {answer}")