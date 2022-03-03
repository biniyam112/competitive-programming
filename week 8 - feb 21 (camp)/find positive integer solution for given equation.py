# """
#    This is the custom function interface.
#    You should not implement it, or speculate about its implementation
from git import List


class CustomFunction:
    #    Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
    #    i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
    def f(self, x, y):
        # lets set the function to just multiplication for testing
        return x * y


class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
      output = []
      for x in range(1,101):
        i = 1
        j = 101
        while i <= j:
          mid = i + (j-i)//2
          if customfunction.f(x,mid) < z:
            i = mid+1
          elif customfunction.f(x,mid) > z:
            j = mid-1
          else:
            output.append([x,mid])
            break
      return output
          