class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        sum = 0
        for i, n in enumerate(nums):
            if len(nums) % (i+1) == 0:
                sum += n ** 2
        return sum
            