class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        cc=Counter(answers)
        result=0
        for ele in answers:
            if cc[ele]<ele+1:
                if cc[ele]>0:
                    result+=(ele+1)
                    cc[ele]=0
            else:
                result+=(ele+1)
                cc[ele]-=(ele+1)
            
        return result