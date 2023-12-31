import heapq
def solution(operations):
    maxHeap = []
    minHeap = []
    for operation in operations:
        oper, number = operation.split()
        number = int(number)
        if oper == "I":
            heapq.heappush(maxHeap, -number)
            heapq.heappush(minHeap, number)
        else:
            if number == 1:
                if maxHeap:
                    maxNumber = heapq.heappop(maxHeap)
                    minHeap.remove(-maxNumber)
            else:
                if minHeap:
                    minNumber = heapq.heappop(minHeap)
                    maxHeap.remove(-minNumber)

    answer = []
    if maxHeap:
        answer = [-maxHeap[0], minHeap[0]]
    else:
        answer = [0, 0]
    return answer