class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        import numpy as np
        result=True
        for g in board:
            se=list(set(g))
            se.remove(".")
            re=list(map(lambda x:g.count(x),se))
            if se:
                if max(re)>1:
                    result=False
                    break
        if result==True:
            a=np.array(board)
            ab=np.swapaxes(a,0,1)
            for h in list(ab):
                se=list(set(h))
                se.remove(".")
                re=list(map(lambda x:list(h).count(x),se))
                if se:
                    if max(re)>1:
                        result=False
                        break
        if result==True:    
            abb=a.reshape(9,3,3)
            alll=[]
            for i in range(3):
                all=[]
                all.append(list(abb[0][i]))
                all.append(list(abb[1][i]))
                all.append(list(abb[2][i]))
                alln=np.array(all)
                allr=alln.reshape(9)
                alll.append(list(allr))
            for i in range(3):
                all=[]
                all.append(list(abb[3][i]))
                all.append(list(abb[4][i]))
                all.append(list(abb[5][i]))
                alln=np.array(all)
                allr=alln.reshape(9)
                alll.append(list(allr))
            for i in range(3):
                all=[]
                all.append(list(abb[6][i]))
                all.append(list(abb[7][i]))
                all.append(list(abb[8][i]))
                alln=np.array(all)
                allr=alln.reshape(9)
                alll.append(list(allr))
            for k in alll:
                se=list(set(k))
                se.remove(".")
                re=list(map(lambda x:k.count(x),se))
                if se:
                    if max(re)>1:
                        result=False
                        break
            return(result)


