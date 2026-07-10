class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        unique=set(nums)
        for i in unique:
            a=nums.count(i)
            if  a>len(nums)/2:
                return i