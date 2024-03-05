class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def perm(ind):
            if ind==len(nums)-1:
                result.append(nums[:])
                return 
            for i in range(ind,len(nums)):
                nums[ind],nums[i]=nums[i],nums[ind]
                perm(ind+1)
                nums[ind],nums[i]=nums[i],nums[ind]
        perm(0)
        return result

