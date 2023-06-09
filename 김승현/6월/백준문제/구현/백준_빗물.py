import sys
input = sys.stdin.readline

N, M = map(int, input().split())

rain = list(map(int, input().split()))

# 첫번째 값을 저장후 다음값이 저장한 값보다 큰 값이 나올때까지
# 리스트에 저장을 함
# 값이 나오면 이전에 리스트에 저장한 값 중 큰 값을 찾아서
# 계산을 함

# 끝까지 나오지않으면 마지막값과 비교하여서 계산

temp = []
max_v = rain[0]
cnt = 0

# 모든 경우를 비교해서 값을 확인
for i in range(M):
    if i == M - 1:
        if rain[i] > max_v:
            for j in range(len(temp)):
                cnt += max_v - temp[j]
        else:
            temp.append(rain[i])
            max_temp = max(temp)
            for j in range(len(temp)):
                cnt += max_temp - temp[j]
    else:
        if rain[i] > max_v:
            max_v = rain[i]
            if temp:
                max_temp = max(temp)
                for j in range(len(temp)):
                    cnt += max_temp - temp[j]

                temp = []

        else:
            temp.append(rain[i])


print(cnt)
