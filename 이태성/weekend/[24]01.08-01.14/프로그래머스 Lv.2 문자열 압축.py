def solution(s):
    answer = 1001
    lenS = len(s)
    if lenS == 1:
        return 1
    for cut in range(1, lenS//2+1):
        stack = []
        length = [1 for _ in range(lenS//cut+1)]
        lengthIdx = 0
        string = ""
        for idx in range(lenS):
            alpha = s[idx]
            string += alpha
            if len(string) == cut:
                if stack:
                    if stack[-1] == string:
                        length[lengthIdx] += 1
                    else:
                        stack.append(string)
                        lengthIdx += 1
                else:
                    stack.append(string)
                string = ""

        plusLength = 0
        for kdx in range(lengthIdx+1):
            nowLength = length[kdx]
            if nowLength // 1000:
                plusLength += 4
            elif nowLength // 100:
                plusLength += 3
            elif nowLength // 10:
                plusLength += 2
            elif nowLength > 1:
                plusLength += 1
        nowValue = len(stack) * cut + lenS % cut + plusLength
        if nowValue < answer:
            answer = nowValue
    
    return answer