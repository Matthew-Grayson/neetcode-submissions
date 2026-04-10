class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # sorted w/ O(log) hint at binary search
        # b-search by row comparing its min-max value to target
        # b-search that row; return True if target found, else False

        m, n = len(matrix), len(matrix[0])
        
        first, last =  0, m - 1
        while first <= last:
            row = (first + last) // 2
            if matrix[row][0] > target:
                last = row - 1
            elif matrix[row][n - 1] < target:
                first = row + 1
            else:
                break
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2

            if matrix[row][mid] > target:
                right = mid - 1
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                return True
        return False
