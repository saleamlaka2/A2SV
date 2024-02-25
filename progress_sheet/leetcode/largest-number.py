class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def MyCmp(a,b):
            if a+b>b+a:
                return -1
            elif a+b<b+a:
                return 1
            else:
                return 0
        return str(int("".join(list(sorted(list(map(str,nums)),key=cmp_to_key(MyCmp))))))