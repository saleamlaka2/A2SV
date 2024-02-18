class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        black=0
        white=0
        l=0
        maxBlack=0
        for r in range(len(blocks)):
            if blocks[r]=="W":
                white+=1
            else:
                black+=1
            while (r-l+1)>k:
                if blocks[l]=="W":
                    white-=1
                else:
                    black-=1
                l+=1
            if (r-l+1)==k:
                maxBlack=max(maxBlack,black)
        return k-maxBlack