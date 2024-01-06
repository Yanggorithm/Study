# 프로그래머스 성격 유형 검사하기

cal = {
    1 : 3,
    2 : 2, 
    3 : 1,
    4 : 0,
    5 : 1,
    6 : 2,
    7 : 3
}

def solution(survey, choices):
    scores = { 
        'R' : 0,
        'T' : 0,
        'C' : 0,
        'F' : 0,
        'J' : 0,
        'M' : 0,
        'A' : 0,
        'N' : 0
    }
    
    n = len(survey)
    
    for idx in range(n):
        if choices[idx] < 4:
            scores[survey[idx][0]] += cal[choices[idx]]
        else :
            scores[survey[idx][1]] += cal[choices[idx]]
            
    answer = ['T', 'F', 'M', 'N']
    
    if scores['R'] >= scores['T'] :
        answer[0] = 'R'
    
    if scores['C'] >= scores['F'] :
        answer[1] = 'C'
    
    if scores['J'] >= scores['M'] :
        answer[2] = 'J'
        
    if scores['A'] >= scores['N'] :
        answer[3] = 'A'
    
    ANSWER = ''.join(answer)
    
    return ANSWER