class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        dirs = [[-1,0],[0,1],[1,0],[0,-1]]
        m = len(grid)
        n = len(grid[0])

        def helper(row,col):
            queue = deque()
            queue.append([row,col])

            while queue:
                r,c = queue.popleft()
                print(r,c)

                grid[r][c] = "0"
                for dir in dirs:
                    a,b = dir
                    if 0 <= r + a < m and  0 <= c +b < n:
                        if grid[r+a][c+b] == "1":
                            queue.append([r+a,c+b])

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    helper(i,j)
        
        return res































        # directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        # m = len(grid)
        # n = len(grid[0])

        # def dfs(r,c):
        #     if (r < 0 or c < 0 or r >= m or
        #         c >= n or grid[r][c] == "0"
        #     ):
        #         return
            
        #     grid[r][c] = "0"
            
        #     for dr, dc in directions:
        #         dfs(r+dr, c+dc)


        # res = 0
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == "1":
        #             dfs(i,j)
        #             res += 1
        
        # return res