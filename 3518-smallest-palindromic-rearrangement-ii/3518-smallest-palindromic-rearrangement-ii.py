class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        counts = Counter(s)
        half_counts = {}
        mid_char = ""
        
        for char, count in counts.items():
            if count % 2 != 0:
                mid_char = char
            if count // 2 > 0:
                half_counts[char] = count // 2
                
        N = sum(half_counts.values())
        
        P = math.factorial(N)
        for count in half_counts.values():
            P //= math.factorial(count)
            
        if k > P:
            return ""
            
        ans_half = []
        sorted_chars = sorted(half_counts.keys())
        
        for _ in range(N):
            for c in sorted_chars:
                if half_counts[c] == 0:
                    continue
                
                P_next = P * half_counts[c] // N
                
                if k <= P_next:
                    ans_half.append(c)
                    half_counts[c] -= 1
                    P = P_next
                    N -= 1
                    break
                else:
                    k -= P_next
        first_half = "".join(ans_half)
        return first_half + mid_char + first_half[::-1]