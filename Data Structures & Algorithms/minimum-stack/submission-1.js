class MinStack {

    constructor() {
        this.minstack = []
        this.stack = []
    }

    /**
     * @param {number} val
     * @return {void}
     */
    push(val) {
        this.stack.push(val)
        if (this.minstack.length === 0){
            this.minstack.push(val)
        }else{
            if(this.minstack[this.minstack.length - 1] >= val){
                this.minstack.push(val)
            }
        }
    }

    /**
     * @return {void}
     */
    pop() {
        let val = this.stack.pop()
        if (this.minstack[this.minstack.length - 1] === val){
            this.minstack.pop()
        }
    }

    /**
     * @return {number}
     */
    top() {
        return this.stack[this.stack.length - 1]
    }

    /**
     * @return {number}
     */
    getMin() {
        return this.minstack[this.minstack.length - 1]
    }
}
