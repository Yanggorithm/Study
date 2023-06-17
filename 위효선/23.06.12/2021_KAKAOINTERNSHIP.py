# LV.1 숫자 문자열과 영단어

def solution(s):

    n = len(s)
    t = 0
    answer = ''
    while t < n:

        if s[t].isdigit():
            answer += s[t]
            t += 1
        else:
            if s[t] == 'z':
                answer += '0'
                t += 4
            elif s[t] == 'o':
                answer += '1'
                t += 3
            elif s[t] == 't':
                if s[t+1] == 'w':
                    answer += '2'
                    t += 3
                else:
                    answer += '3'
                    t += 5
            elif s[t] == 'f':
                if s[t+1] == 'o':
                    answer += '4'
                    t += 4
                else:
                    answer += '5'
                    t += 4
            elif s[t] == 's':
                if s[t+1] == 'i':
                    answer += '6'
                    t += 3
                else:
                    answer += '7'
                    t += 5
            elif s[t] == 'e':
                answer += '8'
                t += 5
            else:
                answer += '9'
                t += 4
    return int(answer)

number_dict = {'one' : '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9', 'zero' : '0'}

def solution2(s):
    
    for key in number_dict.keys():
        s = s.replace(key, number_dict[key])
    
    return int(s)