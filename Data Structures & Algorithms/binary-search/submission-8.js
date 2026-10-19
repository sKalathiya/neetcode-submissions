class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        let result = -1
        let left = 0
        let right = nums.length - 1


        while (left <= right){
            const mid = Math.floor((left + right) / 2)

          

            if (target > nums[mid]){
                left = mid + 1
            }
            else if (target < nums[mid]){
                right = mid - 1

            }

            else {
                result = mid
                break
            }
        }
        return result
    }
}
