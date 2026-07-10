class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        V = sorted(list(set(nums)))
        m = len(V)
        val_to_idx = {val: i for i, val in enumerate(V)}
        
        comp = [0] * m
        for i in range(1, m):
            if V[i] - V[i-1] <= maxDiff:
                comp[i] = comp[i-1]
            else:
                comp[i] = comp[i-1] + 1
                
        LOG = 20
        up = [[0] * LOG for _ in range(m)]
        for i in range(m):
            furthest_idx = bisect.bisect_right(V, V[i] + maxDiff) - 1
            up[i][0] = furthest_idx
            
        for j in range(1, LOG):
            for i in range(m):
                up[i][j] = up[up[i][j-1]][j-1]
                
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
                
            val_u = nums[u]
            val_v = nums[v]
            
            if val_u == val_v:
                ans.append(1)
                continue
                
            if val_u > val_v:
                val_u, val_v = val_v, val_u
                
            a = val_to_idx[val_u]
            b = val_to_idx[val_v]
            
            if comp[a] != comp[b]:
                ans.append(-1)
                continue
                
            jumps = 0
            curr = a
            
            for k in range(LOG - 1, -1, -1):
                if up[curr][k] < b:
                    curr = up[curr][k]
                    jumps += (1 << k)
            
            ans.append(jumps + 1)
            
        return ans