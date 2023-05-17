def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        tmp = str(arr1[i] | arr2[i])
        ans = ""
        for j in range(n):
            if tmp[j] == "1":
                ans += "#"
            else:
                ans += " "
        answer.append(ans)
    return answer

solution()