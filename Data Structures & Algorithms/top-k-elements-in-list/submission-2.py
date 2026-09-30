class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyMap = {}
        for num in nums:
            frequencyMap[num] = frequencyMap.get(num, 0) + 1
        
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in frequencyMap.items():
            bucket[freq].append(num)
        result = []
        total = 0
        for freq in range(len(bucket) - 1, 0, -1):
            for num in bucket[freq]:
                result.append(num)

            if len(result) == k:
                return result
        