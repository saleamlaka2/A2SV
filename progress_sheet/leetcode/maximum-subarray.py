class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub=float("-inf")
        cur_sub=0
        for i in nums:
            cur_sub+=i
            max_sub=max(max_sub,cur_sub)
            cur_sub=max(0,cur_sub)
        return max_sub
        