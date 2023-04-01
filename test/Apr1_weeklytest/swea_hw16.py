# 암호코드 스캔
import sys
import math

sys.stdin = open('input.txt', 'r')

my_dict = {"112": 0,
           "122": 1,
           "221": 2,
           "114": 3,
           "231": 4,
           "132": 5,
           "411": 6,
           "213": 7,
           "312": 8,
           "211": 9}


def pw_solve(arr):
    rlt = 0
    result_arr = set()

    for n in arr:
        ans = ""
        for s in n:
            binary4 = ""
            # 10진수로 전환 후 2진수 전환 진행
            s = int(s, 16)

            for i in range(3, -1, -1):
                binary4 += "1" if s & (1 << i) else "0"

            ans += binary4

        # 뒤부터 검사해서 1이 등장하면 시작
        ans = ans[::-1]
        pre = ans[0]
        cnt = 0
        check_list = []
        result = []

        for s in ans:

            if s == pre:
                cnt += 1

            else:
                check_list.append(cnt)
                cnt = 1
            
            pre = s

        for i in range(1,len(check_list),4):

            gcd_num = min(check_list[i:i+3])
            new_check = ""
            
            for j in range(3):
                new_check += str(check_list[i+j] // gcd_num)

            app_v = my_dict.get(new_check, -1)
            result.append(app_v)
        
        result = result[::-1]

        for i in range(0, len(result), 8):
            result_arr.add(tuple(result[i:i+8]))


    for res in result_arr:

        check_sum = 0
        for i in range(8):
            if i % 2 == 0:
                check_sum += res[i] * 3
            else:
                check_sum += res[i]

        if check_sum % 10 == 0:
            rlt += sum(res)

        else:
            pass

    return rlt


T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    box = set(input().strip()[:m] for _ in range(n))

    rlt = pw_solve(box)

    print(f'#{tc} {rlt}')
