class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        max_len = 0
        left = 0
        char_counts = {}

        for right in range(len(s)):
            char = s[right]
            char_counts[char] = char_counts.get(char, 0) + 1
            
            while char_counts[char] > 2:
                char_counts[s[left]] -= 1
                left += 1
                
            max_len = max(max_len, right - left + 1)
        return max_len