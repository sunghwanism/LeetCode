class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        n = n+1
        cache = [-1 for _ in range(n+1)]

        def iteration(i):
            if i < 2:
                return i

            if cache[i] != -1:
                return cache[i]

            cache[i] = iteration(i-1) + iteration(i-2)

            return cache[i]

        return iteration(n)
            


