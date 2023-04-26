# # 2018 카카오 블라인드 테스트 1차 - 비밀지도

def solution(n, arr1, arr2):
    answer = ["" for _ in range(n)]
    
    secret_map = [[0] * n for _ in range(n)]
    
    line = 0
    
    for i in arr1:
        str = ""
        for j in range(n-1,-1,-1):
            if i & 1 << j:
                str += "1"
            else:
                str += "0"
        
        for k in range(len(str)):
            if str[k] == "1":
                secret_map[line][k] = 1
        
        line += 1
    
    line = 0
    
    for i in arr2:
        str = ""
        for j in range(n-1,-1,-1):
            if i & 1 << j:
                str += "1"
            else:
                str += "0"
        
        for k in range(len(str)):
            if str[k] == "1":
                secret_map[line][k] = 1
        
        line += 1
    
    # print(secret_map)
    
    for idx in range(len(secret_map)):
        for value in secret_map[idx]:
            if value:
                answer[idx] += "#"
            else:
                answer[idx] += " "
                
        
    
    return answer