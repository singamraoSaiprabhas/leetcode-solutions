class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        counts = Counter(s)
        odd_count = 0
        mid_char = ""
        
        for char, count in counts.items():
            if count % 2 != 0:
                odd_count += 1
                mid_char = char
                
        # A palindrome can have at most one character with an odd frequency
        if odd_count > 1:
            return ""
            
        n = len(s)
        m = n // 2
        
        # The characters available to construct the first half of the palindrome
        half_counts = {char: count // 2 for char, count in counts.items()}
        
        last_div_i = -1
        last_div_c = ""
        
        curr_avail = dict(half_counts)
        matched_all = True
        
        # 2. Greedily attempt to match the first half of the target string
        for i in range(m):
            t_char = target[i]
            
            # Check if we can diverge at index 'i' by picking a strictly greater character
            for c_code in range(ord(t_char) + 1, ord('z') + 1):
                c = chr(c_code)
                if curr_avail.get(c, 0) > 0:
                    last_div_i = i
                    last_div_c = c
                    break  
            
            # Check if we can continue matching the exact prefix
            if curr_avail.get(t_char, 0) > 0:
                curr_avail[t_char] -= 1
            else:
                matched_all = False
                break
                
        # 3. Check if exact prefix match produces a valid strictly greater palindrome
        if matched_all:
            exact_half = target[:m]
            pal = exact_half + mid_char + exact_half[::-1]
            if pal > target:
                return pal
                
        # If no valid divergence point exists, no such palindromic permutation exists
        if last_div_i == -1:
            return ""
            
        # 4. Reconstruct the optimal first half based on the deepest divergence point
        rem_counts = dict(half_counts)
        for i in range(last_div_i):
            rem_counts[target[i]] -= 1
        rem_counts[last_div_c] -= 1
        
        rest_chars = []
        for c_code in range(ord('a'), ord('z') + 1):
            c = chr(c_code)
            if rem_counts.get(c, 0) > 0:
                rest_chars.append(c * rem_counts[c])
                
        ans_half = target[:last_div_i] + last_div_c + "".join(rest_chars)
        
        # Build and return the final palindrome
        return ans_half + mid_char + ans_half[::-1]