class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        hashmap=Counter()
        l=0
        tot=0
        result=0
        for r in range(len(nums)):
            hashmap[nums[r]]+=1
            tot+=nums[r]
            while l<len(nums) and  r-l+1!=len(hashmap):
                hashmap[nums[l]]-=1
                if hashmap[nums[l]]==0:
                    hashmap.pop(nums[l])
                tot-=nums[l]
                l+=1
            if len(hashmap)==r-l+1:
                result=max(result,tot)
        return result


        