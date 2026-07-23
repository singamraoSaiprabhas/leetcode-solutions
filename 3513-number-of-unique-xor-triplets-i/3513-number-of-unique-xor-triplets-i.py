class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n=len(nums)
        if n<=2:
            return n
        else:
            return 1 << n.bit_length()