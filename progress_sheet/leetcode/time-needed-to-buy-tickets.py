class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time=0
        tick=deque()
        for i in range(len(tickets)):
            tick.append(i)
        result=tickets[:]
        while result[k]:
            result[tick[0]]-=1
            poped=tick.popleft()
            if result[poped]>0:
                tick.append(poped)
            time+=1
        return time

