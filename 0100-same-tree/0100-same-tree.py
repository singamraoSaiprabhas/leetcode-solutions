# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if not p and not q:
            return True
        
        # One node is empty, or values do not match
        if not p or not q or p.val != q.val:
            return False
        
        # Check both left and right subtrees recursively
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)