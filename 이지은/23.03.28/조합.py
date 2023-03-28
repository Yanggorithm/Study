lst = [1,2,3,4,5]
n = 5
R = 3

# n개 중에 r개를 고르는 경우의 수

# 1. idx 번째 숫자를 고를지 고르지 않을 지 결정
def comb(idx, r, selected):
    
    # 종료 조건
    if idx == n:
        if len(selected) == R:
            print(selected)
        return
    
    # 재귀 호출
    # 고르고 진행하던가
    selected.append(lst[idx])
    comb(idx+1, r+1, selected)
    # 고르지 않고 진행하던가
    selected.pop()
    comb(idx+1, r, selected)


comb(0,0,[])

print("===========")
# 2. R개 고를 때까지 계속 선택
# 내가 idx번째 원소를 골랐다면, idx 이전에 있는 친구는 고려하지 않고
# 뒤에 있는 것만 선택
def comb2(idx, selected):
    # 종료 조건
    if len(selected) == R:
        print(selected)
        return

    # 재귀 호출
    # 현재 위치 idx 기준 i >= idx i번째 숫자를 하나 고르고 진행
    for i in range(idx, n):
        comb2(i+1, selected + [lst[i]])

comb2(0,[])