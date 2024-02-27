class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for ele  in s:
            if ele=="]":
                result=""
                while stack and stack[-1]!="[":
                    result+=stack.pop()
               
                stack.pop()
                dig=""
                while stack and stack[-1].isdigit():
                    dig+=stack.pop()
                num=int(dig[::-1])
                word=result[::-1]
                    
                stack.extend(list(num*word))
            else:
                stack.append(ele)
        return "".join(stack)
                

        