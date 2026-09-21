class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        res = [0] * k
        dp = [0] * k  # dp[r] is the number of subarrays ending at current index with product % k == r
        
        for val in nums:
            v = val % k
            new_dp = [0] * k
            
            # Subarray consisting solely of nums[i]
            new_dp[v] += 1
            
            # Extending subarrays ending at the previous index
            for r in range(k):
                if dp[r] > 0:
                    new_dp[(r * v) % k] += dp[r]
            
            # Accumulate current valid subarrays into total result
            for r in range(k):
                res[r] += new_dp[r]
                
            dp = new_dp
            
        return res