def solution(s):
    lst = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    # enumerate를 사용히면 리스트의 인덱스와 동일한 값처럼
    # 순서가 0부터 출력되므로 인덱스로 이용하기 편하다.
    for i, word in enumerate(lst):
        if word in s:
            # replace는 두 요소 모두 str이어야 사용가능하다.
            s = s.replace(word, str(i))

    return int(s)

s = "one4seveneight"
# 다른 테스트케이스
# s = "23four5six7"
# s = "2three45sixseven"
# s = "123"

