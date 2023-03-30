# 병합정렬 구현

def merge_sort(s, e):
    if s == e:
        return

    # 분할
    middle = (s + e) // 2

    # 정복
    merge_sort(s, middle)
    merge_sort(middle + 1, e)

    # 결합
    l, r = s, middle + 1
    for k in range(s, e + 1):
        # 왼쪽 부분만 남았을경우 : 왼쪽 배열 남은거 추가
        if r > e:
            tmp[k] = arr[l]
            l += 1
        # 오른쪽 부분만 남았을경우 : 오른쪽 배열에 남은거 추가
        elif l > middle:
            tmp[k] = arr[r]
            r += 1
        # 둘다 남아있을 경우 : 값 비교
        elif arr[l] < arr[r]:
            tmp[k] = arr[l]
            l += 1
        else:
            tmp[k] = arr[r]
            r += 1
    # 복사
    for i in range(s, e + 1):
        arr[i] = tmp[i]


T = 1

for tc in range(1, T + 1):
    arr = [5, 4, 3, 2, 1]
    N = len(arr)
    tmp = [0] * N
    merge_sort(0, N - 1)
    print(tmp)
