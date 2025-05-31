class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_table = {} # {value:index}

        for i, num in enumerate(nums):

            t = target - num

            if t in hash_table:
                return [hash_table[t], i]

            hash_table[num] = i

        