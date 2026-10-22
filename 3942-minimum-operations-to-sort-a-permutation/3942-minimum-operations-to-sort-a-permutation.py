from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        # Find the index of 0 to anchor our cycle checks
        k = nums.index(0)

        # 1. Check if the array is an increasing cyclic shift
        is_inc = True
        for i in range(n):
            if nums[(k + i) % n] != i:
                is_inc = False
                break

        if is_inc:
            if k == 0:
                return 0
            # Path A: Rotate left k times (cost: k)
            # Path B: Reverse, rotate, reverse (cost: (n - k) % n + 2)
            return min(k, (n - k) % n + 2)

        # 2. Check if the array is a decreasing cyclic shift
        is_dec = True
        for i in range(n):
            # Move backwards through the array modulo n
            if nums[(k - i + n) % n] != i:
                is_dec = False
                break

        if is_dec:
            # Path A: Rotate to place n-1 at index 0, then reverse
            # Path B: Reverse first to make it an increasing cycle, then rotate
            return min((k + 1) % n + 1, n - k)

        # If it's neither, the adjacency is permanently broken and cannot be sorted
        return -1