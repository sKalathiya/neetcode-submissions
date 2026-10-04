class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    characterReplacement(s, k) {
        let window = new Map()
        let left = 0
        let max_freq= 0
        let max_length = 0

        for (let right =0 ;right<s.length ; right++){
            window.set(s[right] , (window.get(s[right]) || 0)  + 1)
            max_freq = Math.max(max_freq, window.get(s[right]))
            while (((right - left + 1) - max_freq) > k){
                window.set(s[left], window.get(s[left]) - 1)
                left++
            }
            max_length = Math.max(max_length, (right-left + 1))
        }

        return max_length
    }
}
