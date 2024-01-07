def solution(arr1, arr2):
    lenColumn1 = len(arr1[0])
    lenArr1 = len(arr1)
    lenColumn2 = len(arr2[0])
    answer = [[] for _ in range(lenArr1)]
    for idx in range(lenArr1):
        nowList = arr1[idx]
        for jdx in range(lenColumn2):
            nowV = 0
            nextList = []
            for kdx in range(lenColumn1):
                nextList.append(arr2[kdx][jdx])

            for ldx in range(lenColumn1):
                nowV += nowList[ldx] * nextList[ldx]
            answer[idx].append(nowV)
    return answer
