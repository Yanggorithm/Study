numberDict = { 'zero' : '0',
'one' : '1',
'two' : '2',
'three' : '3',
'four' : '4',
'five' : '5',
'six' : '6',
'seven' : '7',
'eight' : '8',
'nine' : '9',
 }

def solution(s):
    answer = 0
    flag = 0
    
    while True:
        for i in numberDict.keys():
            print(i,s)
            if i in s:
                # 만약 딕셔너리 값이 있다면
                s = s.replace(i, numberDict[i])
                break
            else:
                if i == 'nine':
                    # 만약 없다면
                    flag = 1
                    break
            
        if flag:
            break

    return int(s)