# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0
            
            # Recursively get the max path sum of left and right subtrees.
            # If a path sum is negative, we ignore it by taking max(..., 0).
            left_max = max(dfs(node.left), 0)
            right_max = max(dfs(node.right), 0)

            # Task A: Calculate the max path if the current node is the "peak"
            # and update the global max_sum if it's the largest found so far.
            current_path_sum = node.val + left_max + right_max
            self.max_sum = max(self.max_sum, current_path_sum)

            # Task B: Return the maximum path sum that can extend upwards to the parent.
            # We can only choose one branch (left or right) to continue the path.
            return node.val + max(left_max, right_max)

        dfs(root)
        return self.max_sum