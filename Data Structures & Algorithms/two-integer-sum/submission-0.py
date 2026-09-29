class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainingSum = {}
        for i in range(len(nums)):
            if target - nums[i] not in remainingSum:
                remainingSum[nums[i]] = i;
            else:
                return [remainingSum.get(target-nums[i]), i]
        