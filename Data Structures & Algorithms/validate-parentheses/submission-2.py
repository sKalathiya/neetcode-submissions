class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        if len(s) < 2:
            return False
        for c in s:
            if c == "(" or c == "{" or c=="[":
                stack.append(c)
            else:
                if len(stack) == 0 or (stack[-1] != self.getOppositeBracket(c)):
                    return False
                else:
                    stack.pop()

        return len(stack) == 0

    def getOppositeBracket(self, c) -> str:
        if c == ")": 
            return "("
        if c == "]": 
            return "["
        if c == "}": 
            return "{"