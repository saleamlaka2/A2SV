class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        currentSum=0
        result=0
        hashmap=Counter()
        for num in nums:
            currentSum+=num
            if currentSum%k==0:
                result+=1
            result+=hashmap[currentSum%k]
            hashmap[currentSum%k]+=1
        return result
            