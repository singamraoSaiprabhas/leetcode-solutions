class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total_xor = 0
        for num in nums:
            total_xor ^= num
            
        if total_xor != 0:
            return len(nums)
        
        if any(num != 0 for num in nums):
            return len(nums) - 1
            
        return 0