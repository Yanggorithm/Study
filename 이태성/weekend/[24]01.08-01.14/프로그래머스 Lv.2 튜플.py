def solution(s):
    answer = []
    
    newS = s.split("},{")
    newS[0] = newS[0][2:]
    newS[-1] = newS[-1][:-2]

    stack = []
    for smallS in newS:
        stack.append(list(map(int, smallS.split(","))))
    stack.sort(key=lambda x:len(x))
    
    V = [0 for _ in range(100001)]
    for lstS in stack:
        for l in lstS:
            if V[l]:
                continue
            V[l] = 1
            answer.append(l)
    
    return answer