# 프로그래머스 PCCE 기출 10번 데이터 분석

def solution(data, ext, val_ext, sort_by):
    check = {
        "code" : 0,
        "date" : 1,
        "maximum" : 2,
        "remain" : 3
    }
    
    return sorted([ x for x in data if x[check[ext]] < val_ext ], key = lambda x : x[check[sort_by]])