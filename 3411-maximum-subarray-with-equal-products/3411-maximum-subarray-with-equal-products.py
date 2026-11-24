from math import gcd
from typing import List

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1 if nums[0] == 1 else 0

        ans = 2  # Any subarray of length 2 is always valid
        left = 0
        window_prod = 1

        for right, x in enumerate(nums):
            while gcd(window_prod, x) > 1:
                window_prod //= nums[left]
                left += 1
            window_prod *= x
            ans = max(ans, right - left + 1)

        return ans