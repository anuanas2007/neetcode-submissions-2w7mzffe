class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [[-1,0],[0,1],[1,0],[0,-1]]
        m = len(grid)
        n = len(grid[0])

        def helper(row,col):
            queue = deque()
            queue.append([row,col])
            grid[row][col] = 0
            area = 0
            while queue:
                r,c = queue.popleft()
                area += 1

                for dir in dirs:
                    a,b = dir
                    if 0 <= r + a < m and  0 <= c +b < n:
                        if grid[r+a][c+b] == 1:
                            queue.append([r+a,c+b])
                            grid[r+a][c+b] = 0
                
            return area

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    temp = helper(i,j)
                    res = max(res, temp)
        return res
        























        # m = len(grid)
        # n = len(grid[0])

        # directions = [[-1,0], [1,0], [0,-1], [0,1]]

        # def bfs(r,c):
        #     res = 1
        #     queue = deque()
        #     queue.append((r,c))
        #     grid[r][c] = 0

        #     while queue:
        #         row,col = queue.popleft()
        #         if grid[row][col] == 1:
        #             res+= 1
        #             grid[row][col] = 0
        #         for dr, dc in directions:
        #             nr, nc = dr + row, dc + col
        #             if (nr < 0 or nc < 0 or nr >= m or
        #                 nc >= n or grid[nr][nc] == 0
        #             ):
        #                 continue
                    
        #             queue.append((nr,nc))

        #     return res     

        # fres = 0

        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == 1:
        #             k = bfs(i,j)
        #             fres = max(fres, k)
            
        # return fres
        