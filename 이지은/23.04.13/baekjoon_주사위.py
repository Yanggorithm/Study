
"""
    +---+        
    | D |        
+---+---+---+---+
| E | A | B | F |
+---+---+---+---+
    | C |        
    +---+   
현재 동일한 주사위를 N**3 개
N×N×N크기의 정육면체, 바닥면이 안보이므로, 5개의 면
보이는 5개의 면에 쓰여 있는 수의 합의 최솟값

주사위의 붙어 있는 면(2개)
A, B
A, C
A, D
A, E
B, C 
B, D 
B, F
C, E
C, F
D, E
D, F
E, F

주사위의 붙어 있는 면(3개)
A, B, C
A, B, D
A, C, E
A, D, E
B, C, F
B, D, F
C, E, F
D, E, F
"""
# 풀이 접근
# 1. 가장자리를 제외한 1 ~ n-2번째 주사위의 면은 최솟값을 보여준다.
# 2. 면의 가장자리 : 주사위 여섯개 면 중에 붙어있는 두면의 합이 가장 작은 경우 찾기
# 3. 면의 모서리 : 주사위 여섯개 면 중에 붙어 있는 세 면의 합이 가장 작은 경우 찾기
import sys
input = sys.stdin.readline

# 입력
n = int(input().strip())
a, b, c, d, e, f = map(int, input().strip().split())

# 두면이 맞닿은 경우
two = [(a, b), (a, c), (a, d), (a, e), (b, c), (b, d),
       (b, f), (c, e), (c, f), (d, e), (d, f), (e, f)]

# 세면이 맞닿은 경우
three = [(a, b, c), (a, b, d), (a, c, e), (a, d, e),
         (b, c, f), (b, d, f), (c, e, f), (d, e, f)]

# n이 1이면 육면체 중에 바닥면을 제외한 모든 면의 합
if n == 1:
    print(sum([a,b,c,d,e,f]) - max([a,b,c,d,e,f])) 
else:
    min_one = min(a, b, c, d, e, f)

    min_two = 999999999
    for t in two:
        tmp = sum(t)
        if tmp < min_two:
            min_two = tmp

    min_three = 999999999
    for t in three:
        tmp = sum(t)
        if tmp < min_three:
            min_three = tmp

    result = min_one * ((n-2) * (n-2) * 5 + (n-2)*4)
    result += (min_two*((n-2)*8+4) + min_three*4)
    print(result)
