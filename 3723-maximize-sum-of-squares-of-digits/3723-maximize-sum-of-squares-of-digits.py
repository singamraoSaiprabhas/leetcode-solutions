class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""
        
        # Calculate the number of 9s, the remaining digit, and the number of 0s.
        nines = sum // 9
        remainder = sum % 9
        zeros = num - nines - (1 if remainder > 0 else 0)
        
        # Construct the maximum possible integer string
        res = "9" * nines
        if remainder > 0:
            res += str(remainder)
        res += "0" * zeros
        
        return res