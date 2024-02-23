class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        minElement=nums[0]
        result=0
        for ele in nums:
            # print(ele,minElement,k)
            if (ele-minElement)>k:
                result+=1
                minElement=ele
        return result+1