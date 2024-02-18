class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        hashmap=Counter()
        l=0
        result=float("inf")
        for r in range(len(cards)):
            hashmap[cards[r]]+=1
            if len(hashmap)!=r-l+1:
                result=min(r-l+1,result)
            while l<len(cards) and  len(hashmap)!=r-l+1:
                if len(hashmap)!=r-l+1:
                    result=min(r-l+1,result)
                hashmap[cards[l]]-=1
                if hashmap[cards[l]]==0:
                    hashmap.pop(cards[l])
                l+=1
        return result if result!=float('inf') else -1
                


