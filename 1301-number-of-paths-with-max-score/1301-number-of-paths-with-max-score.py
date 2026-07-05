class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)
        dp_sum = [[-1] * n for _ in range(n)]
        dp_count = [[0] * n for _ in range(n)]
        
        dp_sum[n-1][n-1] = 0
        dp_count[n-1][n-1] = 1
        
        for r in range(n - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if (r == n - 1 and c == n - 1) or board[r][c] == 'X':
                    continue
                
                max_val = -1
                count = 0
                
                for dr, dc in [(1, 0), (0, 1), (1, 1)]:
                    nr, nc = r + dr, c + dc
                    
                    if nr < n and nc < n and dp_sum[nr][nc] != -1:
                        if dp_sum[nr][nc] > max_val:
                            max_val = dp_sum[nr][nc]
                            count = dp_count[nr][nc]
                        elif dp_sum[nr][nc] == max_val:
                            count = (count + dp_count[nr][nc]) % MOD
                
                if max_val != -1:
                 
                    if board[r][c] == 'E':
                        val = 0
                    else:
                        val = int(board[r][c])
                        
                    dp_sum[r][c] = max_val + val
                    dp_count[r][c] = count
        
        if dp_sum[0][0] == -1:
            return [0, 0]
        
        return [dp_sum[0][0], dp_count[0][0]]