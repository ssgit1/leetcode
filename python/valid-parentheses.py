class Solution:
    openParenthesis = ['[', '{', '(', '[']
    closeParenthesis = [']', '}', ')', '']
    
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c in self.openParenthesis:
                stack.append(c)
            elif c in self.closeParenthesis:
                if stack and self.closeParenthesis.index(c) == self.openParenthesis.index(stack[-1]):
                    stack.pop()
                else:
                    return False
        # stack has to be empty for valid expression
        return not stack
