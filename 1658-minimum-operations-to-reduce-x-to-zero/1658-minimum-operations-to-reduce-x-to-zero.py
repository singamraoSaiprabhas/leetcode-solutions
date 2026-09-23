class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        n = len(nums)
        
        # If the total sum is exactly x, we must remove all elements
        if target == 0:
            return n
        # If the target is negative, it's impossible since all elements are positive
        if target < 0:
            return -1
            
        left = 0
        current_sum = 0
        max_len = -1
        
        for right in range(n):
            current_sum += nums[right]
            
            # Shrink the window if the sum exceeds the target
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1
                
            # If we found a valid subarray, update the maximum length
            if current_sum == target:
                max_len = max(max_len, right - left + 1)
                
        # If max_len is still -1, no such subarray was found
        return n - max_len if max_len != -1 else -1