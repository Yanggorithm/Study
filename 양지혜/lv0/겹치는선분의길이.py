def solution(lines):
    answer = 0
    [[a1,a2],[b1,b2],[c1,c2]] = lines
    # 점의 범위를 리스트에 넣기
    lineA = list(i for i in range(a1,a2))
    lineB = list(i for i in range(b1,b2))
    lineC = list(i for i in range(c1,c2))
    # 교집합 구하기
    inAB = [i for i in lineA if i in lineB]
    inBC = [i for i in lineB if i in lineC]
    inAC = [i for i in lineA if i in lineC]

    # 합집합 구하기
    dset = list(set(inAB+inAC+inBC))
    print(dset)
    answer = len(dset)

    return answer