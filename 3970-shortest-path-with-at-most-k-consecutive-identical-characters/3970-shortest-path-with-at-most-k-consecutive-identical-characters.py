import heapq
from collections import defaultdict
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        # Edge case: If k is 0, we can't even include the starting node
        if k == 0:
            return -1
            
        # Build the adjacency list
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            
        # Priority Queue stores tuples of: (weight, consecutive_count, node)
        # We arrange it this way so heapq implicitly breaks ties by processing 
        # smaller consecutive counts first when weights are identical.
        pq = [(0, 1, 0)]
        
        # min_count[i] tracks the smallest consecutive_count we've seen when reaching node i.
        min_count = [float('inf')] * n
        
        while pq:
            w, c, u = heapq.heappop(pq)
            
            # Pruning Step: 
            # If we've already reached this node with an equal or fewer consecutive 
            # characters (and naturally, a smaller or equal weight due to Dijkstra), skip it.
            if c >= min_count[u]:
                continue
            
            # Record this new best consecutive count for the current node
            min_count[u] = c
            
            # Because of Dijkstra's properties, the first time we pop the destination node,
            # it is guaranteed to be the minimum total weight.
            if u == n - 1:
                return w
                
            # Explore outgoing edges
            for v, edge_w in adj[u]:
                # Calculate the consecutive count if we move to node v
                next_c = c + 1 if labels[u] == labels[v] else 1
                
                # Only push valid paths to the priority queue
                if next_c <= k:
                    heapq.heappush(pq, (w + edge_w, next_c, v))
                    
        return -1