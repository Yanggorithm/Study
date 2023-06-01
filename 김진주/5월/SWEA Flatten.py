import sys
sys.stdin = open('input.txt', 'r')

# 높은 곳 상자를 낮은 곳에 옮기기, 가장 높은 곳과 가장 낮은 곳의 차이는 <= 1
# 제한된 횟수만큼 옮기고 최고점과 최저점의 차이를 반환

T = 10
for tc in range(1, T+1):
    N = int(input())
    height = list(map(int, input().split()))
    ans = 0

    # 덤프 횟수만큼 반복
    for _ in range(N):
        # max 찾아서 -1
        for i in range(len(height)):
            if height[i] == max(height):
                height[i] = height[i]- 1
                break
        # min 찾아서 +1
        for j in range(len(height)):
            if height[j] == min(height):
                height[j] = height[j] + 1
                break

    # 덤프 완료 후 최대와 최소 차이 반환
    ans = max(height) - min(height)

    print(f"#{tc} {ans}")