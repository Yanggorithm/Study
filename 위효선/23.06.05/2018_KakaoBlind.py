# 2018 KAKAO BLIND NEWS CLUSTERING

def solution(str1, str2):
    A = dict()
    B = dict()

    a = b = 0

    for i in range(len(str1)-1):
        tmp = str1[i:i+2].lower()
        if tmp.isalpha():
            a += 1
            if not A.get(tmp):
                A[tmp] = 1
            else:
                A[tmp] += 1
        
    for i in range(len(str2)-1):
        tmp = str2[i:i+2].lower()
        if tmp.isalpha(): 
            b += 1
            if not B.get(tmp):
                B[tmp] = 1
            else:
                B[tmp] += 1

    if a == b == 0:
        return 65536
    
    c = 0
    
    for key in A.keys():
        if B.get(key):
            c += min(A.get(key), B.get(key))

    return int(c / (a+b-c) * 65536)