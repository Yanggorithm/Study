# 3차 n진수 게임

def solution(n, t, m, p):
    '''
    n = 몇 진수인지?
    t = 미리 구할 숫자의 개수
    m = 게임에 참가하는 인원
    p = 튜브의 순서
    '''
    
    # 일단 진법 변환이 우선이 되야할것같음..
    myStr = ""
    for i in range(2, m*t+1):
        changeStr = ""
        # 2부터 시작하겠음 1은 무조건 1이므로
        while True:
            a = i % n
            if a >= 10:
                if a == 10:
                    a = "A"
                if a == 11:
                    a = "B"                
                if a == 12:
                    a = "C"               
                if a == 13:
                    a = "D"                
                if a == 14:
                    a = "E"
                if a == 15:
                    a = "F"
            # 최대 16진수 이므로
            
            if i // n == 1: 
                changeStr += str(a)
                changeStr += "1"
                i = i // n
                break
            elif i // n == 0:
                changeStr += str(a)
                i = i // n
                break
            else:
                changeStr += str(a)
                i = i // n

        myStr += changeStr[::-1]

    result = "01" + myStr
    answer = result[p-1::m][:t]

    return answer