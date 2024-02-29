# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,node,arr):
        if node is None :
            return True
        if not (self.inorder(node.left,arr)):
            return False
        if arr and arr[-1]>=node.val:
            return False
        arr.append(node.val)
        if not (self.inorder(node.right,arr)):
            return False
        return True
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
            return self.inorder(root,[])