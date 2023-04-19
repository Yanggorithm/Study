import sys
sys.stdin = open('수영장.txt', 'r')

'''
1일이용권 : 1일 이용
1달이용권 : 1 달 이용 가능 매달 1일부터 시작
3달이용권 : 연속된 3달 동안 이용가능, 3달 이용권은 매달 1일부터시작
1년이용권 : 1년 동안 이용가능 매년 1월 1일부터 시작
'''
def check(idx, cnt, result):
    global min_v
    if cnt <= 0:
        min_v = min(min_v, result)
        return

    for i in range(idx, N - 2):
        result += price[0] * re_month[i]
        check(i + 1, cnt - 1, result)
        result -= price[0] * re_month[i]

        result += price[1]
        check(i + 1, cnt - 1, result)
        result -= price[1]

        result += price[2]
        check(i + 3, cnt - 3, result)

T = int(input())

for test_case in range(1, T + 1):
    price = list(map(int, input().split()))
    month = list(map(int, input().split()))

    month_cnt = 0
    re_month = []
    for i in range(12):
        if month[i]:
            month_cnt += 1
            re_month.append(month[i])

    re_month += [0, 0]
    N = len(re_month)

    year = price[3]
    min_v = 100000

    check(0, month_cnt, 0)
    print(f'#{test_case} {min(min_v, year)}')
