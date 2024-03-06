class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        iof=Counter()
        first=[]
        for i in range(len(intervals)):
            iof[intervals[i][0]]=i
            first.append(intervals[i][0])
        first.sort()
        result=[]
        for k in range(len(intervals)):
            ind=bisect_left(first,intervals[k][1])
            # print([ind,first,intervals[k][1]])
            if ind<len(intervals):
                result.append(iof[first[ind]])
            else:
                result.append(-1)
        return result
        