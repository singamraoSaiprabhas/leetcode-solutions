class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        # dp[j] stores the number of distinct subsequences of s forming t[:j]
        dp = [0] * (n + 1)
        dp[0] = 1  # An empty string t can always be formed 1 way
        
        for i in range(1, m + 1):
            # Iterate backwards to use previous row's values (equivalent to 2D DP)
            for j in range(n, 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]
                    
        return dp[n]