class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        left = 0
        max_freq = 0
        max_length = 0
        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1
            max_freq = max(max_freq, window.get(s[right]))
            while ((right-left + 1) - max_freq) > k:
                window[s[left]] = window.get(s[left]) - 1
                left+=1
            max_length = max(max_length , right-left + 1)
        return max_length

        