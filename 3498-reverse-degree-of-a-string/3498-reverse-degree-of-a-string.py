class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for index, char in enumerate(s, 1):
            # Calculate the reversed alphabet position (e.g., 'a' -> 26, 'z' -> 1)
            rev_pos = 26 - (ord(char) - ord('a'))
            
            # Multiply by the 1-indexed position in the string and add to total
            total += rev_pos * index
            
        return total