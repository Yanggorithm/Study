# 추가문제 21
# 수영장

def comb(n, rlt, visited, comb_arr, cal):
    if len(rlt) == n:
        comb_arr.append(rlt[:])
        return

    start = cal.index(rlt[-1]) if rlt else 0
    for i in range(start, 10):
        if not visited[i]:
            visited[i] = 1
            rlt.append(i)
            comb(n, rlt, visited, comb_arr, cal)
            visited[i] = 0
            rlt.pop()

    return


def dfs(arr):
    result = [0] * 12

    for i in range(len(arr)):
        # 우선 하루 이용권 이용 가격과 1달 이용가격만 비교
        # 이용하는 날짜가 하루라도 있다면?
        if arr[i]:
            if arr[i] * day > month:
                result[i] = month
            else:
                result[i] = arr[i] * day

    # 콤비네이션으로 3달치 모든 경우의 수 구해줌
    cal = [i for i in range(10)]
    comb_arr = []
    for i in range(1, 4):
        visited = [0] * 10
        rlt = []
        comb(i, rlt, visited, comb_arr, cal)

    # 전체 저장, 이후 값은 의미 없음
    comb_arr.append([0, 3, 6, 9])
    min_v = sum(result)
    for combi in comb_arr:
        copy_result = result[:]
        max_v = 0
        cnt = 0
        for i in combi:
            for j in range(i, i + 3):
                max_v += copy_result[j]
                copy_result[j] = 0
            cnt += 1

        if max_v > t_month * cnt:
            min_v = min(min_v, t_month * cnt + sum(copy_result))

    # 1년치는 최종적으로 하루, 1달, 3달 이용권 조합한 최적의 값과 마지막에 비교
    ans = min(year, min_v)

    return ans


T = int(input())

for tc in range(1, T + 1):
    day, month, t_month, year = map(int, input().split())
    plan = list(map(int, input().split()))

    ans = dfs(plan)

    print(f'#{tc} {ans}')
