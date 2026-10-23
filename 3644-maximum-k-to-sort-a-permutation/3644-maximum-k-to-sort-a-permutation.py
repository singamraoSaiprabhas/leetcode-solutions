from typing import List

class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        ans = -1
        
        for i, val in enumerate(nums):
            # If the element is not at its sorted position
            if val != i:
                if ans == -1:
                    ans = val
                else:
                    ans &= val
                
                # Optimization: The bitwise AND can never increase. 
                # If it hits 0, it will stay 0, so we can exit early.
                if ans == 0:
                    break
                    
        # If ans is still -1, the array was already sorted.
        return ans if ans != -1 else 0