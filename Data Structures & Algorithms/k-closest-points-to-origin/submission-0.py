class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis = []
        
        for i in points:
            x,y = i
            d = (x*x + y*y)
            heapq.heappush(dis,[d*-1,x,y])
            if len(dis) > k:
                heapq.heappop(dis)
        
        res = []

        for p in dis:
            d,i,j = p
            res.append([i,j])
        
        return res