class Solution:
    def maxDepth(self, s: str) -> int:
        maxDepth=0
        curr_depth=0
        for i in s:
            if i=="(":
                curr_depth+=1
            if i==")":
                 curr_depth-=1
            if curr_depth>maxDepth:
                maxDepth=curr_depth
        return maxDepth              

        
        