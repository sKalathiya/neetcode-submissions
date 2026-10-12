class Solution {
    /**
     * @param {number} target
     * @param {number[]} position
     * @param {number[]} speed
     * @return {number}
     */
    carFleet(target, position, speed) {
        const cars = position.map((pos, index) => [pos, speed[index]]).sort((a,b) => b[0] - a[0])
        let fleets = 0
        let max_time = 0
        for (let i =0; i<cars.length ; i++){
            const time = (target - cars[i][0]) / cars[i][1]
            if (time > max_time) {
                 fleets++
                 max_time = time
            }
        }

        return fleets
    }
}
