class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxA = 0
        while l != r:
            if (r - l) * min(height[r], height[l]) > maxA:
                maxA = (r - l) * min(height[r], height[l])
            if height[l] <= height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
        return maxA