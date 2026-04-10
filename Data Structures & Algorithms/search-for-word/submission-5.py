class Solution:
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                board[r][c] != word[i]
            ):
                return False

            temp = board[r][c]
            board[r][c] = '#'   # mark visited

            for dr, dc in dirs:
                if dfs(r + dr, c + dc, i + 1):
                    board[r][c] = temp
                    return True

            board[r][c] = temp  # backtrack
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        return False