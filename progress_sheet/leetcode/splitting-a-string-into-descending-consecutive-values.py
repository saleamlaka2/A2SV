class Solution:
    def splitString(self, s: str) -> bool:
        def ss(j,prev):
            if j>=len(s):
                return True
            # print("j",j)
            for k in range(j,len(s)):
                val=int(s[j:k+1])
                # print("val",val)
                if val+1==prev and ss(k+1,val):
                        return True
            return False
           
            
        for i in range(len(s)-1):
            ele=int(s[:i+1])
            # print("ele",ele)
            if ss(i+1,ele):
                return True
        return False
        
        