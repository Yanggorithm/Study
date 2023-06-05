def solution(today, terms, privacies):
      # 오늘 날짜, 약관 유효기간 배열, 개인정보의 정보 배열
    answer = []
    
    # 약관종류별 유효기간 딕셔너리 생성
    terms_dict = {}
    for term in terms:
        a, b = term.split()
        terms_dict[a] = int(b)

    # 오늘 날짜
    ty, tm, td = map(int, today.split("."))
    for i in range(len(privacies)):
        
        c, d = privacies[i].split()
        year, month, day = map(int, c.split('.'))
        
# 날짜 계산
        if month+terms_dict[d] > 12:
            year += terms_dict[d]//12
            if terms_dict[d] % 12 + month > 12:
                year += 1
                month = terms_dict[d] % 12 + month - 12
            else:
                month += terms_dict[d] % 12
        else:
            month += terms_dict[d]
        
        ty, tm, td = map(str, [ty, tm, td])
        if len(tm) == 1:
            tm = '0'+tm
        
        if len(td) == 1:
            td = '0'+td
            
        year, month, day = map(str, [year, month, day])
        
        if len(month) == 1:
            month = '0'+month
            
        if len(day) == 1:
            day = '0'+day
        
        today = ty+tm+td
        d_day = year+month+day
        
        print(today, d_day)
        if today >= d_day:
            answer.append(i+1)
        
    return answer
