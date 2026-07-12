class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # a=dividend//divisor
        # if a >0:
        #     return a
        # else:
        #     a+=1
        #     return a
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        is_negative = (dividend < 0) != (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        quotient = 0
        while dividend >= divisor:
            temp_divisor = divisor
            multiple = 1
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            dividend -= temp_divisor
            quotient += multiple
            
        if is_negative:
            quotient = -quotient
            
        return quotient
        