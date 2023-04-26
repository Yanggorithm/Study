def merge(l, r):
    global cnt

    ans = []

    if l[-1] > r[-1]:
        cnt += 1

    while l or r:
        if l and r:
            if l[0] > r[0]:
                ans.append(r.pop(0))
            else:
                ans.append(l.pop(0))
        else:
            if l:
                while l:
                    ans.append(l.pop(0))
            else:
                while r:
                    ans.append(r.pop(0))

    return ans


def mergeSort(m):
    # 종료
    if len(m) == 1:
        return m

    # 분할
    # 왼쪽 : left, 오른쪽 : right
    # 가운데
    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]

    # 정복
    left = mergeSort(left)
    right = mergeSort(right)

    print(f"left : {left}")
    print(f"right : {right}")
    result = merge(left, right)
    print(f"result : {result}")
    print(f"-------------")
    # 병합
    return result


for tc in range(1):
    arr = list(map(int, input().split()))
    cnt = 0
    result = mergeSort(arr)

    print(cnt)
