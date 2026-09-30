class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyMap = {}
        for num in nums:
            frequencyMap[num] = frequencyMap.get(num, 0) + 1
        
        fMap = sorted(frequencyMap.items(), key= lambda item: item[1], reverse=True)
        result = []
        for i in range(k):
            result.append(fMap[i][0])
        return result

        