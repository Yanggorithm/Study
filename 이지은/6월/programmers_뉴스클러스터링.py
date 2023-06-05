def make_lst(str1):
    lst = []
    for i in range(len(str1)-1):
        is_alpha = True
        tmp = str1[i:i+2]
        for j in tmp:
            if 'A' <= j <= 'Z':
                pass
            else:
                is_alpha = False
        if is_alpha:
            lst.append(tmp)
    return lst

def count_lst(lst1):
    lst_dict = {}
    for l in lst1:
        lst_dict[l] = lst1.count(l)
    return lst_dict

def solution(str1, str2):
    answer = 0
#     자카드 유사도: J(A, B) : 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값
# 두 집합 모두 공집합일 경우 : J(A,B) = 1

# str1, str2를 두글자씩 끊어서 다중 집합의 원소로 만든다.
# 알파벳 외의 글자 무시, 대소문자 차이 무시

    str1 = str1.upper()
    str2 = str2.upper()
    
    lst1 = make_lst(str1)
    lst2 = make_lst(str2)
    
    if lst1==[] and lst2==[]:
        answer = 1*65536
    elif lst1 == [] or lst2 ==[]:
        answer = 0
    else:
        dict1 = count_lst(lst1)
        dict2 = count_lst(lst2)

        hap = 0
        gyo = 0

        for i in dict1.keys():
            if dict2.get(i):
                hap += max(dict2[i], dict1[i])
                gyo += min(dict2[i], dict1[i])
            else:
                hap += dict1[i]
                
        for i in dict2.keys():
            if not dict1.get(i):
                hap += dict2[i]
                
        answer = int(65536*gyo/hap)
    return answer