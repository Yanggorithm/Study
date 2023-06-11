def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()

    dic1 = dict()
    dic2 = dict()

    kyo = 0

    for i in range(len(str1) - 1):
        tmp = (str1[i:i + 2])
        if tmp.isalpha():
            if tmp in dic1:
                dic1[(str1[i:i + 2])] += 1
            else:
                dic1[tmp] = 1

    for j in range(len(str2) - 1):
        tmp = (str2[j:j + 2])
        if tmp.isalpha():
            if tmp in dic2:
                dic2[tmp] += 1
            else:
                dic2[tmp] = 1

    for i in dic2:
        if i in dic1:
            kyo += min(dic1.get(i), dic2.get(i))  # dic1이랑 dic2랑 비교해서 어느쪽에 더 적게있는지! 적게있는게 교집합개수

    hap = sum(dic1.values()) + sum(dic2.values()) - kyo  # 합집합은 dic1+dic2-교집합
    if hap == 0:  # 문자가 아예 똑같은 경우 (예시4)
        answer = 65536
    else:
        answer = int((kyo / hap) * 65536)
    return answer