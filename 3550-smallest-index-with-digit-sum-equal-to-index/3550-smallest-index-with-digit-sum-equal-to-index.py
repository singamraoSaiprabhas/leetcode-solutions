class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            # Calculate the sum of the digits of the current number
            digit_sum = sum(int(digit) for digit in str(num))
            
            # Check if the digit sum equals the current index
            if digit_sum == i:
                return i
                
        # If no such index is found, return -1 as specified
        return -1