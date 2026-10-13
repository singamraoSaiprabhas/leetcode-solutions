class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squares = sorted([x * x for x in nums], reverse=True)
        
        # Calculate how many positive positions (even indices) there will be
        num_positive_positions = (len(nums) + 1) // 2
        
        # Sum the largest squares and subtract the smallest squares
        return sum(squares[:num_positive_positions]) - sum(squares[num_positive_positions:])