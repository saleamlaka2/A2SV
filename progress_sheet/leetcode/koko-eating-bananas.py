class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(m):
            time_needed=0
            for i in range(len(piles)):
                time_needed+=ceil(piles[i]/m)
            return time_needed<=h
        low=1
        high=max(piles)
        re=float("inf")
        while low<=high:
            mid=(low+high)//2

            if check(mid):
                re=min(re,mid)
                high=mid-1
            else:
                low=mid+1
        return re

