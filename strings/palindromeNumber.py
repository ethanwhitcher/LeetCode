class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp = x
        reverse = 0
        while temp:
            remainder = temp % 10
            reverse = reverse * 10 + remainder
            temp = temp // 10
        return x == reverse