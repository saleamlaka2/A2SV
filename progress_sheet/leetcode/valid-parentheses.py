class Solution:
    def isValid(self, s: str) -> bool:
        para={")":"(","}":"{","]":"["}
        stack=[]
        for i in range(len(s)):
            if s[i] in para:
                if not stack or  stack.pop()!=para[s[i]]:
                    return False
            else:
                stack.append(s[i])
        return True if not stack else False

