from functools import lru_cache

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Helper to extract prime factors
        def get_factors(n):
            counts = {2: 0, 3: 0, 5: 0, 7: 0}
            for p in [2, 3, 5, 7]:
                while n > 0 and n % p == 0:
                    counts[p] += 1
                    n //= p
            return counts, n
        
        req_counts, rem = get_factors(t)
        # If t has prime factors other than 2, 3, 5, 7, it's impossible.
        if rem > 1:
            return "-1"
        
        # DP to find the optimal digits to satisfy remaining factors of 2 and 3
        @lru_cache(None)
        def solve_23(r2, r3):
            if r2 <= 0 and r3 <= 0:
                return (0, "")
            
            best_len = float('inf')
            best_str = ""
            
            options = [(2, 1, 0), (3, 0, 1), (4, 2, 0), (6, 1, 1), (8, 3, 0), (9, 0, 2)]
            for d, p2, p3 in options:
                next_r2 = max(0, r2 - p2)
                next_r3 = max(0, r3 - p3)
                
                # FIX: Prevent infinite recursion if the state doesn't change
                if next_r2 == r2 and next_r3 == r3:
                    continue
                    
                cand_len, cand_str = solve_23(next_r2, next_r3)
                if cand_len != float('inf'):
                    cand_len += 1
                    cand_str = "".join(sorted(cand_str + str(d)))
                    
                    if cand_len < best_len:
                        best_len = cand_len
                        best_str = cand_str
                    elif cand_len == best_len:
                        if cand_str < best_str:
                            best_str = cand_str
                            
            return (best_len, best_str)

        def get_min_suffix(rem_2, rem_3, rem_5, rem_7, available_length):
            l_23, s_23 = solve_23(rem_2, rem_3)
            total_len = l_23 + rem_5 + rem_7
            
            if total_len > available_length:
                return None
            
            # FIX: Build the sorted suffix directly by counting characters 
            # to avoid sorting massive strings of up to 200,000 characters
            pad = available_length - total_len
            freq = {'2': 0, '3': 0, '4': 0, '5': rem_5, '6': 0, '7': rem_7, '8': 0, '9': 0}
            for char in s_23:
                freq[char] += 1
            
            suffix = "1" * pad
            for digit in "23456789":
                if freq[digit] > 0:
                    suffix += digit * freq[digit]
                    
            return suffix

        n = len(num)
        
        # Determine the first zero's position
        first_zero = num.find('0')
        if first_zero == -1:
            first_zero = n
            
            # Check if num itself is valid
            cur_2, cur_3, cur_5, cur_7 = 0, 0, 0, 0
            for char in num:
                f, _ = get_factors(int(char))
                cur_2 += f[2]; cur_3 += f[3]; cur_5 += f[5]; cur_7 += f[7]
                
            if cur_2 >= req_counts[2] and cur_3 >= req_counts[3] and \
               cur_5 >= req_counts[5] and cur_7 >= req_counts[7]:
                return num

        # Precompute prefix factors up to index i
        prefix_factors = []
        c2, c3, c5, c7 = 0, 0, 0, 0
        for i in range(n):
            prefix_factors.append((c2, c3, c5, c7))
            if num[i] != '0':
                f, _ = get_factors(int(num[i]))
                c2 += f[2]; c3 += f[3]; c5 += f[5]; c7 += f[7]

        # Try to modify from rightmost valid prefix to left
        max_valid_i = min(n - 1, first_zero)
        for i in range(max_valid_i, -1, -1):
            start_d = int(num[i]) + 1
            if num[i] == '0': 
                start_d = 1
                
            for d in range(start_d, 10):
                d_f, _ = get_factors(d)
                p2, p3, p5, p7 = prefix_factors[i]
                
                rem_2 = max(0, req_counts[2] - (p2 + d_f[2]))
                rem_3 = max(0, req_counts[3] - (p3 + d_f[3]))
                rem_5 = max(0, req_counts[5] - (p5 + d_f[5]))
                rem_7 = max(0, req_counts[7] - (p7 + d_f[7]))
                
                suffix_len = n - 1 - i
                suffix = get_min_suffix(rem_2, rem_3, rem_5, rem_7, suffix_len)
                
                if suffix is not None:
                    return num[:i] + str(d) + suffix

        # If no valid replacement of the same length works, we need a longer number.
        l_23, s_23 = solve_23(req_counts[2], req_counts[3])
        req_len = l_23 + req_counts[5] + req_counts[7]
        target_len = max(n + 1, req_len)
        
        return get_min_suffix(req_counts[2], req_counts[3], req_counts[5], req_counts[7], target_len)