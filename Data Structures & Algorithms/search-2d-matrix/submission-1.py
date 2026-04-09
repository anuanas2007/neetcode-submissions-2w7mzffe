class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        l, r = 0, m*n - 1

        while l <= r:
            ind = (l+r) // 2
            ro = ind // n 
            c = ind % n

            if matrix[ro][c] == target:
                return True
            
            elif matrix[ro][c] > target:
                r = ind - 1
            
            else:
                l = ind + 1
            
        return False



