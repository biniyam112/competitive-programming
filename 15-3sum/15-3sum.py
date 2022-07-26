class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        negative = []
        positive = []
        zero = []
        
        
        result = set()
        
        for i in nums:
            if i<0:
                negative.append(i)
            elif i>0:
                positive.append(i)
            else:
                zero.append(i)
        
        negativeSet, positiveSet = set(negative), set(positive)
        
        if zero:
            for i in positive:
                if -i in negativeSet:
                    result.add((i,0,-i))
            
        if len(zero)>=3:
            result.add((0,0,0))
            
        for i in range(len(negative)):
            for j in range(i+1,len(negative)):
                sums = negative[i]+negative[j]
                
                if -sums in positiveSet:
                    result.add(tuple(sorted([negative[i], -sums, negative[j]])))
        
        for i in range(len(positive)):
            for j in range(i+1,len(positive)):
                sums = positive[i]+positive[j]
                
                if -sums in negativeSet:
                    result.add(tuple(sorted([positive[i], -sums, positive[j]])))
        
        return result