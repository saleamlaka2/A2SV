class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        arr=[]
        for a,b in costs:
            arr.append([a,b,a-b])
        arr.sort(key=lambda x:x[-1])
        print(arr)
        aa=0
        bb=0
        for i in range(len(arr)):
            if i>=((len(costs)//2)):
                bb+=arr[i][1]
            else:
                aa+=arr[i][0]
        print(aa,bb)
        return aa+bb
