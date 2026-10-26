from collections import deque
from typing import List

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        if not grid or not grid[0]:
            return 0
            
        m = len(grid)
        n = len(grid[0])
        valid_islands = 0
        
        # Directions for 4-way connectivity (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for i in range(m):
            for j in range(n):
                # If we find a positive integer, it's a new unvisited island component
                if grid[i][j] > 0:
                    island_sum = 0
                    queue = deque([(i, j)])
                    
                    # Accumulate value and mark as visited by setting to 0
                    island_sum += grid[i][j]
                    grid[i][j] = 0 
                    
                    # BFS to traverse the entire island
                    while queue:
                        r, c = queue.popleft()
                        
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            
                            # Check boundaries and if it's part of the island (> 0)
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                                island_sum += grid[nr][nc]
                                grid[nr][nc] = 0  # Mark visited immediately to prevent duplicate queueing
                                queue.append((nr, nc))
                    
                    # Check if the total island sum is divisible by k
                    if island_sum % k == 0:
                        valid_islands += 1
                        
        return valid_islands