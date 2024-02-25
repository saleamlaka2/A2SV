class Solution(object):
    def characterReplacement(self, s, k):
        result=0
        l=0
        co=Counter()
        for r in range(len(s)):
            co[s[r]]+=1
            while (r-l+1)-max(co.values())>k:
                co[s[l]]-=1
                l+=1
            result=max(result,r-l+1)
        return result
                
        