class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        stack = []
        brackets = {
            '{':'}',
            '[':']',
            '(':')'
        }

        for c in s:
            # check karege ki wo open hai kya hai to apend
            if c in brackets:
                stack.append(c)
            else:
                #kya closing bracket same hai stack wale se
                if len(stack) == 0:
                    return False
                if c != brackets[stack[-1]]:
                    return False
                    
                stack.pop()
                
        return len(stack) == 0


        
