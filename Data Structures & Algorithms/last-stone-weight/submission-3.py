class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for s in stones:
            heapq.heappush(heap, s*(-1))

        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            
            if x != y:
                heapq.heappush(heap, x-y)
        
        return heap[0] * -1 if heap else 0

        