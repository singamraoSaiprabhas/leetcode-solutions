class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)
        
        pref_sum = [0] * (n + 1)
        nz_count = [0] * (n + 1)
        s_prime = []
        
        for i in range(n):
            digit = int(s[i])
            pref_sum[i+1] = pref_sum[i] + digit
            nz_count[i+1] = nz_count[i] + (1 if digit != 0 else 0)
            if digit != 0:
                s_prime.append(digit)
                
        k = len(s_prime)
        pref_val = [0] * (k + 1)
        pow10 = [1] * (k + 1)
        
        for i in range(k):
            pref_val[i+1] = (pref_val[i] * 10 + s_prime[i]) % MOD
            pow10[i+1] = (pow10[i] * 10) % MOD
            
        ans = []
        for l, r in queries:
            digit_sum = pref_sum[r+1] - pref_sum[l]
            
            # 2. Find boundaries of the non-zero digits in our s_prime array
            c1 = nz_count[l]
            c2 = nz_count[r+1]
            length = c2 - c1
            
            # 3. Calculate the concatenated number x modulo (10^9 + 7)
            if length == 0:
                x = 0
            else:
                x = (pref_val[c2] - pref_val[c1] * pow10[length]) % MOD
                x = (x + MOD) % MOD # Ensures non-negative result
                
            # 4. Multiply and append to answer
            ans.append((x * digit_sum) % MOD)
            
        return ans