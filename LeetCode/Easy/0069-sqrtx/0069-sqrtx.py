class Solution:
    def mySqrt(self, x: int) -> int:

        val = sqrt(x)
        result = 0
        
        while(val >= 1):
            val -= 1
            result += 1
            
        return result
