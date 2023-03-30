# 병합정렬 구현
def merge(s, e):
    middle = (s + e) // 2
    left, right = s, middle + 1
    for k in range(s, e+1):
        # 왼쪽 부분만 남았다면? => 오른쪽이 이미 끝에 도달했다.
        if right > e:
            tmp[k] = arr[left]
            left += 1
        # 오른쪽 부분만 남았다면? => 왼쪽이 이미 끝에 도달했다.
        elif left > middle:
            tmp[k] = arr[right]
            right += 1
        # 왼쪽에 있는 값이 더 클때 정렬을 위해 오른쪽 값을 사용
        elif arr[left] > arr[right]:
            tmp[k] = arr[right]
            right += 1
        # 반대 경우 왼쪽값 사용
        else:
            tmp[k] = arr[left]
            left += 1

    # 복사
    for i in range(s, e + 1):
        arr[i] = tmp[i]


def merge_sort(start, end):
    if start == end:
        return

    # 분할
    middle = (start + end) // 2

    # 정복
    if middle == 0:
        return
    print(start, middle, end)
    merge_sort(start, middle-1)
    merge_sort(middle, end)

    # 결합
    merge(start, end)
    return


T = 1

for tc in range(1, T + 1):
    arr = [5, 4, 3, 2, 1]
    N = len(arr)
    tmp = [0] * N
    merge_sort(0, N - 1)
    print(arr)
