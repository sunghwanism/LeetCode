class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n == 0:
            return 1

        def powLoop(base, exp):
            result = 1
            while(exp > 0):
                if exp % 2 == 1:
                    result *= base
                
                base *= base
                exp = exp//2
                # print("Base", base, "exp", exp, "result", result)

            return result

        if n < 0:
            n = -n
            x = 1/x

        return powLoop(x, n)

        