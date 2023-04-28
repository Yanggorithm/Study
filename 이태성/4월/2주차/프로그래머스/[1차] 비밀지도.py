def solution(n, arr1, arr2):
    answer = []

    def bin_solve(num):
        binary = ""
        while num > 1:
            binary += str(num % 2)
            num //= 2
        binary += str(num)
        if len(binary) < n:
            new_binary = "0" * (n - len(binary)) + binary[::-1]
            return new_binary
        return binary[::-1]

    for i in range(n):
        line1 = bin_solve(arr1[i])
        line2 = bin_solve(arr2[i])
        new_line = ""
        for j in range(n):
            if line1[j] == "1" or line2[j] == "1":
                new_line += "#"
            else:
                new_line += " "
        answer.append(new_line)

    return answer