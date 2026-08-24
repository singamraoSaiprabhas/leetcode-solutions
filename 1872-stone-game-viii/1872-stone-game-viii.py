class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        prefix_sums = list(accumulate(stones))
        
        # Base case: The last possible choice is picking all remaining stones (index n-1)
        # If a player is forced/chooses to take this, the next player gets 0.
        dp = prefix_sums[-1]
        
        # Iterate backwards from the second to last possible choice down to index 1
        # (index 0 is not valid because x > 1 stones must be removed)
        for i in range(len(stones) - 2, 0, -1):
            dp = max(dp, prefix_sums[i] - dp)
            
        return dp