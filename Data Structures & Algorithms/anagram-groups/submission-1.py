class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for a in strs:
            count = [0] * 26;
            for ch in a:
                count[ord(ch) - ord("a")] += 1
            c = tuple(count)
            if c in groups:
                groups[c].append(a)
            else:
                groups[c] = [a]
        return list(groups.values())

        
        