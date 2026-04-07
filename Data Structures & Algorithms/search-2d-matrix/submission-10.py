class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search
        # start in middle row
        # if target is in bounds of row; binary search that row
        # else move search bounds
        m, n = len(matrix) - 1, len(matrix[0]) - 1
        top, bottom =  0, m
        left, right = 0, n
        while top <= bottom:
            row = (top + bottom) // 2
            if target < matrix[row][0]:
                bottom = row - 1
            elif target > matrix[row][n]:
                top = row + 1
            else:
                break
        while left <= right:
            mid = (left + right) // 2
            if target < matrix[row][mid]:
                right = mid - 1
            elif target > matrix[row][mid]:
                left = mid + 1
            else:
                return True
        return False