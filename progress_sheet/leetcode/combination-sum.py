class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        visited=set()
        def comb(arr):
            if sum(arr)>target:
                return
            if sum(arr)==target:
                li=list(sorted(arr))
                if tuple(li) not in visited:
                    result.append(arr)
                    visited.add(tuple(li))
                return 
            for i in range(len(candidates)):
                comb(arr+[candidates[i]])
        comb([])
        return result
            