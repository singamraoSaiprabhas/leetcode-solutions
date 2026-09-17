class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        # min_len[i] stores the minimum length of a valid subarray ending at or before index i
        min_len = [float('inf')] * n
        
        curr_sum = 0
        left = 0
        ans = float('inf')
        
        for right in range(n):
            curr_sum += arr[right]
            
            # Shrink window from the left while the sum exceeds target
            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1
            
            # Carry forward the best length found so far
            if right > 0:
                min_len[right] = min_len[right - 1]
            
            # Valid subarray found in range [left, right]
            if curr_sum == target:
                length = right - left + 1
                
                # Check if there exists a valid non-overlapping subarray to the left
                if left > 0 and min_len[left - 1] != float('inf'):
                    ans = min(ans, length + min_len[left - 1])
                
                # Update min_len for the current index
                min_len[right] = min(min_len[right], length)
                
        return ans if ans != float('inf') else -1