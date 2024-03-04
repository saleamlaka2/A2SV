# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result=0
        def preorder(root):
            nonlocal result
            if root:
                preorder(root.left)
                if root.val>=low and root.val<=high:
                    result+=root.val
                preorder(root.right)
        preorder(root)
        return result

