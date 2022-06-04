class Solution:
    start = 0
    end = 0
    def longestPalindrome(self, s: str) -> str:
        def helper(low,high):
            while low >= 0 and high < len(s):
                if s[low] == s[high]:
                    low -= 1
                    high += 1
                else:
                    break
            if high-low > self.end-self.start:
                self.start,self.end = low,high
        for i in range(len(s)):
            if i %2 == 1:
                low = i//2
                high = i//2+1
                helper(low,high)
            else:
                low = i //2 - 1
                high = i // 2 + 1
                helper(low,high)
        if self.end == self.start:
            return s[self.end]
        return s[self.start:self.end]
        