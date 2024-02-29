# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        result=[]
        def inorder(node,r,c):
            if not node:
                return 
            inorder(node.left,r+1,c-1)
            result.append([r,c,node.val])
            inorder(node.right,r+1,c+1)
        inorder(root,0,0)
        result.sort(key=lambda x:(x[1],x[0],x[2]))
        cc=defaultdict(list)
        for i in result:
            cc[i[1]].append(i[-1])
        # print(cc)
        return list(cc.values())
       