import bisect

class SparseTable:
    def __init__(self, arr):
        if not arr:
            self.st = []
            return
        n = len(arr)
        k = n.bit_length()
        self.st = [arr[:]]
        for i in range(1, k):
            row = []
            prev = self.st[i-1]
            offset = 1 << (i - 1)
            for j in range(n - (1 << i) + 1):
                row.append(max(prev[j], prev[j + offset]))
            self.st.append(row)

    def query(self, L, R):
        if L > R or not self.st:
            return 0
        j = (R - L + 1).bit_length() - 1
        return max(self.st[j][L], self.st[j][R - (1 << j) + 1])


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: list[list[int]]) -> list[int]:
        n = len(s)
        total_ones = s.count('1')
        
        # 1. Compress string into zero blocks: (start_idx, end_idx, length)
        zero_blocks = []
        i = 0
        while i < n:
            if s[i] == '0':
                j = i
                while j < n and s[j] == '0':
                    j += 1
                zero_blocks.append((i, j - 1, j - i))
                i = j
            else:
                i += 1
                
        # Edge case: No zeros to merge
        if not zero_blocks:
            return [total_ones] * len(queries)
            
        starts = [b[0] for b in zero_blocks]
        ends = [b[1] for b in zero_blocks]
        
        # 2. Precompute the sum of adjacent zero blocks (separated by a 1-block)
        adj_sum = []
        for i in range(len(zero_blocks) - 1):
            adj_sum.append(zero_blocks[i][2] + zero_blocks[i+1][2])
            
        # 3. Build Sparse Table for O(1) Range Maximum Queries
        st = SparseTable(adj_sum)
        ans = []
        
        # 4. Process each query
        for l, r in queries:
            # Find the first zero block that ends on or after `l`
            a = bisect.bisect_left(ends, l)
            # Find the last zero block that starts on or before `r`
            b = bisect.bisect_right(starts, r) - 1
            
            # If no valid zero blocks exist entirely or partially in this range, or only 1 exists
            if a >= len(zero_blocks) or b < 0 or a > b or a == b:
                ans.append(total_ones)
                continue
                
            # Calculate lengths of boundary zero blocks truncated by l and r
            L_a = min(r, zero_blocks[a][1]) - max(l, zero_blocks[a][0]) + 1
            L_b = min(r, zero_blocks[b][1]) - max(l, zero_blocks[b][0]) + 1
            
            if a + 1 == b:
                # Only 2 zero blocks in range, separated by one 1-block
                max_gain = L_a + L_b
            else:
                # 3 or more zero blocks in range. We check 3 possibilities:
                # Option 1: Truncated Left-most block + 2nd block
                gain1 = L_a + zero_blocks[a+1][2]
                
                # Option 2: 2nd to last block + Truncated Right-most block
                gain2 = zero_blocks[b-1][2] + L_b
                
                # Option 3: Maximum adjacent pairs completely inside the query range
                gain3 = st.query(a + 1, b - 2) if a + 1 <= b - 2 else 0
                
                max_gain = max(gain1, gain2, gain3)
                
            ans.append(total_ones + max_gain)
            
        return ans