# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return [float("-inf"),float("inf"),float("-inf")]
            left=dfs(node.left)
            right=dfs(node.right)
            re1=min(node.val,left[1],right[1])
            re2=max(node.val,left[2],right[2])
            re=max(left[0],right[0],abs(node.val-re1),abs(node.val-re2))
            # print([re,re1,re2])
            return [re,re1,re2]
        return (dfs(root)[0])
