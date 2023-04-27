A = [5, 4, 3, 2, 1]

tmp = [0] * len(A)

def mergeSort(left, right):

    # 종료 조건 ( 왼쪽, 오른쪽이 같으면 원소가 1개 )
    if left == right:
        return
    
    # 분할
    mid = (left + right)//2

    # 정복
    mergeSort(left, mid)
    mergeSort(mid+1, right)

    # 결합
    # 왼쪽 부분, 오른쪽 부분의 시작 인덱스
    l, r = left, mid + 1

    # 임시 배열에 놓을 기준 위치 k
    # 우리가 보고 있는 배열의 범위는 left ~ right
    for k in range(left, right+1):
        # 왼쪽 부분만 남은 경우 : 왼쪽 배열 남은거 추가
        if r > right:
            tmp[k] = A[l]
            l += 1
        # 오른쪽 부분만 남은 경우 : 오른쪽 배열 남은거 추가
        elif l > mid:
            tmp[k] = A[r]
            r += 1

        # 둘다 남아있다
        # 왼쪽이 작으면 왼쪽거 추가
        elif A[l] <= A[r]:
            tmp[k] = A[l]
            l += 1
        # 오른쪽이 작으면 오른쪽거 추가
        else:
            tmp[k] = A[r]
            r += 1
    
    # 복사
    for i in range(left, right + 1):
        A[i] = tmp[i]

mergeSort(0, 4)
print(A)