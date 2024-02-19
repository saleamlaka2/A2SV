class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        cc=Counter(s)
        curCount=Counter()
        valid=0
        result=[]
        l=0
        for i,val in enumerate(s):
            curCount[val]+=1
            if curCount[val]==cc[val]:
                valid+=1
            if valid ==len(curCount):
                result.append(i+1-l)
                curCount=Counter()
                valid=0
                l=i+1
        return result

