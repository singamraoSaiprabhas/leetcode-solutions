class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = {i: [] for i in range(1, n + 1)}
        for u, v, dist in roads:
            graph[u].append((v, dist))
            graph[v].append((u, dist)) 
            
        queue = deque([1])
        visited = set([1])
        min_score = float('inf') 
        while queue:
            current_city = queue.popleft()
            for neighbor, dist in graph[current_city]:
                min_score = min(min_score, dist)
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return min_score


