class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        let stack = []

        for ( let c of s){
            if (c === "(" || c === "{" || c==="["){
                stack.push(c)
            }else{
                if ( stack.length === 0 || stack[stack.length - 1] !== this.getBracket(c) ) return false
                stack.pop()
            }
        }

        return stack.length === 0
    }

    getBracket(c){
        if (c == "}") return "{"
        if ( c == "]") return "["
        if ( c == ")") return "("
    }
}
