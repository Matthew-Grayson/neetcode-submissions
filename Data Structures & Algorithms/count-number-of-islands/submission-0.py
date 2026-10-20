class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rLen, cLen = len(grid), len(grid[0])
        count = 0

        def bfs(r, c):
            q = deque()
            grid[r][c] = "0"
            q.append((r, c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr < 0 or nr >= rLen or nc < 0 or nc >= cLen or grid [nr][nc] == "0"):
                        continue
                    
                    q.append((nr, nc))
                    grid[nr][nc] = "0"

        for r in range(rLen):
            for c in range(cLen):
                if grid[r][c] == "1":
                    bfs(r, c)
                    count += 1
        
        return count
