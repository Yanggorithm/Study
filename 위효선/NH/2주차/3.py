# 프로그래머스 명예의 전당(1)

def solution(k, score):
    fame = []
    answer = []
    
    for s in score:
        if len(fame) == k:
            if min(fame) < s:
                i = fame.index(min(fame))
                fame[i] = s
        else:
            fame.append(s)
        answer.append(min(fame))
        
    return answer