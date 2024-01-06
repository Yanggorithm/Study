# 프로그래머스 햄버거 만들기

# def solution(ingredient):
#     hamburger = 0
#     lst = []
#     for i in ingredient:
#         lst.append(i)
#         if lst[-4:] == [1, 2, 3, 1] :
#             lst = lst[:-4]
#             hamburger += 1
#     return hamburger

def solution(ingredient):
    hamburger = 0
    lst = []
    for i in ingredient:
        lst.append(i)
        if lst[-4:] == [1, 2, 3, 1] :
            hamburger += 1
            # del lst[-4:]
            for _ in range(4):
                lst.pop()
    return hamburger