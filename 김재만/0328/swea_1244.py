# 최대상금
import sys

sys.stdin = open('input.txt', 'r')


def perm(k):
    global max_ans

    if change_cnt == k:
        ans = int("".join(list(map(str, num_list))))
        max_ans = max(max_ans, ans)
    else:
        for j in range(k, len(num_list)):
            num_list[k], num_list[j] = num_list[j], num_list[k]
            perm(k + 1)
            num_list[k], num_list[j] = num_list[j], num_list[k]


def permm(cnt):
    global max_ans

    if max_ans == max_num:
        return

    # 교환 횟수를 다 사용했다면 최대 상금 구하기
    if cnt == change_cnt:
        ans = int("".join(list(map(str, num_list))))
        max_ans = max(max_ans, ans)
    else:
        # 교환 횟수가 남았다면 카드 바꾸기
        # 이 문제에서는 동일한 위치에서 중복 교환을 허용
        # 자리 위치 2개를 교환 마다 새로 정해 주어야 한다.
        for i in range(len_num - 1):
            for j in range(i + 1, len_num):
                num_list[i], num_list[j] = num_list[j], num_list[i]
                permm(cnt + 1)
                num_list[i], num_list[j] = num_list[j], num_list[i]


T = int(input())

for tc in range(1, T + 1):
    num_list, change_cnt = input().split()
    num_list = list(map(int, num_list))
    change_cnt = int(change_cnt)
    len_num = len(num_list)
    max_num = int("".join(map(str, sorted(num_list, reverse=True))))

    if len(num_list) < change_cnt:
        change_cnt = len(num_list)

    max_ans = 0
    permm(0)

    print(f"#{tc} {max_ans}")
