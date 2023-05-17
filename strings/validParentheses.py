class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')' : '(', '}' : '{', ']' : '['}
        for c in s: # loop through string
            if c in closeToOpen: # if closing parenthesis 
                if stack and stack[-1] == closeToOpen[c]: # check if value matches dict
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(c)
        return True if not stack else False
            