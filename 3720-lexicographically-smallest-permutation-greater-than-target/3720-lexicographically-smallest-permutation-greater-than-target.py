class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        avail_counts = Counter(s)
        
        last_div_i = -1
        last_div_c = ''
        
        # 1. Find the optimal divergence point
        for i, t_char in enumerate(target):
            # Check if we can diverge at index 'i'
            # We need an available character strictly greater than target[i]
            # We check in ascending order to find the smallest valid candidate
            for c_code in range(ord(t_char) + 1, ord('z') + 1):
                c = chr(c_code)
                if avail_counts[c] > 0:
                    last_div_i = i
                    last_div_c = c
                    break # Smallest strictly greater character found
                    
            # Check if we can continue matching the prefix for the next iteration
            if avail_counts[t_char] > 0:
                avail_counts[t_char] -= 1
            else:
                # We don't have the character to match target[i], so we must stop exploring deeper
                break
                
        # If no valid divergence point was found, no such permutation exists
        if last_div_i == -1:
            return ""
            
        # 2. Reconstruct the optimal string
        # Re-calculate remaining characters based on our chosen divergence point
        rem_counts = Counter(s)
        for i in range(last_div_i):
            rem_counts[target[i]] -= 1
        rem_counts[last_div_c] -= 1
        
        # The remaining characters must be appended in ascending order 
        # to ensure the result is lexicographically smallest
        rest_chars = []
        for c_code in range(ord('a'), ord('z') + 1):
            c = chr(c_code)
            if rem_counts[c] > 0:
                rest_chars.append(c * rem_counts[c])
                
        return target[:last_div_i] + last_div_c + "".join(rest_chars)