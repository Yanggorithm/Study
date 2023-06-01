def solution(new_id):
    first = new_id.lower()
    # print(first)

    second = ""
    for i in list(first):
        if i.isdigit() or i.isalpha() or i in ('-', '_', '.'):
            second += i
    # print(second)

    third = ""
    temp = []
    for j in list(second):
        if j == '.':
            temp.append('.')
        else:
            if temp:
                third += '.'
                temp = []
            third += j
    if second[-1] == '.':
        third += '.'
    # print(third)

    fourth = ""
    if list(third)[0] == '.':
        fourth = list(third)[1:]
    else:
        fourth = third
    fourth = ''.join(fourth)
    # print(fourth)

    fifth = ""
    if fourth == "":
        fifth = 'a'
    else:
        fifth = fourth
    # print(fifth)

    six = ""
    if len(fifth) >= 16:
        six = list(fifth)[:15]
    else:
        six = fifth

    if list(six)[-1] == '.':
        six = list(six)[:-1]
    six = ''.join(six)
    # print(six)

    seven = ""
    if len(six) < 3:
        while len(six) < 3:
            six += list(six)[-1]

    seven = six

    return seven