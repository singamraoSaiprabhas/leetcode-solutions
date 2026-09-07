class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        
        # Array to store the number of distinct subsequences ending with each letter
        ends_with = [0] * 26 
        total_subsequences = 0
        
        for char in s:
            # Map character 'a'-'z' to index 0-25
            idx = ord(char) - ord('a')
            
            # The new subsequences ending with `char` can be formed by appending `char` 
            # to all previously existing subsequences, plus the `char` itself as a standalone subsequence.
            new_count_for_char = (total_subsequences + 1) % MOD
            
            # The change in our total subsequences is the difference between the 
            # new count for this character and its old count.
            delta = (new_count_for_char - ends_with[idx]) % MOD
            
            # Update the count of subsequences ending with this character
            ends_with[idx] = new_count_for_char
            
            # Update the total count of subsequences
            total_subsequences = (total_subsequences + delta) % MOD
            
        return total_subsequences
        