import heapq
from typing import List

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        # Min-heap for available servers: (weight, index)
        available = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(available)
        
        # Min-heap for busy servers: (free_time, weight, index)
        busy = []
        
        ans = []
        time = 0
        
        for j, task_time in enumerate(tasks):
            # The current task arrives at second j. 
            # Advance logical time to j if it's currently behind.
            time = max(time, j)
            
            # If no servers are available, fast-forward time to when the next server frees up.
            if not available:
                time = busy[0][0]
            
            # Free all servers that have finished their tasks by the current time.
            while busy and busy[0][0] <= time:
                _, weight, index = heapq.heappop(busy)
                heapq.heappush(available, (weight, index))
            
            # Assign the current task to the highest-priority available server.
            weight, index = heapq.heappop(available)
            ans.append(index)
            
            # Push the server into the busy heap with its new completion time.
            heapq.heappush(busy, (time + task_time, weight, index))
            
        return ans