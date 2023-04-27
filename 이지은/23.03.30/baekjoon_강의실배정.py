from heapq import heappop, heappush
import sys

n = int(sys.stdin.readline().strip())
cnt = 0

lecture = []
for i in range(n):
    lecture.append(tuple(map(int, sys.stdin.readline().strip().split())))

lecture.sort()

room = []
heappush(room, lecture[0][1])

for i in range(1, n):
    if room[0] > lecture[i][0]:
        heappush(room, lecture[i][1])
    else:
        heappop(room)
        heappush(room, lecture[i][1])

print(len(room))

# 시간이 겹치는지 확인
    # 시간이 겹치면, 다른 강의실 배정
# 시간이 겹치지 않으면 해당 강의실에 배정

# 내 코드의 문제점 : 한 강의실에 겹치는 지만 확인하고 있다
# 추가된 강의실에서도 겹치는지 안겹치는 지 확인 어떻게 해??
    
"""
ex)
3
1 3
2 4
3 5

==> [(1, 3), (2, 4), (3, 5)]
1   2   3   4   5   
|///|///|   |   |   |
|   |///|///|   |   |
|   |   |///|///|   |

heapq
[3]
[3, 4]
[4, 5]

5
1 4
2 4
1 3
4 5
7 9
==> [(1,3), (1,4), (2, 4), (4, 5), (7, 9)]
0   1   2   3   4   5   6   7   8   9   10  11  
|   |///|///|///|   |   |   |   |   |   |   |
|   |   |///|///|   |   |   |   |   |   |   |
|   |///|///|   |   |   |   |   |   |   |   |
|   |   |   |   |///|   |   |   |   |   |   |

heapq
[3]
[3, 4]
[3, 4, 4]
[4, 4, 5]


"""