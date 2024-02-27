class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n==1:
            return 0
        parent=self.kthGrammar(n-1,ceil(k/2))
        is_odd=k%2==1
        if parent==1:
            return 1 if is_odd else 0
        else:
            return 0 if is_odd else 1
