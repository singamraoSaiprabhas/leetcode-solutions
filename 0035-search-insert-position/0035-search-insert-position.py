class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i 
        
        nums.sort()
        if target > max(nums):
            return len(nums)
        else:
            for i in range(len(nums)):
                if nums[i]>target:
                    return i