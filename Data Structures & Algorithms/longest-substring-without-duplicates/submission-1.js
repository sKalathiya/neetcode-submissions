class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        let left = 0
        let max_length = 0
        let window = new Set()

        for (let right =0; right < s.length ; right++){
            while (window.has(s[right])) {
                window.delete(s[left])
                left++
            }
            window.add(s[right])
            max_length = Math.max(max_length, window.size)
        }

        return max_length
    }
}
