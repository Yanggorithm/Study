# swea 실습 51
# 16905. 베이비진 게임
import sys
sys.stdin = open('input.txt', 'r')


def solve_baby(arr):
    flag = 0
    check_list = arr[:]
    # triplet 부터 검사
    while True:
        if max(check_list) >= 3:
            idx = check_list.index(max(check_list))
            check_list[idx] -= 3
            flag += 1
        else:
            break

    # run 검사
    while True:
        baby_run = 0
        for i in range(len(check_list)):
            # 0이 아닌 숫자라면 run 증가
            if check_list[i]:
                baby_run += 1
                check_list[i] -= 1
            # 연속되지 않으면 의미가 없으므로 run 값 초기화
            else:
                baby_run = 0

            # run이 3일때 즉 run이 달성되면 flag 증가후 run값 초기화
            if baby_run == 3:
                flag += 1
                baby_run = 0
                break
        else:
            break

    if flag >= 1:
        return 1
    else:
        return 0


T = int(input())

for tc in range(1, T + 1):
    card_list = list(map(int, input().split()))

    player_a = [0] * 10
    player_b = [0] * 10

    for i in range(12):
        # player_a 차례
        if i % 2 == 0:
            player_a[card_list[i]] += 1
            a = solve_baby(player_a)
            if a:
                print(f"#{tc} {1}")
                break
        # player_b 차례
        else:
            player_b[card_list[i]] += 1
            b = solve_baby(player_b)
            if b:
                print(f"#{tc} {2}")
                break
    else:
        print(f"#{tc} {0}")