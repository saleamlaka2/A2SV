# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def preorder(node):
            if not node:
                return 0
            left=1+preorder(node.left)
            right=1+preorder(node.right)
            return max(left,right)
        return preorder(root)
        