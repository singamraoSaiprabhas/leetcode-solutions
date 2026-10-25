class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        if not grid:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            # If out of bounds or water (1), stop exploring
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 1:
                return
            
            # Sink the land by marking it as water (visited)
            grid[r][c] = 1
            
            # Explore all 4 adjacent directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        # Step 1: Eliminate all land connected to the grid boundaries
        for r in range(rows):
            dfs(r, 0)          # Left boundary
            dfs(r, cols - 1)   # Right boundary
            
        for c in range(cols):
            dfs(0, c)          # Top boundary
            dfs(rows - 1, c)   # Bottom boundary
            
        # Step 2: Count the remaining closed islands
        closed_islands = 0
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if grid[r][c] == 0:
                    dfs(r, c) # Sink this entire closed island
                    closed_islands += 1
                    
        return closed_islands