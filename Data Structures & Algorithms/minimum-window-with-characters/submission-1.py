class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        min_length = sys.maxsize
        answer = ""
        need= {}
        have = {}
        right = 0
        for c in t:
            need[c] = need.get(c, 0) + 1
        required = len(need)
        while right < len(s):
            currentIndex = s[right]
            have[currentIndex] = have.get(currentIndex ,0) + 1
            if have.get(currentIndex) == need.get(currentIndex):
                required -= 1
            
            if required == 0:
                while required == 0:
                    if min_length > (right - left + 1):
                        min_length = right - left + 1
                        answer = s[left:right+ 1]
                    removeIndex = s[left]
                    have[removeIndex] = have.get(removeIndex,0) - 1
                    if have.get(removeIndex,0) < need.get(removeIndex,0):
                        required += 1
                    left += 1
            right += 1

        return answer




        