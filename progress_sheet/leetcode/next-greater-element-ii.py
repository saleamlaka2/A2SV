class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result=[-1]*len(nums)
        stack=[]
        temp=nums+nums
        for i in range(len(temp)):
            while stack and temp[stack[-1]]<temp[i]:
                poped=stack.pop()
                if poped<len(result):
                    result[poped]=temp[i]
            stack.append(i)
        return result