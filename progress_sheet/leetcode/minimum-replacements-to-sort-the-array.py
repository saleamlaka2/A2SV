class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        prev_number=nums[-1]
        result=0
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<=prev_number:
                prev_number=nums[i]
            else:
                number_of_divison=ceil(nums[i]/prev_number)
                result+=number_of_divison-1
                prev_number=nums[i]//number_of_divison
        return result

        