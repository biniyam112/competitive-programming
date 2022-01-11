    def minNonZeroProduct(self, p: int) -> int:
        def recursion(count,value):
            if count ==1:
                return value
            return value * recursion(count//2,value)**2   % (10**9+7)
        value = (2**p)-2
        count = 2**(p-1)-1
        if count == 0:
            return 1
        return (value+1) * recursion(count,value)  % (10**9+7)
    
    
    
minNonZeroProduct(4)