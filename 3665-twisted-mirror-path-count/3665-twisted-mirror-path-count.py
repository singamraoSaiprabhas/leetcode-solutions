from typing import List

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        MOD = 10**9 + 7
        
        # Base case for 1x1 grid
        if m == 1 and n == 1:
            return 1

        # We store the landing cell as an integer (r * n + c) to save space/overhead.
        # -1 represents moving out of bounds (an invalid path).
        jump_right = [[-1] * n for _ in range(m)]
        jump_down = [[-1] * n for _ in range(m)]
        
        # 1. Precompute where a ray lands if it enters grid[r][c] moving Right or Down
        # We iterate bottom-up, right-to-left to build dependencies.
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                idx = r * n + c
                
                # If it's the destination or an empty cell, the robot stops here.
                if (r == m - 1 and c == n - 1) or grid[r][c] == 0:
                    jump_right[r][c] = idx
                    jump_down[r][c] = idx
                else:
                    # It's a mirror (grid[r][c] == 1)
                    # Entered moving RIGHT -> turns DOWN -> targets cell below moving DOWN
                    if r + 1 < m:
                        jump_right[r][c] = jump_down[r + 1][c]
                        
                    # Entered moving DOWN -> turns RIGHT -> targets cell right moving RIGHT
                    if c + 1 < n:
                        jump_down[r][c] = jump_right[r][c + 1]

        # 2. DP to count the valid paths
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        
        for r in range(m):
            for c in range(n):
                if dp[r][c] == 0:
                    continue
                
                # Stop initiating moves if we're already at the destination
                if r == m - 1 and c == n - 1:
                    continue
                
                # Attempt to move Right
                if c + 1 < n:
                    land = jump_right[r][c + 1]
                    if land != -1:  # If it doesn't reflect out of bounds
                        nr, nc = land // n, land % n
                        dp[nr][nc] = (dp[nr][nc] + dp[r][c]) % MOD
                        
                # Attempt to move Down
                if r + 1 < m:
                    land = jump_down[r + 1][c]
                    if land != -1:  # If it doesn't reflect out of bounds
                        nr, nc = land // n, land % n
                        dp[nr][nc] = (dp[nr][nc] + dp[r][c]) % MOD
                        
        return dp[m - 1][n - 1]