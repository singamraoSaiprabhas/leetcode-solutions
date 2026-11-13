from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        # Prefix sums for O(1) sum queries of original array elements
        pref_sum = [0] * (n + 1)
        for i in range(n):
            pref_sum[i + 1] = pref_sum[i] + nums[i]
            
        ans = 0
        # Stack elements will be tuples: (start_index, max_value, cumulative_cost_from_bottom)
        st = []
        
        # Traverse right to left
        for i in range(n - 1, -1, -1):
            # Maintain monotonic stack (strictly decreasing values)
            while st and st[-1][1] <= nums[i]:
                st.pop()
                
            # Determine the boundary of the new block dominated by nums[i]
            next_idx = st[-1][0] if st else n
            
            # Cost to flatten this specific block to nums[i]
            block_cost = (next_idx - i) * nums[i] - (pref_sum[next_idx] - pref_sum[i])
            
            # Cumulative cost builds from the bottom of the stack up to the current block
            new_cum = (st[-1][2] if st else 0) + block_cost
            st.append((i, nums[i], new_cum))
            
            # 1. Binary search the stack to find the block where the budget k is exceeded
            low, high = 0, len(st) - 1
            exceed_j = -1
            
            while low <= high:
                mid = (low + high) // 2
                # Cost to include all blocks from the top of the stack down to 'mid' inclusive
                cost_to_mid = st[-1][2] - (st[mid - 1][2] if mid > 0 else 0)
                
                if cost_to_mid > k:
                    exceed_j = mid
                    low = mid + 1
                else:
                    high = mid - 1
                    
            if exceed_j == -1:
                # If budget is never exceeded, we can extend the subarray to the very end
                best_R = n - 1
            else:
                # 2. Budget is exceeded in block 'j'. Calculate remaining budget for this block
                j = exceed_j
                rem_k = k - (st[-1][2] - st[j][2] if j < len(st) - 1 else 0)
                
                B_start = st[j][0]
                B_end = st[j-1][0] - 1 if j > 0 else n - 1
                
                # Binary search for the exact right boundary 'R' within this specific block
                l, r = B_start, B_end
                best_R = B_start - 1
                
                while l <= r:
                    m = (l + r) // 2
                    partial_cost = (m - B_start + 1) * st[j][1] - (pref_sum[m + 1] - pref_sum[B_start])
                    
                    if partial_cost <= rem_k:
                        best_R = m
                        l = m + 1
                    else:
                        r = m - 1
                        
            # Number of valid subarrays starting at 'i' is the length of the window
            ans += best_R - i + 1
            
        return ans