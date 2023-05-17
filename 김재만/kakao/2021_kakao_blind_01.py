# 신규 아이디 추천
# 구현 문제

def solution(new_id):
    # 1단계
    new_id_1 = new_id.lower()
    
    new_id_2 = ""
    prev = ""
    for char in new_id_1:
        # 2단계
        if not char in ['-', '_', '.'] and ('a' > char or char > 'z') and not char.isdigit():
            continue
        # 3단계
        if char == '.' and prev == '.':
            continue
        new_id_2 += char
        prev = char
    # 4단계
    new_id_4 = new_id_2.strip(".")
    # 5단계
    if not new_id_4: 
        answer = "aaa"
        return answer
    
    # 6단계
    if len(new_id_4) >= 16:
        new_id_6 = new_id_4[:15].rstrip('.')
        return new_id_6
    
    # 7단계
    if len(new_id_4) <= 2:
        while len(new_id_4) != 3:
            new_id_4 += new_id_4[-1]
        answer = new_id_4
        return answer
    
    answer = new_id_4
    return answer