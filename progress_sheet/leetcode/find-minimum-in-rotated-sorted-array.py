class Solution:
    def findMin(self, nums: List[int]) -> int:
        def check(m):
            if m+1<len(nums):
                if nums[m]>nums[m+1]:
                    return True
            return False
        low=0
        high=len(nums)-1

        while low<=high:
            mid=(low+high)//2
            # print(mid,check(mid))
            if check(mid):
                return nums[mid+1]
            elif nums[mid]<nums[0]:
                high=mid-1
            else:
                low=mid+1
        return nums[0]