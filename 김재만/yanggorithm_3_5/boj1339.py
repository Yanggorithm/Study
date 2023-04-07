# 양고리즘 스터디 문제
# boj 1339 단어수학
# 완탐 안될듯 내일 다시
# 백트래킹?
# 결국 그리디
# 최대힙?
import heapq
from collections import deque
import sys
input = sys.stdin.readline


n = int(input())
num_list = [i for i in range(10)]
# 아스키 코드로 전환해서 풀자
scores = [0] * 100
check_list = []
heapq.heapify(check_list)
max_len = 0
num_dict = dict()
arr = []

for _ in range(n):
    a = list(input().strip())
    alpha_list = deque(a)
    arr.append(a[:])
    heapq.heappush(check_list, (-len(alpha_list), alpha_list))
    max_len = max(max_len, len(alpha_list))

# 알파벳당 점수를 매기자 !
score = 10**max_len
while check_list[0][0]:
    length, q = heapq.heappop(check_list)
    while check_list and check_list[0][0] == length:
        big_alpha = q.popleft()
        length += 1
        heapq.heappush(check_list, (length, q))
        length, q = heapq.heappop(check_list)
        scores[ord(big_alpha)] += score
    big_alpha = q.popleft()
    length += 1
    scores[ord(big_alpha)] += score
    heapq.heappush(check_list, (length, q))
    score //= 10

    print(check_list)
    print(scores)
# 여기서 그리디 진행
# 이후 점수순으로 9 ~ 0 까지 dictionary 만들자
while True:
    max_idx = scores.index(max(scores))
    if not max(scores):
        break
    else:
        num_dict[chr(max_idx)] = num_list.pop()
        scores[max_idx] = 0

# dictionary 완성
# 이제 매치 시켜서 계산하면 끝
result = 0
for l in arr:
    new_list = []
    for i in l:
        new_list.append(str(num_dict[i]))
    
    result += int("".join(new_list))

print(result)