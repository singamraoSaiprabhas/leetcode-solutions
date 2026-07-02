class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = grid[0][0]
        q = deque([(grid[0][0], 0, 0)])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while q:
            d, r, c = q.popleft()
            if r == m - 1 and c == n - 1:
                if health - d >= 1:
                    return True
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    nd = d + grid[nr][nc]
                    if nd < dist[nr][nc]:
                        dist[nr][nc] = nd
                        if grid[nr][nc] == 0:
                            q.appendleft((nd, nr, nc))
                        else:
                            q.append((nd, nr, nc))
        return health - dist[m-1][n-1] >= 1