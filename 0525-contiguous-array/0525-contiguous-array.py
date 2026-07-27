class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ans=0
        pre=0
        pretoin={0:-1}
        for i,num in enumerate(nums):
            pre+=1 if num else -1
            ans=max(ans,i-pretoin.setdefault(pre,i))
        return ans
