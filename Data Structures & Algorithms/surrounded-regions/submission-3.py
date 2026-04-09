class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])

        dirs = [[-1,0], [1,0], [0,1], [0,-1]]

        def change(row,col, mark):
            q = deque()
            q.append((row,col))

            while q:
                r, c = q.popleft()
                board[r][c] = mark
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'O':
                        q.append((nr,nc))


        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    if i in [0, m-1] or j in [0, n-1]:
                        change(i,j,'T')
    
        # for i in range(m):
        #     for j in range(n):
        #         if board[i][j] == 'O':
        #             change(i,j,'X')
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    change(i,j,'X')
                elif board[i][j] == 'T':
                    board[i][j] = 'O'
