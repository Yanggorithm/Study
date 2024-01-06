# 프로그래머스 이상한 문자 만들기

def solution(s):
    answer = ''
    lst = s.split(' ')
    for word in lst:
        for j, letter in enumerate(word):
            if j%2 :
                answer += letter.lower()
            else :
                answer += letter.upper()
        answer += ' '
    return answer[0:-1]