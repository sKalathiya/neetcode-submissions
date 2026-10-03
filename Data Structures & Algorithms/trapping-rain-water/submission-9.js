class Solution {
    /**
     * @param {number[]} height
     * @return {number}
     */
    trap(height) {
        let left = 0;
        let right = height.length - 1;
        let left_max = height[left];
        let right_max = height[right];
        let total = 0;

        while (left <= right){
            if (left_max <= right_max) {
                left_max = Math.max(left_max, height[left]);
                total = total + (left_max - height[left]);
                left++;
            }else{
                right_max = Math.max(right_max, height[right]);
                total =  total +  (right_max  - height[right]);
                right--;
            }
        }

        return total;
    }
}
