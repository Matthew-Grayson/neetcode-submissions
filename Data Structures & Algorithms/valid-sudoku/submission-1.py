class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Initialize dictionaries to track values by row, column and square
        row = {"r{}".format(i): set() for i in range(9)}
        col = {"c{}".format(i): set() for i in range(9)}
        square = {
            "r{}c{}".format(i, j): set()
            for i in range(3)
            for j in range(3)
            }
        for i in range(len(board)):
            squareRow = i//3
            for j, y in enumerate(board[i]):
                squareCol = j//3
                if y != ".":
                    if (
                        y in row["r{}".format(i)] or
                        y in col["c{}".format(j)] or
                        y in square["r{}c{}".format(squareRow, squareCol)]
                        ):
                        return False
                    row["r{}".format(i)].add(y)
                    col["c{}".format(j)].add(y)
                    square["r{}c{}".format(squareRow, squareCol)].add(y)
        return True
                
