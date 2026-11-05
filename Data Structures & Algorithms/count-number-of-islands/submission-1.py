class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        rowLen, colLen = len(grid), len(grid[0])
        count = 0

        def bfs(row, col):
            q = deque()
            q.append((row, col))
            grid[row][col] = "0"

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col

                    if (nr < 0 or nr >= rowLen or nc < 0 or nc >= colLen or grid[nr][nc] == "0"):
                        continue

                    q.append((nr, nc))
                    grid[nr][nc] = "0"

        for row in range(rowLen):
            for col in range(colLen):
                if grid[row][col] == "1":
                    bfs(row, col)
                    count += 1

        return count