class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        # Precompute suffix sums to quickly find the total remaining stones
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
            
        memo = {}
        
        def dp(i, m):
            # Base case: no more piles left
            if i >= n:
                return 0
                
            # Base case: if we can take all remaining piles, take them all
            if i + 2 * m >= n:
                return suffix_sum[i]
                
            if (i, m) in memo:
                return memo[(i, m)]
            
            max_stones = 0
            
            # The current player can take x piles, where 1 <= x <= 2m
            for x in range(1, 2 * m + 1):
                # The maximum stones the current player can get is the total 
                # remaining stones minus the max stones the OTHER player can get
                opponent_stones = dp(i + x, max(m, x))
                max_stones = max(max_stones, suffix_sum[i] - opponent_stones)
                
            memo[(i, m)] = max_stones
            return max_stones
        
        # Start the game from index 0 with M = 1
        return dp(0, 1)