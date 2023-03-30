# 퀵정렬
def partition(A, l, r):
    pivot = A[l]
    i = l  # 피봇보다 큰값을 찾아 오른쪽으로 이동
    j = r  # 피봇보다 작은 값을 찾아 왼쪽으로 이동
    while i <= j:
        while i <= j and A[i] <= pivot:
            i += 1
        while i <= j and A[j] >= pivot:
            j -= 1
        if i < j:  # 교차하지 않은 경우
            A[i], A[j] = A[j], A[i]

    A[j], A[l] = A[l], A[j]
    return j


def qsort(A, l, r):
    if l < r:
        p = partition(A, l, r)
        qsort(A, l, p - 1)
        qsort(A, p + 1, r)


T = 1

for tc in range(1, T + 1):
    N = 5
    arr = [5, 4, 3, 2, 1]
    qsort(arr, 0, N - 1)
    print(arr)
