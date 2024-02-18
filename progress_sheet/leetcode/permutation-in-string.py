class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=0
        cs1=Counter(s1)
        countE=Counter()
        for r in range(len(s2)):
            countE[s2[r]]+=1
            while r-l+1>len(s1):
                countE[s2[l]]-=1
                if  countE[s2[l]]==0:
                    countE.pop(s2[l])
                l+=1
            if r-l+1==len(s1):
                if cs1==countE:
                    return True
        return False