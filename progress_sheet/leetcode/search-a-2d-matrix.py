class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
             return self.binarys2(matrix,target,0,len(matrix)-1)
    def binarys(self,nums,target,l,r):
            while l<=r:
                m=(l+r)//2
                if target>nums[m]:
                    l=m+1
                elif target < nums[m]:
                    r=m-1
                else:
                    return True
            return False
    def binarys2(self,nums,target,l,r):
        while l<=r:
            m=(l+r)//2
            if target>nums[m][-1]:
                l=m+1
            elif target < nums[m][0]:
                r=m-1
            else:
                return self.binarys(nums[m],target,0,len(nums[m])-1)
        return False