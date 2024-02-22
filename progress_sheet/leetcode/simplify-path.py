class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        paths=path.split("/")
        print(paths)
        for ele in paths:
            if ele=="..":
                if stack:
                    stack.pop()
            elif ele=="." or ele=="":
                pass
            else:
                stack.append(ele)
        return ("/"+"/".join(stack))