class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        i = 0
        
        while i <= n - k:
            # 1. Greedily check for a length k palindrome
            sub_k = s[i : i + k]
            if sub_k == sub_k[::-1]:
                ans += 1
                i += k  # Jump past this palindrome
                continue
            
            # 2. If length k fails, check for a length k + 1 palindrome
            if i + k < n:
                sub_k_plus_1 = s[i : i + k + 1]
                if sub_k_plus_1 == sub_k_plus_1[::-1]:
                    ans += 1
                    i += k + 1  # Jump past this palindrome
                    continue
            
            # 3. If neither works, move 1 step forward
            i += 1
            
        return ans