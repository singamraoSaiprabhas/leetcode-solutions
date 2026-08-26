class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        count_ones = 0
        min_len = float('inf')
        best_str = ""
        
        for right in range(len(s)):
            if s[right] == '1':
                count_ones += 1
                
            # Once we hit exactly k ones, we evaluate and try to shrink the window
            while count_ones == k:
                current_len = right - left + 1
                current_str = s[left:right + 1]
                
                # Update if we find a strictly shorter one
                if current_len < min_len:
                    min_len = current_len
                    best_str = current_str
                # Update if lengths match but it is lexicographically smaller
                elif current_len == min_len:
                    if current_str < best_str:
                        best_str = current_str
                        
                # Shrink from the left
                if s[left] == '1':
                    count_ones -= 1
                left += 1
                
        return best_str