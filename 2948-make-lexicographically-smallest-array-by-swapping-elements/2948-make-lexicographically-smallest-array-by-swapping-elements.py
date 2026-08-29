class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        if not nums:
            return []

        # Pair each number with its original index and sort by the number's value
        pairs = sorted([(nums[i], i) for i in range(n)])
        
        res = [0] * n
        i = 0
        
        while i < n:
            j = i + 1
            # Expand the group as long as the adjacent difference is within the limit
            while j < n and pairs[j][0] - pairs[j-1][0] <= limit:
                j += 1
            
            # The current group of values is from index i to j-1 in the sorted pairs
            # Extract and sort their original indices
            group_indices = sorted([pairs[k][1] for k in range(i, j)])
            
            # Place the sorted values back into the sorted original indices
            for k in range(len(group_indices)):
                res[group_indices[k]] = pairs[i + k][0]
                
            i = j
            
        return res