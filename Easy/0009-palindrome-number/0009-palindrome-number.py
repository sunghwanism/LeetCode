class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            x = str(x)
            if x == x[::-1]:
                return True
            else:
                return False


        