class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_count = 0
        mismatches = 0
        
        for char in s:
            if char == '(':
                open_count += 1
            else:  # char == ')'
                if open_count > 0:
                    open_count -= 1
                else:
                    mismatches += 1
                    
        return mismatches + open_count