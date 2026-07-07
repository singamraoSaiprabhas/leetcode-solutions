class Solution:
    def sumAndMultiply(self, n: int) -> int:
        str_n = str(n)
        
        non_zero_chars = [char for char in str_n if char != '0']
        
        if not non_zero_chars:
            return 0
            
        x = int("".join(non_zero_chars))
        
        digit_sum = sum(int(char) for char in non_zero_chars)
        
        return x * digit_sum