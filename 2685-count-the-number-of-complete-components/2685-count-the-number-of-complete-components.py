class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited = set()
        complete_count = 0
        for i in range(n):
            if i not in visited:
                v_count = 0
                degree_sum = 0
                queue = [i]
                visited.add(i)
                
                while queue:
                    node = queue.pop(0)
                    v_count += 1
                    
                    degree_sum += len(adj[node]) 
                    
                    for neighbor in adj[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
                            
                if degree_sum == v_count * (v_count - 1):
                    complete_count += 1
                    
        return complete_count