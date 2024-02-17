class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        li=[]
        mx=0
        for i in range(len(arr))[::-1]:
            m=max(arr[:i+1])
            if arr[i]==m:
                pass
            elif arr.index(m)==0:
                arr[:i+1]=arr[:i+1][::-1]
                li.append(i+1)
                mx+=1
            else:
                li.append(arr.index(m)+1)
                mx+=1
                arr[:arr.index(m)+1]=arr[:arr.index(m)+1][::-1]
                arr[:i+1]=arr[:i+1][::-1]
                li.append(i+1)
                mx+=1
        return li
        



