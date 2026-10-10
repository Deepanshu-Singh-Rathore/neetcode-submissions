class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = str()
        for i in s:
            if i.isalnum():
                new_str += i
        left, right = 0, len(new_str) - 1
         
        while left < right:
            if new_str[left].lower() != new_str[right].lower():
                return False
            left += 1
            right -= 1
        return True