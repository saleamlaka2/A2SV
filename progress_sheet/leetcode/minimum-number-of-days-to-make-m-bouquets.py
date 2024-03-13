class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def check(t):
            no_bouquets=0
            no_flowers=0
            for i in range(len(bloomDay)):
                if bloomDay[i]<=t:
                    no_flowers+=1
                else:
                    no_flowers=0
                if no_flowers==k:
                    no_bouquets+=1
                    no_flowers=0
            # print(t,no_bouquets,no_bouquets>=m)
            return no_bouquets>=m

 
        l=min(bloomDay)
        r=max(bloomDay)
        
        while r>l:
            mid=(l+r)//2
            
            if check(mid):
                r=mid
            else:
                l=mid+1
        print("l",l)
        return l if check(l) else -1
                
                
                
            