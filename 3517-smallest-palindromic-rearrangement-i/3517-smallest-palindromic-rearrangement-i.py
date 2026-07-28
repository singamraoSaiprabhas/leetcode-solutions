class Solution:
    def smallestPalindrome(self, s: str) -> str:
        counts = Counter(s)
        left_half = []
        middle = ""
        for char in sorted(counts.keys()):
            left_half.append(char * (counts[char] // 2))
            
            if counts[char] % 2 != 0:
                middle = char
                
        left_str = "".join(left_half)
        return left_str + middle + left_str[::-1]