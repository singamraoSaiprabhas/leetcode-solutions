class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # dp[j] stores the set of all possible XOR sums to reach the current cell in column j
        dp = [set() for _ in range(n)]
        dp[0].add(grid[0][0])
        
        # Initialize the first row 
        for j in range(1, n):
            dp[j] = {x ^ grid[0][j] for x in dp[j-1]}
            
        # Process the remaining rows
        for i in range(1, m):
            # Update the first column for the new row
            dp[0] = {x ^ grid[i][0] for x in dp[0]}
            
            for j in range(1, n):
                # The reachable XOR states for the current cell come from either 
                # the cell directly above (dp[j]) or the cell to the left (dp[j-1]).
                dp[j] = {x ^ grid[i][j] for x in dp[j] | dp[j-1]}
                
        # Return the minimum XOR value reachable at the bottom-right cell
        return min(dp[-1])