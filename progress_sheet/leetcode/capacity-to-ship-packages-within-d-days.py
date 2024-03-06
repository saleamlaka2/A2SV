class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(re):
            days_needed=1
            tot=0
            for i in range(len(weights)):
                tot+=weights[i]
                # print(tot,re)
                if tot>re:
                    days_needed+=1
                    tot=weights[i]
            
            return days_needed<=days
        low=max(weights)
        high=sum(weights)
        res=float("inf")
        while low<=high:
            mid=(low+high)//2
            # print(mid,check(mid))
            if check(mid):
                res=min(res,mid)
                high=mid-1
            else:
                low=mid+1
        return low

