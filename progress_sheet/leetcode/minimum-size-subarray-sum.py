class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        currSum=0
        result=float("inf")
        for r in range(len(nums)):
            currSum+=nums[r]
            while l<len(nums) and  currSum-nums[l] >=target:
                currSum-=nums[l]
                l+=1
            if currSum>=target:
                result=min(result,r-l+1)
        return result if result!=float("inf") else 0
