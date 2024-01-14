def solution(k, room_number):
    answer = []
    lenRoom_number = len(room_number)
    dictRoom = dict()
    for idx in range(lenRoom_number):
        firstNumber = room_number[idx]
        number = dictRoom.get(firstNumber, 0)
        if number:
            temp = [firstNumber]
            while True:
                nextNumber = number
                number = dictRoom.get(number, 0)
                if not number:
                    dictRoom[nextNumber] = nextNumber + 1
                    answer.append(nextNumber)
                    for ts in temp:
                        dictRoom[ts] = nextNumber + 1
                    break
                temp.append(number)
        else:
            dictRoom[firstNumber] = firstNumber + 1
            answer.append(firstNumber)

    return answer
