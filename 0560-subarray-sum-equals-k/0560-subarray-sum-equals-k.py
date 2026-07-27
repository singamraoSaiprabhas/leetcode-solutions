class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d={0:1}
        presume=0
        count=0
        for nu in nums:
            presume+=nu
            if presume-k in d:
                count+=d[presume-k]
            if presume in d:
                d[presume]+=1
            else:
                d[presume]=1
        return count
