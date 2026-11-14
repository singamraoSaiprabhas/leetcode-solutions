class Solution:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        min_pos_sum = float('inf')
        n = len(nums)
        
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                length = j - i + 1
                
                # Break early if the subarray exceeds the maximum allowed length
                if length > r:
                    break
                    
                # Update minimum positive sum if constraints are met
                if l <= length <= r and current_sum > 0:
                    min_pos_sum = min(min_pos_sum, current_sum)
                    
        return min_pos_sum if min_pos_sum != float('inf') else -1