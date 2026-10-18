from math import comb

class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7

        def count(arr: list[int]) -> int:
            # A tree of size <= 2 has only 1 valid relative order
            if len(arr) <= 2:
                return 1

            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]

            # Ways to choose positions for the left subtree elements
            interleavings = comb(len(left) + len(right), len(left))

            return (interleavings * count(left) * count(right)) % MOD

        return (count(nums) - 1) % MOD