class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        
        # Step 1: Precompute proper divisors for every possible length up to n
        divisors = [[] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, i):
                if i % j == 0:
                    divisors[i].append(j)
                    
        # Step 2: Precompute the cost to make any substring s[i...j] a semi-palindrome
        cost = [[0] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(i + 1, n):
                L = j - i + 1
                min_changes = float('inf')
                
                # Check all valid divisors for the current length L
                for d in divisors[L]:
                    current_changes = 0
                    
                    # A divisor d means there are d groups
                    for g in range(d):
                        left = i + g
                        right = i + g + L - d
                        
                        # Two pointers to count differences for the current group
                        while left < right:
                            if s[left] != s[right]:
                                current_changes += 1
                            left += d
                            right -= d
                            
                    if current_changes < min_changes:
                        min_changes = current_changes
                        
                cost[i][j] = min_changes
                
        # Step 3: DP to find minimum changes for k partitions
        # dp[p][i] = min changes to partition the first i characters into p substrings
        dp = [[float('inf')] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0
        
        for p in range(1, k + 1):
            # A valid partition p requires at least 2*p characters (min length 2 per substring)
            for i in range(p * 2, n + 1):
                # The previous partition must have ended at j
                # j must be at least 2*(p-1) to satisfy min length of previous partitions
                for j in range((p - 1) * 2, i - 1):
                    if dp[p - 1][j] != float('inf'):
                        dp[p][i] = min(dp[p][i], dp[p - 1][j] + cost[j][i - 1])
                        
        return dp[k][n]