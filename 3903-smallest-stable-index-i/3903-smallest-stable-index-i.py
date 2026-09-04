class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        # Step 1 & 2: Precompute suffix minimums
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], nums[i])
            
        curr_max = float('-inf')
        
        # Step 3 & 4: Calculate running maximum and find the first stable index
        for i in range(n):
            curr_max = max(curr_max, nums[i])
            
            if curr_max - suffix_min[i] <= k:
                return i
                
        # Step 5: If no such index exists
        return -1