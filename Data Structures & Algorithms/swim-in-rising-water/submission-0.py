class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        minh = [[grid[0][0], 0, 0]] 
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        visit.add((0, 0))

        while minh:
            t, r, c = heapq.heappop(minh)
            if r == N -1 and c == N-1:
                return t
            
            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc
                if (neiR < 0 or neiC < 0 or
                    neiR == N or neiC == N or
                    (neiR, neiC) in visit):
                    continue
                
                visit.add((neiR, neiC))
                heapq.heappush(minh, [max(t, grid[neiR][neiC]), neiR, neiC])
