# 16진수 숫자
# 시계방향으로 한번 돌릴때마다 한칸씩 회전
# 비밀번호는 숫자 중에 k번째로 큰 수를 10진 수로 만든 수

"""
풀이 접근 방법
N/4 - 1회전 하면 무조건 같은 수가 됨.

"""
from collections import deque
t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())
    nums = input()

    lst = set()
    # 초기 상태에 있는 숫자 넣기
    for i in range(4):
        t = nums[i*(n//4):(i+1)*(n//4)]
        b = int(t, 16)
        lst.add(b)

    # 숫자가 중복되기 전까지
    for _ in range(n//4-1):
        # 한칸씩 회전시키면서
        tmp = nums[0]
        nums = nums[1:] + tmp
        # 숫자 넣기
        for i in range(4):
            t = nums[i*(n//4):(i+1)*(n//4)]
            b = int(t, 16)
            lst.add(b)

    print(f"#{tc} {sorted(list(lst), reverse=True)[k-1]}")
