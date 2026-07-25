class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        # if len(nums)==1:
        #     return 0
        # elif len(nums)==2:
        #     new=[]
        #     for i in nums:
        #         new.append(nums[0]+k)
        #         new.append(nums[-1]-k)
        #     return (max(new)-min(new))
        # else:
        #     lastmin=(max(nums)-min(nums))
        #     neg=-k
        #     pos=0
        #     while pos>=k:
        #         if (nums[max(nums)]-neg)-(nums[min(nums)]+pos)<lastmin:
        #             lastmin=(nums[max(nums)]-neg)-(nums[min(nums)]+pos)
        #         else:
        #             neg+=1
        #             pos+=1
        #     return lastmin
        max_val = max(nums)
        min_val = min(nums)
        new_max = max_val - k
        new_min = min_val + k
        return max(0, new_max - new_min)
                
