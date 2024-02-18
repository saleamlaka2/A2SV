class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        window=len(cardPoints)-k
        tot=0
        result=float("inf")
        l=0
        
        for r in range(len(cardPoints)):
            tot+=cardPoints[r]
            if l<len(cardPoints) and r-l+1>window:
                tot-=cardPoints[l]
                l+=1
            if r-l+1==window:
                result=min(result,tot)
        return sum(cardPoints)-result    
        