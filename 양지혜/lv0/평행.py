def solution(dots):
    answer = 0
    # 값 할당하기
    [[x1,y1],[x2,y2],[x3,y3],[x4,y4]] = dots
    # 각 선의 기울기 구하기
    linA = abs(x2-x1) / abs(y2-y1)
    linB = abs(x4-x3) / abs(y4-y3)
    # 기울기가 같으면 평행이므로
    if linA == linB:
        answer = 1
    return answer