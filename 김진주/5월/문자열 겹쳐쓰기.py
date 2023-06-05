def solution(my_string, overwrite_string, s):
    answer = ''

    # s-1까지는 ""에 저장
    # 나머지는 붙이기

    head = my_string[:s]
    tail = overwrite_string

    answer = head + tail

    m_l = len(my_string)
    o_l = len(overwrite_string)
    a_l = len(answer)

    if m_l > (s + o_l):
        gap = m_l - (s + o_l)
        answer += my_string[-gap::]

    return answer