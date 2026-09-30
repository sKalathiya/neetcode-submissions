class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyMap = {}
        for num in nums:
            frequencyMap[num] = frequencyMap.get(num, 0) + 1
        
        bucket = [[] for _ in range(len(nums) + 1)]
        for key in frequencyMap.keys():
            bucket[frequencyMap.get(key)] += [key] 
        result = []
        total = 0
        for i in reversed(range(len(bucket))):
            if total == k:
                return result
            if bucket[i] != []:
                print(bucket[i])
                result += bucket[i]
                total += len(bucket[i])
        