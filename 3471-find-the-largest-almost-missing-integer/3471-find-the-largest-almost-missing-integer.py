class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        subarray_counts = {}
        n = len(nums)
        
        # Count the number of subarrays of size k each unique value appears in
        for i in range(n - k + 1):
            unique_in_window = set(nums[i : i + k])
            for val in unique_in_window:
                subarray_counts[val] = subarray_counts.get(val, 0) + 1
        
        # Find the maximum element that appears in exactly 1 subarray
        largest_val = -1
        for val, count in subarray_counts.items():
            if count == 1 and val > largest_val:
                largest_val = val
                
        return largest_val