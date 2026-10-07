class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search to find row
        # binary search to find target

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom:
            row = top + (bottom - top) // 2
            if target < matrix[row][left]:
                bottom = row - 1

            elif target > matrix[row][right]:
                top = row + 1

            else:
                break

        if top > bottom:
            return False

        while left <= right:
            col = left + (right - left) // 2
            if target < matrix[row][col]:
                right = col - 1

            elif target > matrix[row][col]:
                left = col + 1

            else:
                return True

        return False
       

