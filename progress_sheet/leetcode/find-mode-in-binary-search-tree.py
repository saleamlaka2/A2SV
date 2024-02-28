# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        hashmap=Counter()
        def inorder(node):
            if not node:
                return 
            hashmap[node.val]+=1
            inorder(node.left)
            inorder(node.right)
        inorder(root)
        # print(hashmap)
        mx=max(hashmap.values())
        result=[]
        for ele in hashmap:
            if hashmap[ele]==mx:
                result.append(ele)
        return result
