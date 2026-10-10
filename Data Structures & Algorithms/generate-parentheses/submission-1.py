class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        open = 0
        close = 0
        result = []
        stack = [] 
        self.process(open, close, n, result, stack)
        return result

    
    def process(self, open: int, close: int, n: int, result: List[str], stack: List[str]):
        if open == close == n:
            result.append("".join(stack))
            return 
        if open < n:
            stack.append("(")
            open += 1
            self.process(open, close, n, result, stack)
            stack.pop()
            open -= 1
      
        if close < open:
            stack.append(")")
            close += 1
            self.process(open, close, n, result, stack)
            stack.pop()
            close -= 1

       
         
        