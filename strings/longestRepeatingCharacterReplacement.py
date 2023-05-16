class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = {}
        l = 0
        maxString = 0
        for r in range(len(s)):
            charCount[s[r]] = 1 + charCount.get(s[r], 0)
            while (r - l + 1) - max(charCount.values()) > k:
                charCount[s[l]] -= 1
                l += 1
            maxString = max(maxString, r - l + 1) # r - l + 1 is size of window
        return maxString