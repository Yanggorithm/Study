def solution(new_id):
    import re

    answer=''
    answer = re.sub('[^a-z\d\_\-\.]','',new_id.lower())  #1,2 단계
    #re.sub('찾을패턴','변경내용','원본')

    answer = re.sub('\.\.+','.',answer) #3단계 ..이 연속되면 한개로만 바꿔
    answer= re.sub('^\.','',answer) #4단계 처음에 .있으면 제거
    answer = re.sub('\.$','', answer[:15]) #6,4단계 끊어놓고나서 뒤에.있다면 제거; 먼저 제거하고 끊으면 제거한뒤에 .있는경우 못찾음
    if answer=="":
        answer="a"

    if len(answer)<=2: #7단계
        while len(answer)<3:
            answer= answer + answer[-1]
    return answer