class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let min_price = prices[0]
        let max_price = 0

        for (let i = 1; i<prices.length ; i++){
            max_price = Math.max(max_price , prices[i] - min_price)
            min_price = Math.min(min_price, prices[i])
        }

        return max_price
    }
}
