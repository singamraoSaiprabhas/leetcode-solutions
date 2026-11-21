import sys
from typing import List


class Solution:

  def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
    n = len(parent)
    sys.setrecursionlimit(max(200000, n + 1000))

    # 1. Build adjacency list for the original tree
    adj = [[] for _ in range(n)]
    for i in range(1, n):
      adj[parent[i]].append(i)

    ans = [1] * n
    last_seen = [-1] * 26  # Closest ancestor index for each char 'a'-'z'

    # 2. Single DFS: find new parent on entry, propagate size on exit
    def dfs(u: int) -> None:
      idx = ord(s[u]) - 97
      prev = last_seen[idx]

      # Reattach to closest matching ancestor if one exists; otherwise keep original parent
      target_parent = prev if prev != -1 else parent[u]

      last_seen[idx] = u
      for v in adj[u]:
        dfs(v)
      last_seen[idx] = prev  # Backtrack

      if target_parent != -1:
        ans[target_parent] += ans[u]

    dfs(0)
    return ans