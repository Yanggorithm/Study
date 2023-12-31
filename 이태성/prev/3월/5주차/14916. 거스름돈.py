n = int(input())
cnt = n//5
remain = n % 5
# 1인 경우 2인 경우 3인 경우 4인 경우
if n > 5:
    if remain == 1:
        cnt -= 1
        cnt += 3
    elif remain == 2:
        cnt += 1
    elif remain == 3:
        cnt -= 1
        cnt += 4
    elif remain == 4:
        cnt += 2
else:
    if remain == 1:
        cnt -= 1
    elif remain == 2:
        cnt += 1
    elif remain == 3:
        cnt -= 1
    elif remain == 4:
        cnt += 2
print(cnt)