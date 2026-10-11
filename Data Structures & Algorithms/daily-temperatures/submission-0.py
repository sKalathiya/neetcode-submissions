class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i, current in enumerate(temperatures):
            if len(stack) == 0: 
                stack.append(i)
                continue
            while len(stack) != 0 and temperatures[stack[-1]] < current:
                index = stack.pop()
                result[index] = i - index
                
                
            
            stack.append(i)
                    
        return result


            
            
