class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        i = 0
        result = []

        while i < len(nums):
            if (i != 0) and (nums[i] == nums[i-1]):
                i+=1
                continue
            left = i + 1
            right = len(nums) - 1

            while left < right:
                if (left != i+1) and (nums[left] == nums[left - 1]):
                    left += 1
                    continue
                if (right != len(nums) - 1) and (nums[right] == nums[right + 1]):
                    right -= 1
                    continue
                
                total = nums[left] + nums[right]

                if total == -nums[i]:
                    result.append([nums[i] , nums[left] , nums[right]])
                    left += 1
                    right -= 1
                
                if total < -nums[i]:
                    left += 1

                if total > -nums[i]:
                    right -= 1
                
            i+=1
        
        return result




        