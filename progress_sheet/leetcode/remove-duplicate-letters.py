class Solution:
    def removeDuplicateLetters(self, s: str) -> str:  
        hashmap=Counter()
        for i in range(len(s)):  
            hashmap[s[i]]=i
        stack=[]  
        visited=set()  
        
        for k in range(len(s)):
            if s[k] not in visited:
                while stack and stack[-1]>s[k] and hashmap[stack[-1]]>k:
                    poped=stack.pop()
                    visited.remove(poped)

                stack.append(s[k])
                visited.add(s[k])
        result="".join(stack)
        return result 
        