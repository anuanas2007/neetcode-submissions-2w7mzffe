class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0

        m = len(grid)
        n = len(grid[0])

        dirs = [[-1,0], [1,0], [0,-1], [0,1]]

        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i,j))
                else:
                    continue
        
        time = 0

        while fresh > 0 and queue:
            l = len(queue)

            for i in range(l):
                r, c = queue.popleft()

                for r1, c1 in dirs:
                    if 0 <= r + r1 < m and 0 <= c + c1 < n and grid[r+r1][c+c1] == 1:
                        fresh -= 1
                        grid[r+r1][c+c1] = 2
                        queue.append((r+r1, c+c1))
            
            time += 1
        

        if fresh == 0:
            return time
        else:
            return -1
