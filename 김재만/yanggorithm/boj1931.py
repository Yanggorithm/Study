# 양고리즘 스터디
# 문제 풀이
# 회의실 배정

n = int(input())
se_list = []

for _ in range(n):
    start, end = map(int, input().split())
    se_list.append([start, end])

se_list.sort(key=lambda x : (x[1],x[0]))
cnt = 1
end_time = se_list[0][1]

for i in range(1,n):
    start_time = se_list[i][0]
    if start_time >= end_time:
        cnt += 1
        end_time = se_list[i][1]

print(cnt)