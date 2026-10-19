class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for char in columnTitle:
            # Convert character to its corresponding numerical value (A=1, B=2, ..., Z=26)
            value = ord(char) - ord('A') + 1
            # Accumulate the result by treating it as a base-26 number system
            result = result * 26 + value
        return result