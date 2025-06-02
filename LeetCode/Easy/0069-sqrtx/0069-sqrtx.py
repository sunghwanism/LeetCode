class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 1 , x//2

        while(left <= right):
            mid = left + (right - left)//2
            square = mid * mid

            if x > square:
                left = mid + 1
            
            elif x < square:
                right = mid - 1

            else:
                return mid
        
        return right



