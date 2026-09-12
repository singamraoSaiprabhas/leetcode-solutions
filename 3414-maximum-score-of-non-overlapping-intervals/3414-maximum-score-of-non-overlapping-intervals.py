class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        
        # Store tuples of (start, end, weight, original_index)
        items = [(intervals[i][0], intervals[i][1], intervals[i][2], i) for i in range(n)]
        
        # Sort intervals by their start time
        items.sort(key=lambda x: x[0])
        
        # Extract purely the start times for fast binary searching
        start_times = [x[0] for x in items]
        
        # dp[i][k] will store the tuple: (max_weight, lexicographically_smallest_indices)
        # We need state up to k=4 intervals. N+1 handles out-of-bound gracefully.
        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]
        
        def get_better(res1, res2):
            if res1[0] > res2[0]:
                return res1
            elif res2[0] > res1[0]:
                return res2
            else:
                # If weights are identical, return the lexicographically smaller index list
                return res1 if res1[1] < res2[1] else res2

        # Traverse backward to build the optimal suffix solutions
        for i in range(n - 1, -1, -1):
            l, r, w, orig_idx = items[i]
            
            # Find the first interval that starts strictly after the current one ends
            next_i = bisect.bisect_right(start_times, r)
            
            for k in range(1, 5):
                # Option 1: Skip the current interval
                res1 = dp[i + 1][k]
                
                # Option 2: Take the current interval
                prev_weight, prev_indices = dp[next_i][k - 1]
                new_weight = w + prev_weight
                
                # Sort the indices combination to maintain ascending order for comparison
                new_indices = sorted([orig_idx] + prev_indices)
                res2 = (new_weight, new_indices)
                
                # Store the optimal choice between skipping and taking
                dp[i][k] = get_better(res1, res2)
                
        # The answer for the entire array taking at most 4 intervals
        return dp[0][4][1]