class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        bestSum = nums[0]
        currentSum = 0
        for i in range(len(nums)):
            if currentSum < 0:
                currentSum = 0
            currentSum += nums[i]
            bestSum = max(bestSum, currentSum)
        return bestSum