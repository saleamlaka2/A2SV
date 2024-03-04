class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def sub(arr,j):
            result.append(arr)
            for i in range(j,len(nums)):
                sub(arr+[nums[i]],i+1)
            return 
        sub([],0)
        return result