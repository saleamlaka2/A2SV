class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def check(m):
            ind=bisect_left(citations,m)
            return  (len(citations)-ind)>=m
        low=0
        high=max(citations)
        re=0
        while low<=high:
            mid=(low+high)//2
            if check(mid):
                re=max(re,mid)
                low=mid+1
            else:
                high=mid-1
        return re



