# 개인정보 수집 유효기간

def solution(today, terms, privacies):
    today_y, today_m, today_d = map(int, today.split("."))
    answer = []
    
    # 종류에 따른 파기 유효기간 정보 딕셔너리로 만들어두기 
    # key : 종류 이름, value : 유효기간
    check_dict = dict()
    for term in terms:
        key, val = term.split()
        check_dict[key] = int(val)
        
    # 고객들의 발급 일자와 파기 기간 종류 코드를 고객 하나 하나 들어올때 바로 비교
    for i in range(len(privacies)):
        priv = privacies[i]
        date_val, type_val = priv.split()
        target_y, target_m, target_d = map(int, date_val.split("."))
        
        # 결과를 일단위로 정확하게 비교 모든달은 28일까지 있다고 가정했으므로 아래식으로 계산
        calc_v  = 0
        calc_v += (today_y - target_y) * 12 * 28
        calc_v += (today_m - target_m) * 28
        calc_v += (today_d - target_d)
        
        # 고객들의 파기기간 종류코드에 따른 유효기간과 현재 날짜에서 발급일자 차이 값을 비교
        # 파기될 인덱스값만 answer에 저장하여 넘기는데 1번부터 시작하므로 +1해줌
        if check_dict[type_val] * 28 <= calc_v:
            answer.append(i+1)

    return answer
