def solution(N, stages):
    answer = []

# 실패율 : 스테이지에 도달했으나 아직 클리어하지 못한 플레이어수 / 스테이지에 도달한 플레이어 수
# N : 전체 스테이지의 개수
# stages : 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호
# 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열

# 해당 단계에 도달한 사람
    reach = [0] * (N+2)
# 해당 단계에 머무르는 사람
    stay = [0] * (N+2)
    
    for stage in stages:
        for i in range(1, stage+1):
            reach[i] += 1
        stay[stage] += 1

    fail = [0] * (N+2)
    for i in range(len(stay)):
# DivisionByZero Error 방지
        if reach[i]:
            fail[i] = stay[i]/reach[i]
        else:
            fail[i] = 0

    tmp = []
    for i in range(1, N+1):
        tmp.append((fail[i], i))

# 정렬
    tmp = sorted(tmp, key=lambda x: (-x[0], x[1]))
    
    for i in range(N):
        answer.append(tmp[i][1])
    return answer