# 프로그래머스 대충 만든 자판

def solution(keymap, targets):
    
    key_book = {}
    for key in keymap:
        for i, x in enumerate(key):
            if x not in key_book:
                key_book[x] = i+1
            else:
                key_book[x] = min(key_book[x], i+1)
    
    answer = []    
    for target in targets:
        cnt = 0
        for x in target:
            if x not in key_book:
                cnt = -1
                break
            cnt += key_book[x]
        answer.append(cnt)
    
    return answer