from collections import deque 
def solution(begin, target, words):
    lenWords = len(words)
    lenW = len(begin)
    V = [0 for _ in range(lenWords+1)]
    q = deque()
    q.append((begin, lenWords))
    result = 1e9
    isFound = False
    while q:
        currentWord, currentIdx = q.popleft()
        if currentWord == target:
            isFound = True
            if result > V[currentIdx]:
                result = V[currentIdx]
            continue
        for nextIdx in range(lenWords):
            if nextIdx == currentIdx:
                continue
            word = words[nextIdx]
            cnt = 0
            for j in range(lenW):
                if currentWord[j] != word[j]:
                    cnt += 1
            # 하나만 다르므로 바꾼다.
            if cnt == 1:
                # 하지만 이미 방문한 단어이면
                if V[nextIdx]:
                    # 다음 가는 위치보다 현재 길이가 짧은지 비교
                    if V[nextIdx] > V[currentIdx] + 1:
                        V[nextIdx] = V[currentIdx] + 1
                        q.append((words[nextIdx], nextIdx))
                else:
                    V[nextIdx] = V[currentIdx] + 1
                    q.append((words[nextIdx], nextIdx))

    if isFound:
        print(V)
        return result
    return 0