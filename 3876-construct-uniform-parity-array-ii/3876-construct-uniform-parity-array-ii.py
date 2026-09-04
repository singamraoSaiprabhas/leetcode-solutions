class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_val = min(nums1)
        
        # If the minimum element is odd, we can make all elements odd.
        if min_val % 2 != 0:
            return True
            
        # If the minimum is even, ALL elements must be even to succeed.
        return all(x % 2 == 0 for x in nums1)