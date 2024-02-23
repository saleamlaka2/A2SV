class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
       
        minstack=deque()
        maxstack=deque()
        l=0
        result=0
        for r in range(len(nums)):
            while minstack and minstack[-1]>nums[r]:
                minstack.pop()
            minstack.append(nums[r])
            while maxstack and maxstack[-1]<nums[r]:
                maxstack.pop()
            maxstack.append(nums[r])
            # print(maxstack,minstack)
            while l<len(nums) and maxstack and minstack and (maxstack[0]-minstack[0])>limit:
                if minstack[0]==nums[l]:
                    minstack.popleft()
                if maxstack[0]==nums[l]:
                    maxstack.popleft()
                l+=1
            if maxstack and minstack and (maxstack[0]-minstack[0])<=limit:
                result=max(result,r-l+1)
        return result

           
        

