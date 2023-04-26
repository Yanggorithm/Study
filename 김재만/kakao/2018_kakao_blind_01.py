# 2018 카카오 블라인드 테스트 1차 - 다트게임

def solution(dartResult):
    # 숫자는 3개이므로 값을 저장해둘 공간을 마련한다.
    dp = [-1,-1,-1]
    
    # 몇번째 값에 넣을지 정해주려고 변수 선언
    cnt = 0
    
    # 10인지 아닌지 확인하기 위한 변수 선언
    flag = 0
    
    for idx in range(len(dartResult)):
        # 전에 확인 했을때 들어온 값이 10이 아니었다고한다면 ? 아래 코드를 돌아라
        if not flag:
            # 들어온 값이 숫자이고, 다음값이 숫자가 아니면 => 즉 1자리수 1~9 이면 아래쪽 계산
            if dartResult[idx].isdigit() and not dartResult[idx+1].isdigit():
                dp[cnt] = int(dartResult[idx])
                cnt += 1
                flag = 0
            # S를 만나면 현재 점수 그대로 이므로 그냥 패스
            elif dartResult[idx] == "S":
                pass
            # D를 만나면 현재 점수의 제곱
            elif dartResult[idx] == "D":
                dp[cnt-1] = dp[cnt-1] ** 2
            # T를 만나면 현재 점수의 3제곱
            elif dartResult[idx] == "T":
                dp[cnt-1] = dp[cnt-1] ** 3
            # 이전 점수, 현재 점수 2배
            elif dartResult[idx] == "*":
                dp[cnt-1] = dp[cnt-1] * 2
                dp[cnt-2] = dp[cnt-2] * 2
            # 현재 점수 - 로 변환
            elif dartResult[idx] == "#":
                dp[cnt-1] = dp[cnt-1] * (-1)
            # 숫자가 10이라면?
            else:
                flag = 1
        # 10 일 때 계산하기 위해 아래쪽을 돌아라.
        else:
            dp[cnt] = 10
            cnt += 1
            flag = 0
    
    # 값을 다 계산 했으면 총점을 구하자
    answer = sum(dp)

    return answer