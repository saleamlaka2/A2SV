class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap=defaultdict(lambda :-1)
        stack=[]
        for ele in nums2:
            while stack and  stack[-1]<ele:
                hashmap[stack.pop()]=ele
            stack.append(ele)
        result=[]
        for el in nums1:
            result.append(hashmap[el])
        return result