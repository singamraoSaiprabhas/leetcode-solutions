class Solution:
    def minOperations(self, s: str) -> int:
        # 0 Operations: Already sorted
        if list(s) == sorted(s):
            return 0
            
        n = len(s)
        
        # Impossible case: Length 2 and not sorted
        if n == 2:
            return -1
            
        min_char = min(s)
        max_char = max(s)
        
        # 1 Operation: One of the ends is already correct
        if s[0] == min_char or s[-1] == max_char:
            return 1
            
        # 3 Operations: Worst case where unique max is at start AND unique min is at end
        if (s[0] == max_char and s.count(max_char) == 1 and 
            s[-1] == min_char and s.count(min_char) == 1):
            return 3
            
        # 2 Operations: Everything else can be sorted in 2 steps
        return 2