class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        hashmap={0:1}
        result=0
        ps=[]
        accumulator=0
        for num in nums:
            accumulator+=num
            ps.append(accumulator)
        
        for ele in ps:
            if (ele-goal) in hashmap:
                result+=hashmap[ele-goal]
            if ele in hashmap:
                hashmap[ele]+=1
            else:
                hashmap[ele]=0
                hashmap[ele]+=1
        return result
