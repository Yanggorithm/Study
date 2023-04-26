def recur(idx, s, selected):
    global cnt, cnt2
    cnt2 += 1
    # 가지 치기 조건
    # 백트래킹 -> 이미 10보다 커졌다면 더이상 탐색할 필요가 없음
    if s > target_num:
        return

    if s + sum(lst[idx:]) < target_num:
        return

    # 종료 조건 ( 마지막 원소에 도달했을때 )
    if idx == n:
        if s == target_num:
            # 골랐던 리스트를 출력
            print(selected)
            cnt += 1
        return
        # 재귀 호출
    # idx 번째 원소를 선택하거나
    selected.append(lst[idx])
    recur(idx + 1, s + lst[idx], selected)
    # idx 번째 원소를 선택하지 않거나
    selected.pop()
    recur(idx + 1, s, selected)


lst = [i for i in range(1, 11)]
n = 10
cnt = 0
cnt2 = 0
target_num = 55
# 합이 10인 부분집합의 갯수
recur(0, 0, [])
print(cnt)
print(cnt2)
# 현재 위치 idx 에 대하여 idx 번째 원소를 선택 or 선택x
