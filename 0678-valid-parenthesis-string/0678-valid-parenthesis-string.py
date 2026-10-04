class Solution:
    def checkValidString(self, s: str) -> bool:
        min_open = 0
        max_open = 0
        
        for char in s:
            if char == '(':
                min_open += 1
                max_open += 1
            elif char == ')':
                min_open -= 1
                max_open -= 1
            else: # char == '*'
                min_open -= 1  # Treat '*' as ')'
                max_open += 1  # Treat '*' as '('
            
            # If max_open is negative, there are too many ')' to ever be valid
            if max_open < 0:
                return False
            
            # min_open cannot be negative; if it drops below 0, it means 
            # we shouldn't have treated some '*' as ')'
            if min_open < 0:
                min_open = 0
                
        # String is valid if we can end with exactly zero open parentheses
        return min_open == 0