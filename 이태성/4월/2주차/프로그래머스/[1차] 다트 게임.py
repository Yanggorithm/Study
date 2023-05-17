def solution(dartResult):
    # 문자열을 받아줄 배열
    mine = ["" for _ in range(3)]
    idx = -1

    # 해당 문자가 숫자면 idx에 1을 더해준다.
    for i in dartResult:
        if "0" <= i <= "9":

            if i == "0" and mine[idx] != "" and mine[idx][-1] == "1":
                mine[idx] += i
            else:
                idx += 1
                mine[idx] += i
        else:
            mine[idx] += i

    score_dict = {"S": 1, "D": 2, "T": 3}

    score = [0 for _ in range(3)]

    for i in range(3):
        if mine[i][0] == "1":
            if mine[i][1] == "0":
                score[i] += 10 ** (score_dict[mine[i][2]])
            else:
                score[i] += 1 ** (score_dict[mine[i][1]])
        else:
            score[i] += int(mine[i][0]) ** (score_dict[mine[i][1]])

    for i in range(3):
        prize = mine[i][-1]
        if prize == "*":
            if i == 0:
                score[i] *= 2
            else:
                score[i] *= 2
                score[i - 1] *= 2
        elif prize == "#":
            score[i] *= -1

    answer = sum(score)

    return answer