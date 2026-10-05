class Solution {
    /**
     * @param {string} s1
     * @param {string} s2
     * @return {boolean}
     */
    checkInclusion(s1, s2) {
        if ( s1.length > s2.length) {
            return false;
        }

        let sMap = new Array(26).fill(0);

        for ( let s of s1){
            const index = s.charCodeAt(0) - 'a'.charCodeAt(0)
            sMap[index] += 1 
        }
        let window = new Array(26).fill(0)

        for (let i = 0; i<s1.length ; i++){
            const index = s2.charCodeAt(i) - 'a'.charCodeAt(0)
            window[index] += 1
        }

        if (this.checkIfWindowMatch(window, sMap)){
            return true;
        }

        let left = 0

        for ( let right = s1.length ; right < s2.length ; right++){

            window[s2.charCodeAt(right) - 'a'.charCodeAt(0)] += 1
            window[s2.charCodeAt(left) - 'a'.charCodeAt(0)] -= 1
            if (this.checkIfWindowMatch(window, sMap)){
                return true
            }
            left++
        }

        return false;

    }

    checkIfWindowMatch(window, sMap) {
    for (let i = 0; i < 26; i++) {
        if (window[i] !== sMap[i]) {
            return false;
        }
    }
    return true;
}
}
