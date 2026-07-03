class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        
        online[0] = True
        online[n - 1] = True
        
        adj = [[] for _ in range(n)]
        unique_costs = set()
        
        for u, v, cost in edges:
            adj[u].append((v, cost))
            unique_costs.add(cost)
            
        sorted_costs = sorted(list(unique_costs))
        
        def is_path_possible(min_required_cost: int) -> bool:
           
            dist = [float('inf')] * n
            dist[0] = 0
            pq = [(0, 0)]  
            
            while pq:
                current_dist, u = heapq.heappop(pq)
                
                if current_dist > dist[u]:
                    continue
                    
                if u == n - 1:
                    return current_dist <= k
                    
                for v, weight in adj[u]:
                  
                    if not online[v] or weight < min_required_cost:
                        continue
                        
                    new_dist = current_dist + weight
                    
                    if new_dist < dist[v]:
                        dist[v] = new_dist
                        heapq.heappush(pq, (new_dist, v))
       
            return dist[n - 1] <= k

        ans = -1
        left, right = 0, len(sorted_costs) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if is_path_possible(sorted_costs[mid]):
                ans = sorted_costs[mid]
                left = mid + 1  
            else:
                right = mid - 1 
                
        return ans