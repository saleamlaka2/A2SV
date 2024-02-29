# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        re=deque([root.val]) if root else deque()
        queue=deque([root])  if root else deque()
        result=[]
        flag=True
        while queue:
            re1=re.copy()
            if flag:
                result.append(list(re1))
                flag=False
            else:
                result.append(list(re1)[::-1])
                flag=True
            for _ in range(len(queue)):
                node=queue.popleft()
                re.popleft()
                if node.left:
                    queue.append(node.left)
                    re.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    re.append(node.right.val)
        return result