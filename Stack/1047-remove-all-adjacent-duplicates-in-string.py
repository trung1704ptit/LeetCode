class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        
        for c in s:
            if len(stack) == 0: 
                stack.append(c)
            else:
                # We will check the current value with the top of stack
                # if they are equal we will pop the top of stack and don't put the
                # current character to stack
                if stack[-1] == c:
                    stack.pop()
                else:
                # push curr to stack
                    stack.append(c)
            
            
        return "".join(stack)