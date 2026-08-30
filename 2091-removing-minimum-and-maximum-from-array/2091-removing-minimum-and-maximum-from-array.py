class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        
        # If the array has 2 or fewer elements, we must delete all of them
        if n <= 2:
            return n
            
        # Find the indices of the minimum and maximum elements
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))
        
        # Determine which index comes first and which comes second
        i = min(min_idx, max_idx)
        j = max(min_idx, max_idx)
        
        # Calculate deletions for all three strategies
        delete_front = j + 1
        delete_back = n - i
        delete_both_sides = (i + 1) + (n - j)
        
        # Return the minimum deletions required
        return min(delete_front, delete_back, delete_both_sides)