class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers, target) {
        let i = 0;
        let j = numbers.length - 1

        while (i < j){
            const value = numbers[i] + numbers[j]

            if (value === target){
                return [i+1,j+1]
            }

            if ( value < target) {
                i++
            }

            if ( value > target ){
                j--
            }
        }
    }
}
