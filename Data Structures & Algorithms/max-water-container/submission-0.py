class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        result = (right - left) * min(heights[left],heights[right])
        while left < right:
            temp = (right - left) * min(heights[left],heights[right])

            if temp >= result:
                result = temp

            if heights[left] <= heights[right]:
                left+=1
            else:
                right-=1
        
        return result

            


        