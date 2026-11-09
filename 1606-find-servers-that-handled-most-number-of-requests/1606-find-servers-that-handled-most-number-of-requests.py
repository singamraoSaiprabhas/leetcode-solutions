import heapq
from typing import List

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        # 'free' stores available servers with ID >= (i % k)
        free = list(range(k))
        heapq.heapify(free)
        
        # 'used' stores available servers with ID < (i % k)
        used = []
        
        # 'busy' stores running servers as (end_time, server_id)
        busy = []
        
        # Array to track the number of requests successfully handled by each server
        counts = [0] * k
        
        for i, arr in enumerate(arrival):
            target = i % k
            
            # When the target wraps around to 0, all servers in 'used' are now >= target.
            # Merge them back into 'free' to maintain the invariant.
            if target == 0 and used:
                free.extend(used)
                heapq.heapify(free)
                used.clear()
                
            # Release servers that have finished processing before or at the current arrival time
            while busy and busy[0][0] <= arr:
                _, sid = heapq.heappop(busy)
                
                # Route the freed server to the correct heap based on the current target
                if sid < target:
                    heapq.heappush(used, sid)
                else:
                    heapq.heappush(free, sid)
            
            # 1. Try to assign to the nearest available server >= target
            if free:
                sid = heapq.heappop(free)
            # 2. If none are available >= target, wrap around to 0 and pick the smallest ID
            elif used:
                sid = heapq.heappop(used)
            # 3. If both heaps are empty, drop the request
            else:
                continue
                
            counts[sid] += 1
            # The server will be busy until current arrival time + load time
            heapq.heappush(busy, (arr + load[i], sid))
            
        max_reqs = max(counts)
        # Return all servers that share the maximum request count
        return [i for i in range(k) if counts[i] == max_reqs]