class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums_set = set(nums)
        
        # Start with the first positive multiple of k
        multiple = k
        
        # Keep incrementing by k until we find a multiple not in the set
        while multiple in nums_set:
            multiple += k
            
        return multiple
        