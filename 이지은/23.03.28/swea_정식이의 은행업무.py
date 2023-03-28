t = int(input())

for tc in range(1,t+1):
    a = list(input())
    b = list(input())

    # 한자리씩 싹다 바꾼수를 각각 배열에 넣는다.
    # 두 배열을 비교해서 같은 수를 찾는다.
    result = []
    for i in range(len(a)):
        # 한자리 바꾸기
        if a[i] == '1':
            a[i] = '0'
        elif a[i] == '0':
            a[i] = '1'

        # 십진수 구하기
        tmp = 0
        for j in range(len(a)):
            if a[::-1][j]  == '1':
                tmp += 2**j
        result.append(tmp)

        # 바꾼자리 복구
        if a[i] == '1':
            a[i] = '0'
        elif a[i] == '0':
            a[i] = '1'

    # print(result)
    result2 = []
    for i in range(len(b)):
        if b[i] == "1":
            b[i] = '0'
            tmp = 0
            for j in range(len(b)):
                if b[::-1][j]!='0':
                    tmp += int(b[::-1][j])*(3**j)
            result2.append(tmp)
            b[i] = '2'
            tmp = 0
            for j in range(len(b)):
                if b[::-1][j]!='0':
                    tmp += int(b[::-1][j])*(3**j)
            result2.append(tmp)

            b[i] = '1'
        elif b[i] == "2":
            b[i] = '0'
            tmp = 0
            for j in range(len(b)):
                if b[::-1][j]!='0':
                    tmp += int(b[::-1][j])*(3**j)
            result2.append(tmp)
            b[i] = '1'
            tmp = 0
            for j in range(len(b)):
                if b[::-1][j]!='0':
                    tmp += int(b[::-1][j])*(3**j)
            result2.append(tmp)

            b[i] = '2'
        else:
            b[i] = '2'
            tmp = 0
            for j in range(len(b)):
                if b[::-1][j]!='0':
                    tmp += int(b[::-1][j])*(3**j)
            result2.append(tmp)
            b[i] = '1'
            tmp = 0
            for j in range(len(b)):
                if b[::-1][j]!='0':
                    tmp += int(b[::-1][j])*(3**j)
            result2.append(tmp)

            b[i] = '0'
    # print(result2)
    
    for v in result:
        if v in result2:
            print(f"#{tc} {v}")
            break