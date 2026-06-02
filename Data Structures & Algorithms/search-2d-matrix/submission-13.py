class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find row where target is between row's smallest and largest value
        # binary search that row

        rowLeft, rowRight = 0, len(matrix) - 1
        colLeft, colRight = 0, len(matrix[0]) - 1

        while rowLeft <= rowRight:
            row = (rowLeft + rowRight) // 2 
            if target < matrix[row][colLeft]:
                rowRight = row - 1
            elif target > matrix[row][colRight]:
                rowLeft = row + 1
            else:
                break
        
        while colLeft <= colRight:
            col = (colLeft + colRight) // 2
            if target < matrix[row][col]:
                colRight = col - 1
            elif target > matrix[row][col]:
                colLeft = col + 1
            else:
                return True

        return False
