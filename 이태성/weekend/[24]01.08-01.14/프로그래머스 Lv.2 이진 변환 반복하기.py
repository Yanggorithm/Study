def solution(s):
    string = s
    cnt = 0
    zero = 0
    while string != "1":
        cnt += 1
        zero += string.count("0")
        string = string.replace("0", "")
        lenString = len(string)
        newString = ""
        while lenString > 1:
            newString += str(lenString % 2)
            lenString //= 2
        newString += str(lenString)
        string = str(int(newString[::-1]))
    return [cnt, zero]