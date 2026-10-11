class Solution {
    /**
     * @param {number[]} temperatures
     * @return {number[]}
     */
    dailyTemperatures(temperatures) {
        let stack = []
        let result = Array(temperatures.length).fill(0)

 

        for(let i in temperatures){
     
            if (stack.length === 0){
                stack.push(i)
                continue;
            }

            while (stack.length !== 0 && (temperatures[stack[stack.length - 1]] < temperatures[i]) ){
                let index = stack.pop()
                result[index] = i - index
            }

            stack.push(i)
        }

        return result
    }
}
