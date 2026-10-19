class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        empty=[]
        a=0
        for i in nums:
            if target==i:
                empty.append(a)
            a+=1
        return empty