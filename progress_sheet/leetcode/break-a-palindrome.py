class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        def check(arr):
            l=0
            r=len(arr)-1

            while l<r:
                if arr[l]!=arr[r]:
                    return False
                l+=1
                r-=1
            return True
        if len(palindrome)==1:
            return ""
        ch=True
        s=list(palindrome)
        for i in range(len(s)):
            if s[i]!="a":
                s[i]="a"
                break
        if ch and check(s):
            s=list(palindrome)
            s[-1]="b"
        return "".join(s)