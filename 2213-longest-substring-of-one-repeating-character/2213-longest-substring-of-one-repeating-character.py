class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        
        # Parallel arrays for Segment Tree nodes to optimize execution time in Python
        tree_longest = [0] * (4 * n)
        tree_pref_len = [0] * (4 * n)
        tree_suff_len = [0] * (4 * n)
        tree_pref_char = [''] * (4 * n)
        tree_suff_char = [''] * (4 * n)
        tree_size = [0] * (4 * n)
        
        s_list = list(s)
        
        def push_up(node, left, right):
            tree_size[node] = tree_size[left] + tree_size[right]
            tree_pref_char[node] = tree_pref_char[left]
            tree_suff_char[node] = tree_suff_char[right]
            
            # Calculate Prefix Length
            tree_pref_len[node] = tree_pref_len[left]
            if tree_pref_len[left] == tree_size[left] and tree_suff_char[left] == tree_pref_char[right]:
                tree_pref_len[node] += tree_pref_len[right]
                
            # Calculate Suffix Length
            tree_suff_len[node] = tree_suff_len[right]
            if tree_suff_len[right] == tree_size[right] and tree_suff_char[left] == tree_pref_char[right]:
                tree_suff_len[node] += tree_suff_len[left]
                
            # Calculate Longest Continuous Segment
            tree_longest[node] = max(tree_longest[left], tree_longest[right])
            if tree_suff_char[left] == tree_pref_char[right]:
                tree_longest[node] = max(tree_longest[node], tree_suff_len[left] + tree_pref_len[right])

        def build(node, start, end):
            if start == end:
                tree_longest[node] = 1
                tree_pref_len[node] = 1
                tree_suff_len[node] = 1
                tree_pref_char[node] = s_list[start]
                tree_suff_char[node] = s_list[start]
                tree_size[node] = 1
                return
            mid = (start + end) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            push_up(node, 2 * node, 2 * node + 1)
            
        def update(node, start, end, idx, val):
            if start == end:
                s_list[idx] = val
                tree_pref_char[node] = val
                tree_suff_char[node] = val
                return
            mid = (start + end) // 2
            if idx <= mid:
                update(2 * node, start, mid, idx, val)
            else:
                update(2 * node + 1, mid + 1, end, idx, val)
            push_up(node, 2 * node, 2 * node + 1)
            
        if not s:
            return []
            
        # Build the initial Segment Tree
        build(1, 0, n - 1)
        ans = []
        
        # Process each query
        for i in range(len(queryIndices)):
            idx = queryIndices[i]
            c = queryCharacters[i]
            update(1, 0, n - 1, idx, c)
            ans.append(tree_longest[1])
            
        return ans