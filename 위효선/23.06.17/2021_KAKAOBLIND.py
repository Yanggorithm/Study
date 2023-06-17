# 2021_KAKAOBLIND_ID

can = ['-', '_', '.']

def solution(new_id):

    answer = tmp = ''

    # 1단계
    new_id = new_id.lower()

    # 2단계
    for letter in new_id:
        if (letter.isalpha() or letter.isdigit() or letter in can):
            tmp += letter

    # 3단계
    n = len(tmp)
    answer += tmp[0]
    t = 1
    while t < n:
        if tmp[t] != '.':
            answer += tmp[t]
            t += 1
        else:
            if answer[-1] != '.':
                answer += tmp[t]
                t += 1
            else:
                t += 1
    
    # 4단계
    if answer[0] == '.':
        answer = answer[1:]
    if answer and answer[-1] == '.':
        answer = answer[:-1]
    
    # 5단계
    if not answer:
        answer = 'a'
    
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    # 7단계
    if len(answer) <= 2:
        if len(answer) == 1:
            answer += answer[-1] * 2
        else:
            answer += answer[-1]
    
    return answer