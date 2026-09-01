class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        start_r = start_c = -1
        litter_positions = []
        
        # 1. Locate the starting position and all litter items
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start_r, start_c = r, c
                elif classroom[r][c] == 'L':
                    litter_positions.append((r, c))
                    
        K = len(litter_positions)
        if K == 0:
            return 0  # No litter to clean
            
        # Map each litter's coordinate to a unique bit index (0 to K-1)
        litter_map = {pos: i for i, pos in enumerate(litter_positions)}
        
        # Queue stores: (row, col, current_energy, collected_litter_bitmask, moves)
        queue = deque([(start_r, start_c, energy, 0, 0)])
        
        # Visited dictionary tracks the maximum energy we've had at a specific (row, col) 
        # with a specific collection mask to avoid suboptimal redundant paths.
        visited = {}
        visited[(start_r, start_c, 0)] = energy
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # 2. Execute BFS
        while queue:
            r, c, e, mask, moves = queue.popleft()
            
            # If energy is 0, we cannot move from this cell
            if e == 0:
                continue
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check bounds and obstacles
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    ne = e - 1
                    nmask = mask
                    
                    # Handle reset areas and litter collection
                    if classroom[nr][nc] == 'R':
                        ne = energy
                    elif (nr, nc) in litter_map:
                        nmask |= (1 << litter_map[(nr, nc)])
                        
                    # Target reached: All K bits are set to 1
                    if nmask == (1 << K) - 1:
                        return moves + 1
                        
                    # If we reach this state with strictly greater energy than before, add to queue
                    if visited.get((nr, nc, nmask), -1) < ne:
                        visited[(nr, nc, nmask)] = ne
                        queue.append((nr, nc, ne, nmask, moves + 1))
                        
        return -1