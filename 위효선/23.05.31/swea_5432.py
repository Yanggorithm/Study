# SWEA_5432 쇠막대기 자르기    
T = int(input())
for TC in range(1,T+1):
    info = list(input())
    n = len(info)

    cnt = 0
    tmp = 0
    for i in range(n-1):
        # 레이저인지 확인
        if info[i] == '(' and info[i+1] == ')':
            cnt += tmp
        # 쇠막대기 시작 지점 확인
        elif info[i] == '(' :
            tmp += 1
        # 쇠막대기 끝 지점 확인
        elif info[i] == ')' and info[i-1] == ')' :
            tmp -= 1
            cnt += 1
    
    print(f'#{TC}', cnt)

'''
위와 같이 풀었는데, 제출하고나서 이게 된다고?? 싶었습니다...
왠지 반례가 있을 거 같다는 생각에 교수님 풀이를 찾아보니 아래의 풀이가 훨씬 직관적이라는 생각이 들었습니다.
다만, 위의 풀이에 오류가 있는지 있다면 구체적으로 무엇인지 궁금하여 스터디원들과 공유하고 싶었습니다!
'''

# T = int(input())
# for test_case in range(1, T + 1):
#     st = input()
#     ans = cnt = 0
#     for i in range(len(st)):
#         if st[i]=='(':      # 막대기 시작 또는 레이저표시
#             cnt += 1
#         else:               # ')'  바로 앞의 기호를 확인해야 함
#             if st[i-1]=='(':# 레이저
#                 cnt -= 1
#                 ans += cnt
#             else:           # 막대기의 끝
#                 cnt -= 1
#                 ans += 1
 
#     print(f'#{test_case} {ans}')