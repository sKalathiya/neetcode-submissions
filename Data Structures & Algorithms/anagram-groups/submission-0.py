class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = {}
        sortedStr = ["".join(sorted(a)) for a in strs]

        for i in range(len(strs)):
            if sortedStr[i] in check:
                ans = check.get(sortedStr[i])
                ans.append(strs[i])
            else:
                check[sortedStr[i]] =  [strs[i]]
        result = []
        for values in check.values():
            result.append(values)
    
        return result
        
        