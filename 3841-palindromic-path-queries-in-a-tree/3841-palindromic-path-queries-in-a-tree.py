class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        # Step 1: Build Adjacency List
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # Step 2: Initialize Structures for DFS & Binary Lifting
        in_time = [0] * n
        out_time = [0] * n
        depth = [0] * n
        up = [[0] * 18 for _ in range(n)]
        mask = [0] * n
        
        timer = 0
        
        # Iterative DFS to avoid hitting python recursion limits on deep trees
        # stack stores: (node, parent, state) where state 0 = pre-visit, 1 = post-visit
        stack = [(0, 0, 0)]
        mask[0] = 1 << (ord(s[0]) - 97)
        
        while stack:
            u, p, state = stack.pop()
            if state == 0:
                timer += 1
                in_time[u] = timer
                up[u][0] = p
                
                # Binary lifting precomputation
                for i in range(1, 18):
                    up[u][i] = up[up[u][i-1]][i-1]
                    
                stack.append((u, p, 1))
                for v in adj[u]:
                    if v != p:
                        depth[v] = depth[u] + 1
                        mask[v] = mask[u] ^ (1 << (ord(s[v]) - 97))
                        stack.append((v, u, 0))
            else:
                out_time[u] = timer
                
        # Step 3: Fenwick Tree (Binary Indexed Tree) for Subtree XOR Updates
        bit = [0] * (n + 2)
        
        def add(idx, val):
            while idx <= n + 1:
                bit[idx] ^= val
                idx += idx & (-idx)
                
        def query_bit(idx):
            res = 0
            while idx > 0:
                res ^= bit[idx]
                idx -= idx & (-idx)
            return res
            
        # Initialize BIT to hold initial point masks
        for i in range(n):
            add(in_time[i], mask[i])
            add(in_time[i] + 1, mask[i]) # difference array logic for point query
            
        # LCA Finder using binary lifting
        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for i in range(18):
                if (diff >> i) & 1:
                    u = up[u][i]
            if u == v:
                return u
            for i in range(17, -1, -1):
                if up[u][i] != up[v][i]:
                    u = up[u][i]
                    v = up[v][i]
            return up[u][0]
            
        # Step 4: Process Queries
        chars = list(s)
        ans = []
        
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                old_c = chars[u]
                
                if old_c != c:
                    # XOR difference to apply to the subtree
                    diff = (1 << (ord(old_c) - 97)) ^ (1 << (ord(c) - 97))
                    chars[u] = c
                    # Range XOR update on the subtree mapped by the Euler Tour
                    add(in_time[u], diff)
                    add(out_time[u] + 1, diff)
            else:
                u = int(parts[1])
                v = int(parts[2])
                
                # Fetch masks recursively tracked up to node u and node v
                mask_u = query_bit(in_time[u])
                mask_v = query_bit(in_time[v])
                
                lca = get_lca(u, v)
                lca_mask = 1 << (ord(chars[lca]) - 97)
                
                # Evaluate final mask layout for the specific path segment
                path_mask = mask_u ^ mask_v ^ lca_mask
                
                # Condition for palindrome: strictly 1 or 0 bits sets are validated
                ans.append((path_mask & (path_mask - 1)) == 0)
                
        return ans