class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result=[]
        visited=set()
        nums.sort()
        def sub(arr,j):
            if tuple(arr) not in visited:
                result.append(arr)
                visited.add(tuple(arr))
            for i in range(j,len(nums)):
                sub(arr+[nums[i]],i+1)
            return 
        sub([],0)
        return result