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
            
            if c in brackets:
                stack.append(c)
            
            else:
                if len(stack) == 0:
                    return False
                
                if c != brackets[stack.pop()]:
                    return False
                    
                
                
        return len(stack) == 0


        
