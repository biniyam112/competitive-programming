# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def isBadVersion(version:int,badVersion:int):
        return version == badVersion
    def firstBadVersion(self, n: int,badVersion:int) -> int:
      i = 1
      if self.isBadVersion(i):
        return i
      while i > 0 and i < n:
        mid = i + (n-i)//2
        if not self.isBadVersion(mid,badVersion) and self.isBadVersion(mid+1,badVersion):
          return mid+1
        elif self.isBadVersion(mid,badVersion) and self.isBadVersion(mid+1,badVersion):
          n = mid
        else:
          i = mid
        
        