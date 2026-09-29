class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {};
        for c in s:
            count[c] = count.get(c, 0) + 1
        for c in t:
            counter = count.get(c, 0)
            if  counter == 0:
                return False
            count[c] = counter - 1
        return True
        