class Solution:
    def arraySign(self, nums: List[int]) -> int:
        x = 1
        for n in nums:
            if n == 0:
                return 0
            x *= n
        if x > 0:
            return 1
        elif x < 0:
            return -1