class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        re=0
        if numOnes>0:
          if numOnes>=k:
              return k
          else:
              re+=numOnes
              k-=numOnes
        if numZeros>0:
          if numZeros>=k:
              return re
          else:
              k-=numZeros
        if numNegOnes>0:
          if numNegOnes>=k:
              re-=(k)
              return re
          else:
              re-=numNegOnes
              k-=numNegOnes
        return re
        
        
        
        