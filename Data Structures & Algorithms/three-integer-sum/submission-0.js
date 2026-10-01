class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {
        nums.sort((a,b) => a-b)
        let i = 0 ;
        const result = []

        while( i < nums.length) {
            
            if(i != 0 && nums[i] === nums[i-1]) {
                i++
                continue
            }

            let left = i + 1;
            let right = nums.length - 1;

            while ( left < right) {
                if (left != i+1 && nums[left] === nums[left-1]){
                    left++;
                    continue;
                }

                if (right != nums.length -1 && nums[right] === nums[right + 1]){
                    right--;
                    continue;
                }
                let total = nums[left] + nums[right];
                if ( total === -nums[i]  ){
                    result.push([nums[i], nums[left], nums[right]])
                    left++
                    right--
                }
                if(total < -nums[i] ){
                    left++
                }
                if(total > -nums[i]){
                    right--;
                }
            }

            i++
        }

        return result
    }
}
