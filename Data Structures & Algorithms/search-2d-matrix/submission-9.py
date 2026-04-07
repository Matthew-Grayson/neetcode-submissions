class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, top = 0, 0
        right, bot = len(matrix[0]) - 1, len(matrix) - 1

        while top <= bot:
            row = (top + bot) // 2
            if target < matrix[row][0]:
                bot = row - 1
            elif target > matrix[row][len(matrix[0]) - 1]:
                top = row + 1
            else:
                break
        if top > bot:
            return False
        while left <= right:
            col = (left + right) // 2
            if target < matrix[row][col]:
                right = col - 1
            elif target > matrix [row][col]:
                left = col + 1
            else:
                return True
        return False
