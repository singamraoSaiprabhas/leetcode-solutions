class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        # Find the median element
        median = nums[len(nums) // 2]
        
        # Calculate the total moves to reach the median
        moves = 0
        for num in nums:
            moves += abs(num - median)
            
        return moves