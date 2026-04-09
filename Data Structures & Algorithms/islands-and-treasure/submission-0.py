class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])

        INF = 2147483647
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i,j))
        
        while queue:
            r,c = queue.popleft()

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if nr < 0 or nc < 0 or nr >= m or nc >= n:
                    continue
                
                if grid[nr][nc] == -1:
                    continue
                
                if grid[nr][nc] == INF:
                    grid[nr][nc] = grid[r][c] + 1 
                    queue.append((nr, nc))
        
    