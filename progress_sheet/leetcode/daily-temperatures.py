class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0 for _ in range(len(temperatures))]
        stack=[]

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]]<temperatures[i]:
                poped=stack.pop()
                result[poped]=(i-poped)
            stack.append(i)
        
        
        return result

        


        