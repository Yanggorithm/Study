import sys
input = sys.stdin.readline

"""
풀이 접근 방법1 --> 자리수가 몇자리가 될지 모름
1. n자리의 수에 1부터 9까지 넣는다.
2. 첫번째 자리 수가 정해지면 두번째 자리수는 2개 혹은 1개 밖에 들어 올 수 없다.

풀이 접근 방법 2
1. n=1일때는 각 숫자별로 1개씩
2. 각 자리수별로 끝나는 숫자에 따라 몇개인지 arr에 저장
ex) 첫번째 자리수가 0일때 뒤에 올 수 있는 수는 1 한개
    첫번째 자리수가 1일때 뒤에 올 수 있는 수는 0, 2 두개
    첫번째 자리수가 9일때 뒤에 올 수 있는 수는 8 한개
3. 2차원 배열 arr에 각 자리수별로 끝나는 수에 따라 저장하면 규칙 발견

"""
n = int(input().strip())
arr = [[0] * 10 for _ in range(n+1)]
for i in range(1, 10):
    arr[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            arr[i][j] = arr[i-1][1]
        elif 0 < j < 9:
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j+1]
        else:
            arr[i][j] = arr[i-1][8]

print(sum(arr[n]) % 1000000000)