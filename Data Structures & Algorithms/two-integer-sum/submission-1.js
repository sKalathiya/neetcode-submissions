class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const sum = new Map();
        for (let i = 0; i< nums.length ; i++){
            if ((sum.get(target - nums[i]) ?? -1) === -1) 
                sum.set(nums[i] , i);
            else
                return [sum.get(target - nums[i]) , i]
        }
    
    }
}
