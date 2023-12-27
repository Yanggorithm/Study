# 프로그래머스 Lv0 정사각형으로 만들기 
def solution(arr):
    answer = []
    # 행 길이
    lenA = len(arr)
    # 열 길이
    lenB = len(arr[0])
    # 행이 더 클 때 (열의 뒤에 차잇값만큼 0채우기)
    if lenA > lenB:
        for i in range(lenA):
            answer.append(arr[i] + [0]*(lenA-lenB))
        
    # 열이 더 클 때 (열의 값만큼 0갯수로 구성된 배열을 행에 추가하기)
    elif lenA < lenB:
        for i in range(lenB-lenA):
            arr.append([0] * lenB)
        answer = arr
    else:
        answer =  arr
    return answer