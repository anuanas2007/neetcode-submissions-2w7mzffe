class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        pac = [[False] * n for _ in range(m)]
        atl = [[False] * n for _ in range(m)]

        dirs = [[-1,0], [1,0], [0,-1], [0,1]]

        pacific = deque()
        atlantic = deque()

        for j in range(m):
            pacific.append((j, 0))
            atlantic.append((j, n -1))

        for i in range(n):
            pacific.append((0, i))
            atlantic.append((m-1, i))
        
        def bfs(queue, src):
            while queue:
                r,c = queue.popleft()
                src[r][c] = True

                for r1, c1 in dirs:
                    if 0 <= r+r1 < m and 0 <= c+c1 < n and not src[r+r1][c+c1]:
                        if heights[r+r1][c+c1] >= heights[r][c]:
                            queue.append((r+r1, c+c1))

        bfs(pacific, pac)
        bfs(atlantic, atl)

        res = []
        for q in range(m):
            for r in range(n):
                if pac[q][r] and atl[q][r]:
                    res.append([q,r])
        
        return res
        