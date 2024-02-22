class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        all=list(zip(position,speed))
        all.sort( key=lambda x:x[0] ,reverse=True)
        # print(all)
        time=[]
        for s,v in all:
            re=(target-s)/v
            if time:
                if time[-1]<re:
                    time.append(re)
            else:
                time.append(re)
            # print(time)
        return len(time)