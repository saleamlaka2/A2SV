class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_queue=deque()
        d_queue=deque()

        for i in range(len(senate)):
            if senate[i]=="R":
                r_queue.append(i)
            else:
                d_queue.append(i)
        while r_queue and d_queue:
            r=r_queue.popleft()
            d=d_queue.popleft()

            if r<d:
                r_queue.append(d+len(senate))
            else:
                d_queue.append(r+len(senate))
        return "Radiant" if r_queue else "Dire"

