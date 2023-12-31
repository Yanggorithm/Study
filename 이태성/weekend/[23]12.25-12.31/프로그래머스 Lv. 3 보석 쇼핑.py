def solution(gems):
    type_count = len(set(gems))  # 보석의 종류 수
    left, right = 0, 0
    answer = [0, len(gems) - 1]
    gem_map = {}  # 현재 윈도우에 있는 보석의 종류와 수를 저장

    while right < len(gems):
        # 윈도우를 오른쪽으로 확장
        if gems[right] not in gem_map:
            gem_map[gems[right]] = 0
        gem_map[gems[right]] += 1
        
        # 윈도우에서 모든 종류의 보석을 포함하는 경우
        while len(gem_map) == type_count:
            # 더 작은 길이를 찾으면 업데이트
            if right - left < answer[1] - answer[0]:
                answer = [left, right]
            
            # 윈도우를 왼쪽으로 축소
            gem_map[gems[left]] -= 1
            if gem_map[gems[left]] == 0:
                del gem_map[gems[left]]
            left += 1

        right += 1
    
    # 인덱스는 1부터 시작하므로 1을 추가
    return [answer[0] + 1, answer[1] + 1]