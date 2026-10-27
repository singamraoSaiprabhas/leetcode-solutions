class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            # If the digit is 9, it becomes 0 and the loop continues to carry the 1
            digits[i] = 0
            
        # If we exit the loop, it means all digits were 9 (e.g., [9, 9] -> [0, 0])
        # We need to prepend a 1 to the list
        return [1] + digits