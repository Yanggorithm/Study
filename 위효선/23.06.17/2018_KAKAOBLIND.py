# 2018_KAKAOBLIND_N

num_dic = {'10' : 'A', '11' : 'B', '12' : 'C', '13' : 'D', '14' : 'E', '15' : 'F'}

def solution(n, t, m, p):

    talk = []
    answer = ''
    num = -1
    while len(talk) < t*m:
        num += 1
        save = num 
        if num < n:
            plus = num_dic[str(num)] if num_dic.get(str(num)) else str(num)
            talk += plus
        else: 
            tmp = ''
            while num >= n:
                if num_dic.get(str(num%n)) :
                    tmp += num_dic[str(num%n)]
                else : 
                    tmp += str(num % n)
                num //= n
            tmp += num_dic[str(num)] if num_dic.get(str(num%n)) else str(num)
            tmp = tmp[::-1]
            talk += tmp
            num = save 
    
    p -= 1    
    while len(answer) < t:
        answer += talk[p]
        p += m
    return answer