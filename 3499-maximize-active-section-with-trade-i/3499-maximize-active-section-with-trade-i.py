class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        t = "1" + s + "1"
        initial_ones = s.count('1')
        
        # Group adjacent identical characters into (char, length)
        blocks = []
        i = 0
        n = len(t)
        while i < n:
            j = i
            while j < n and t[j] == t[i]:
                j += 1
            blocks.append((t[i], j - i))
            i = j
            
        # Find all valid '0' blocks in the original augmented string
        valid_0_lengths = []
        for k in range(len(blocks)):
            if blocks[k][0] == '0':
                if k > 0 and blocks[k-1][0] == '1' and k < len(blocks) - 1 and blocks[k+1][0] == '1':
                    valid_0_lengths.append(blocks[k][1])
                    
        max_original_0 = max(valid_0_lengths) if valid_0_lengths else 0
        max_gain = 0
        has_valid_1 = False
        for k in range(len(blocks)):
            if blocks[k][0] == '1':
                if k > 0 and blocks[k-1][0] == '0' and k < len(blocks) - 1 and blocks[k+1][0] == '0':
                    has_valid_1 = True
                    l_1 = blocks[k][1]
                    left_0_len = blocks[k-1][1]
                    right_0_len = blocks[k+1][1]
                    gain_merge = left_0_len + right_0_len
                    gain_separate = max_original_0 - l_1
                    
                    max_gain = max(max_gain, gain_merge, gain_separate)
                    
        if not has_valid_1:
            return initial_ones
            
        return initial_ones + max(0, max_gain)