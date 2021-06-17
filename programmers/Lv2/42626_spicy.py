#heap구조를 사용해야 했음!
import heapq
def solution(scoville, K):
    heap = []
    for sc in scoville:
        heapq.heappush(heap, sc)
    
    answer = 0
    while(heap[0] < K):
        heap_0 = heapq.heappop(heap)
        T = heap_0 + (heapq.heappop(heap) * 2)
        heapq.heappush(heap, T)
        if len(heap) == 1 and heap[0] < K:
            answer = -1
            break
        answer += 1
    return answer

if __name__ == '__main__':
    print(solution([1, 2], 3))