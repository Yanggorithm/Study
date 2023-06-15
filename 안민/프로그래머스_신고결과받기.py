def solution(id_list, report, k):
    lst = []
    answer = []

    dict = {}  # 신고한 놈, 신고당한 놈이 중복되면 안되게 하려고
    break_dict = {}  # 쪼갠거(신고한놈/당한놈)
    check_dict = {}  # 신고 몇번당했는지
    for i in report:
        if i not in dict:
            dict[i] = 1  # 신고한 놈들 각각 다른놈들뿐임 이제

    for j in dict:
        key = j.split(" ")[0]
        value = j.split(" ")[1]
        if value in break_dict:
            break_dict[value].append(key)
        else:
            break_dict[value] = [key]
    # 신고당한놈이 key, 신고한 놈이 value

    for l in dict:
        check = l.split(" ")[1]
        if check in check_dict:
            check_dict[check] += 1
        else:
            check_dict[check] = 1
    # 신고 몇번 당했는지 파악

    for z in check_dict:
        if (check_dict[z]) >= k:  # 만약 신고 k번 이상 당했으면
            doer = break_dict[z]  # 신고한 놈 찾아서 알려야함
            lst.append(doer)
    # print(lst)

    for m in id_list:
        answer.append(0)

    for c in lst:  # 어차피 신고는 최소 두명한테 받음
        for real in c:  # 신고한놈 하나씩 떼서 real로 보내자
            answer[id_list.index(real)] += 1
    return (answer)