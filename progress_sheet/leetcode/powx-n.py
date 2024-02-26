class Solution:
    def myPow(self, x: float, n: int) -> float:
        def poww(b,e):
            if e==0:
               return 1
            elif e%2==0:
                return poww(b*b,e//2)
            else:
                return b*poww(b*b,(e-1)//2)
        result=poww(x,abs(n))
        return result if n>=0 else 1/result

        
        