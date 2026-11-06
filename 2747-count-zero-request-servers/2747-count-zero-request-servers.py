from typing import List
from collections import defaultdict

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        # Sort logs chronologically by their timestamps
        logs.sort(key=lambda log: log[1])
        
        # Sort queries but keep their original indices to place answers correctly
        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)])
        
        ans = [0] * len(queries)
        active_servers = defaultdict(int)
        
        left = 0
        right = 0
        m = len(logs)
        
        # Sliding window approach for each query
        for q, original_index in sorted_queries:
            window_start = q - x
            window_end = q
            
            # Expand the window to the right to include all logs up to window_end
            while right < m and logs[right][1] <= window_end:
                active_servers[logs[right][0]] += 1
                right += 1
                
            # Shrink the window from the left to remove logs before window_start
            while left < right and logs[left][1] < window_start:
                server_id = logs[left][0]
                active_servers[server_id] -= 1
                
                # Remove the server from the dictionary if it has no active requests in the window
                if active_servers[server_id] == 0:
                    del active_servers[server_id]
                left += 1
                
            # The number of servers that received no requests
            ans[original_index] = n - len(active_servers)
            
        return ans