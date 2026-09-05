class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if not nums:
            return -1

        # Step 1: Precalculate the suffix minimums
        # min_right[i] will store the minimum value in nums[i..n-1]
        min_right = [0] * n
        min_right[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            min_right[i] = min(nums[i], min_right[i + 1])

        # Step 2: Iterate to find the first stable index
        running_max = float('-inf')
        for i in range(n):
            running_max = max(running_max, nums[i])
            
            # The instability score for index i
            instability_score = running_max - min_right[i]
            
            if instability_score <= k:
                return i
                
        return -1