class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        open_needed = 0  # Number of ')' needed
        
        for ch in s:
            if ch == '(':
                # If an odd number of ')' is pending, close the previous one
                if open_needed % 2 == 1:
                    insertions += 1  # Add a ')'
                    open_needed -= 1  # Completed that pair
                open_needed += 2
            else:  # ch == ')'
                open_needed -= 1
                if open_needed < 0:
                    insertions += 1  # Insert a '(' to pair with this ')'
                    open_needed += 2  # The '(' provides 2 slots; -1 + 2 = 1 needed
                    
        return insertions + open_needed