class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(m):
            tot=0
            partition=1
            for i in range(len(nums)):
                tot+=nums[i]
                if tot>m:
                    partition+=1
                    tot=nums[i]
            return partition
        low=max(nums)
        high=sum(nums)

        result=float("inf")
        while low<=high:
            mid=(low+high)//2
            
            re=check(mid)
            print(mid,re)
            if re >k:
                low=mid+1
               
            else:
                result=min(result,mid)
                high=mid-1
        return result

            