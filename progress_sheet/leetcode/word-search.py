class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        result=False
        r_len=len(board)
        c_len=len(board[0])
        def inbound(r,c):
            return 0<=r<r_len and 0<=c<c_len
        directions=[[0,-1],[-1,0],[0,1],[1,0]]
        visited=set()
        def dfs(row,col,arr):
            anflag=True
            nonlocal result
            arr.append(board[row][col])
            ch=True
            if arr:
                ind=len(arr)-1
                if ind<len(word) and arr[-1]!=word[ind]:
                    anflag=False
            # print(arr,word)
            if len(arr)==len(word):
                for i in range(len(word)):
                    if word[i]!=arr[i]:
                        ch=False
                        break
                if ch:
                    result=True
                anflag=False
            visited.add((row,col))
            if anflag:
                for rr,cc in directions:
                    nr=row+rr
                    nc=col+cc
                    if inbound(nr,nc) and (nr,nc) not in visited:
                        dfs(nr,nc,arr)
            arr.pop()
            visited.remove((row,col))
            
            return
        flag=True
        for i in range(r_len):
            if not flag:
                break
            for j in range(c_len):
                if not result:
                    dfs(i,j,[])
                else:
                    flag=False
                    break
        return result    
