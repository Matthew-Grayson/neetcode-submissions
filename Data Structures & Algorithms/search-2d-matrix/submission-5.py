class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # good candidate for b-search O(m * n)
        # stair step method is simpler and more efficient O(m + n)

        rlast = len(matrix) - 1
        clast = len(matrix[0]) - 1
        
        row, col = 0, clast

        while row <= rlast and col >= 0:
            val = matrix[row][col]
            if val < target:
                row += 1
            elif val > target:
                col -= 1
            else:
                return True
            
        return False