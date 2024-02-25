class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(name)>len(typed):
            return False
        else:
            l=0
            prev=1
            for i in range(len(name)):
                if l<len(typed):
                    if name[i]==typed[l]:
                        l+=1
                    else:
                        while l<len(typed) and typed[l]==prev:
                            l+=1
                        if l<len(typed) and name[i]==typed[l]:
                            l+=1
                        else:
                            return False
                    prev=name[i]
                else:
                    return False
        while l<len(typed) and typed[l]==prev:
            l+=1
        return True if l>=len(typed) else False