class Solution:
    def findMin(self, nums: List[int]) -> int:
        def condition(value) -> bool:
            return nums[value] < nums[right]
        
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return nums[left]