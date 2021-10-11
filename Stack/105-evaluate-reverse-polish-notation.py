import math

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        stack = []
        operators = {'+', '-', '*', '/'}
        
        if len(tokens) == 1:
            return int(tokens[0])
        
        for c in tokens:      
            if c not in operators:
                stack.append(int(c))    
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                result = 0
                if c == "+":
                    result = num1 + num2
                if c == "-":
                    result = num1 - num2
                if c == "*":
                    result = num1 * num2
                if c == "/":
                    result = num1 / num2
                    result = math.trunc(result)
                
                stack.append(result)
                
        
        return stack.pop()