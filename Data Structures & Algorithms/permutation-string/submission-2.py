class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        sMap = [0] * 26
        for s in s1:
            sMap[ord(s) - ord("a")] += 1
        
        window = [0] * 26
        for index in range(0, len(s1)):
            window[ord(s2[index]) - ord("a")] += 1
        if window == sMap:
            return True
        left = 0
        for right in range(len(s1), len(s2)):
            window[ord(s2[right]) - ord("a")] += 1
            window[ord(s2[left]) - ord("a")] -= 1
            if window == sMap:
                return True
            left+=1
        
        return False

        