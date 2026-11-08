class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        if not grid:
            return 0
            
        m, n = len(grid), len(grid[0])
        
        # Arrays to store the count of servers in each row and column
        row_counts = [0] * m
        col_counts = [0] * n
        
        # Step 1: Count the servers in each row and each column
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_counts[i] += 1
                    col_counts[j] += 1
                    
        # Step 2: Count servers that can communicate with at least one other server
        communicating_servers = 0
        for i in range(m):
            for j in range(n):
                # A server can communicate if its row or column has more than 1 server
                if grid[i][j] == 1 and (row_counts[i] > 1 or col_counts[j] > 1):
                    communicating_servers += 1
                    
        return communicating_servers