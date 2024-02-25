class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        sortedDeck=list(sorted(deck,reverse=True))
        result=deque(list(range(0,len(deck))))
        
        for i in range(0,len(deck),2):
            result[i]=sortedDeck.pop()
        order=[]
        result2=result.copy()
        while result:
            pop1=result.popleft()
            order.append(pop1)
            if result:
                result.append(result.popleft())
        ind=ceil(len(deck)/2)
        for k in order[ind:]:
            result2[k]=sortedDeck.pop()
        return (list(result2))
        
