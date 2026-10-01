class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        let i = 0;
        let j = s.length - 1;

        while ( i < j){
            if (!isAlphaNumeric(s[i])) {
                i++;
                continue;
            }

            if (!isAlphaNumeric(s[j])) {
                j--;
                continue;
            }

            if ( s[i].toLowerCase() !== s[j].toLowerCase()) return false
            
            i++;
            j--;
        }

        return true;
    }


      
}

function isAlphaNumeric(char) {
    return /^[a-z0-9]$/i.test(char);
    } 
