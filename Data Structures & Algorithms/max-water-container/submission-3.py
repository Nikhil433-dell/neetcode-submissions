class Solution:
    def maxArea(self, heights: List[int]):
        
        area = 0
        l = 0
        r = len(heights) - 1

        for _ in range(len(heights)-1):
           
            arr = (r-l)*min(heights[l], heights[r])
            area = max(area, arr)
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1


        return area