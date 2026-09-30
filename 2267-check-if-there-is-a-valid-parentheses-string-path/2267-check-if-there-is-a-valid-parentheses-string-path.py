class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # 1. Quick parity and boundary checks
        if (m + n - 1) % 2 != 0:
            return False
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        # memo stores visited states: (row, col, balance)
        visited = set()

        def dfs(r: int, c: int, bal: int) -> bool:
            # Update balance for current cell
            bal += 1 if grid[r][c] == '(' else -1
            
            # Invalid if balance dips below 0
            if bal < 0:
                return False
            
            # Prune if there aren't enough remaining steps to close all open brackets
            remaining_steps = (m - 1 - r) + (n - 1 - c)
            if bal > remaining_steps:
                return False
            
            # Reached destination
            if r == m - 1 and c == n - 1:
                return bal == 0
            
            state = (r, c, bal)
            if state in visited:
                return False
            visited.add(state)
            
            # Explore down and right
            if r + 1 < m and dfs(r + 1, c, bal):
                return True
            if c + 1 < n and dfs(r, c + 1, bal):
                return True
            
            return False

        return dfs(0, 0, 0)