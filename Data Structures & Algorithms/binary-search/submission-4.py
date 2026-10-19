class Solution:
    def search(self, nums: List[int], target: int) -> int:
        result = -1
        left = 0
        right = len(nums) - 1

        while left <= right:
            value = (left + right) // 2

            print ( value )

            if target > nums[value]:
                left = value + 1
            elif target < nums[value]:
                right = value - 1
            else:
                result = value
                break
        return result