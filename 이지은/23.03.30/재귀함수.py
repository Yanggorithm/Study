lst = [1,2,3,4,5,6,7,8,9,10]
n = 10

# 합이 10인 부부집합의 개수 구하기

# 현재 위치 idx에 대하여 idx번째 원소를 선택 or 선택x

def recur(idx, s, selected):
    global cnt
    # 가지치기 조건
    if s == 10:
        cnt += 1
        print(selected)
        return
    
    # 종료 조건
    if idx == n:
        # print(selected)
        return

    # 재귀 호출
    # idx 번째 원소를 선택하거나
    selected.append(lst[idx])
    recur(idx + 1, s + lst[idx], selected)
    # idx 번째 원소를 선택하지 않거나
    selected.pop()
    recur(idx + 1, s, selected)

cnt = 0
recur(0, 0, [])
print(cnt)