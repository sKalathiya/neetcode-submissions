class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        total = 0

        while left <= right:
             
            left_value = height[left]
            right_value = height[right]

            if left_max <= right_max:
                total += max(0,min(left_max , right_max) - height[left])
                left_max = max(left_max, left_value)
                left+=1
            else:
                total += max(0,min(left_max , right_max) - height[right])
                right_max = max(right_max, right_value)
                right-=1
        
        return total

        