class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = {}
        max_len = 0
        left = 0
        
        for right in range(len(nums)):
            freq[nums[right]] = freq.get(nums[right], 0) + 1
            
            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                left += 1
                
            max_len = max(max_len, right - left + 1)
            
        return max_len