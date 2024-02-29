# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        re=0
        def inorder(node,arr):
            nonlocal re
            if not node :
                return 
            inorder(node.left,arr)
            arr.append(node.val)
            if len(arr)==k:
                re=arr[-1]
            inorder(node.right,arr)
        inorder(root,[])
        return re
            
