class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxQ = 0
        l, r = 0, len(heights)-1

        while l<r:
            maxQ = max((r - l)*min(heights[l], heights[r]), maxQ)
            if heights[l] <= heights[r]:
                l+=1
            elif heights[l] >= heights[r]:
                r-=1  
        return maxQ          
        