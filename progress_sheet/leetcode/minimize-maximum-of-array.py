class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        re=nums[0]
        tot=nums[0]
        for i in range(1,len(nums)):
            tot+=nums[i]
            if nums[i]>re:
                # print(round(tot/(i+1)),i+1,tot)
                re=max(re,ceil(tot/(i+1)))
        return re
