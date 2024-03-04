class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result=[]
        def combination(arr,j):
            if len(arr)==k:
                result.append(arr)
                return 
            for i in range(j,n+1):
                combination(arr+[i],i+1)
        combination([],1)
        return result